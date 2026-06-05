#!/usr/bin/env python3
"""
Sync the Nepton Zendesk Help Center into this repo as Markdown.

Public API only (no auth). For each locale we:

  1. Fetch categories.json + sections.json (paginated).
  2. Fetch articles.json (paginated).
  3. Write one Markdown file per article at
     <locale>/<category-slug>/<section-slug-chain>/<id>-<slug>.md
     with YAML front matter that records the API's updated_at; skip writes when the
     local file is already up to date.
  4. Rebuild _index.md TOCs at each category/section folder.
  5. Prune any local <id>-*.md whose id is no longer returned by the API.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

import html2text
import yaml

API_BASE = "https://support.nepton.com/api/v2/help_center"
USER_AGENT = "nepton-docs-sync/1.0 (+https://github.com/)"
PAGE_SIZE = 100
RETRY_DELAYS_SEC = [1, 3, 7]
INTER_REQUEST_SLEEP_SEC = 0.2

REPO_ROOT = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------


def http_get_json(url: str) -> dict[str, Any]:
    last_err: Exception | None = None
    for attempt in range(len(RETRY_DELAYS_SEC) + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
            status = getattr(e, "code", None)
            transient = status in (429, 500, 502, 503, 504) or status is None
            if not transient or attempt == len(RETRY_DELAYS_SEC):
                raise
            delay = RETRY_DELAYS_SEC[attempt]
            print(f"  retry in {delay}s after {e!r} ({url})", file=sys.stderr)
            time.sleep(delay)
            last_err = e
    if last_err:
        raise last_err
    raise RuntimeError("unreachable")


def http_get_bytes(url: str) -> bytes:
    last_err: Exception | None = None
    for attempt in range(len(RETRY_DELAYS_SEC) + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.read()
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
            status = getattr(e, "code", None)
            transient = status in (429, 500, 502, 503, 504) or status is None
            if not transient or attempt == len(RETRY_DELAYS_SEC):
                raise
            delay = RETRY_DELAYS_SEC[attempt]
            print(f"  retry in {delay}s after {e!r} ({url})", file=sys.stderr)
            time.sleep(delay)
            last_err = e
    if last_err:
        raise last_err
    raise RuntimeError("unreachable")


def paginate(url: str, key: str) -> Iterable[dict[str, Any]]:
    """Yield items from a paginated Zendesk endpoint."""
    next_url: str | None = url
    while next_url:
        data = http_get_json(next_url)
        for item in data.get(key, []):
            yield item
        next_url = data.get("next_page")
        if next_url:
            time.sleep(INTER_REQUEST_SLEEP_SEC)


# ---------------------------------------------------------------------------
# Slugs / paths
# ---------------------------------------------------------------------------

_SLUG_FALLBACK_RE = re.compile(r"[^\w\-]+", re.UNICODE)


def slug_from_html_url(html_url: str | None, fallback_name: str, fallback_id: int) -> str:
    """
    Zendesk html_urls end with `<id>-<slug>` where <slug> is already URL-safe.
    Decode and strip the leading id so the slug round-trips Finnish letters cleanly.
    """
    if html_url:
        tail = html_url.rstrip("/").rsplit("/", 1)[-1]
        decoded = urllib.parse.unquote(tail)
        prefix = f"{fallback_id}-"
        if decoded.startswith(prefix):
            decoded = decoded[len(prefix) :]
        decoded = decoded.strip("-").strip()
        if decoded:
            return _sanitize_path_segment(decoded)
    return _sanitize_path_segment(_slugify(fallback_name) or str(fallback_id))


def _sanitize_path_segment(s: str) -> str:
    s = unicodedata.normalize("NFC", s)
    # Forbid path separators and other characters that confuse filesystems.
    s = s.replace("/", "-").replace("\\", "-")
    s = re.sub(r"[\x00-\x1f\x7f]", "", s)
    s = s.strip(" .-")
    return s or "untitled"


def _slugify(name: str) -> str:
    name = unicodedata.normalize("NFKD", name)
    name = name.encode("ascii", "ignore").decode("ascii")
    name = name.strip().lower()
    name = re.sub(r"[\s/]+", "-", name)
    name = _SLUG_FALLBACK_RE.sub("", name)
    name = re.sub(r"-+", "-", name).strip("-")
    return name


# ---------------------------------------------------------------------------
# Taxonomy
# ---------------------------------------------------------------------------


@dataclass
class Category:
    id: int
    name: str
    slug: str
    description: str
    html_url: str


@dataclass
class Section:
    id: int
    name: str
    slug: str
    category_id: int
    parent_section_id: int | None
    description: str
    html_url: str


@dataclass
class Taxonomy:
    categories: dict[int, Category] = field(default_factory=dict)
    sections: dict[int, Section] = field(default_factory=dict)

    def section_chain(self, section_id: int) -> list[Section]:
        """Walk parent_section_id up to the root; return root-first order."""
        chain: list[Section] = []
        seen: set[int] = set()
        cur = self.sections.get(section_id)
        while cur and cur.id not in seen:
            chain.append(cur)
            seen.add(cur.id)
            cur = self.sections.get(cur.parent_section_id) if cur.parent_section_id else None
        chain.reverse()
        return chain


def fetch_taxonomy(locale: str) -> Taxonomy:
    print(f"[{locale}] fetching taxonomy...")
    tax = Taxonomy()
    for c in paginate(
        f"{API_BASE}/{locale}/categories.json?per_page={PAGE_SIZE}", "categories"
    ):
        tax.categories[c["id"]] = Category(
            id=c["id"],
            name=c["name"],
            slug=slug_from_html_url(c.get("html_url"), c["name"], c["id"]),
            description=c.get("description") or "",
            html_url=c.get("html_url") or "",
        )
    for s in paginate(
        f"{API_BASE}/{locale}/sections.json?per_page={PAGE_SIZE}", "sections"
    ):
        tax.sections[s["id"]] = Section(
            id=s["id"],
            name=s["name"],
            slug=slug_from_html_url(s.get("html_url"), s["name"], s["id"]),
            category_id=s["category_id"],
            parent_section_id=s.get("parent_section_id"),
            description=s.get("description") or "",
            html_url=s.get("html_url") or "",
        )
    print(f"[{locale}]   {len(tax.categories)} categories, {len(tax.sections)} sections")
    return tax


def fetch_articles(locale: str) -> list[dict[str, Any]]:
    print(f"[{locale}] fetching articles...")
    items = list(
        paginate(
            f"{API_BASE}/{locale}/articles.json?per_page={PAGE_SIZE}"
            "&sort_by=updated_at&sort_order=desc",
            "articles",
        )
    )
    print(f"[{locale}]   {len(items)} articles")
    return items


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------


def make_html2md() -> html2text.HTML2Text:
    h = html2text.HTML2Text()
    h.body_width = 0
    h.unicode_snob = True
    h.ignore_links = False
    h.protect_links = True
    h.wrap_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    h.ignore_tables = False
    h.single_line_break = True
    h.mark_code = True
    return h


def render_markdown(
    article: dict[str, Any],
    *,
    category: Category,
    sections: list[Section],
    section_path_names: list[str],
    rewrite_links: dict[int, str] | None,
    asset_rewrites: dict[str, str] | None,
    h: html2text.HTML2Text,
) -> str:
    body_html: str = article.get("body") or ""

    if rewrite_links:
        body_html = _rewrite_internal_links(body_html, rewrite_links)
    if asset_rewrites:
        for src, dst in asset_rewrites.items():
            body_html = body_html.replace(src, dst)

    body_md = h.handle(body_html).rstrip()

    front_matter = {
        "id": article["id"],
        "title": article["title"],
        "url": article.get("html_url") or "",
        "locale": article.get("locale") or "",
        "category": category.name,
        "category_id": category.id,
        "section": sections[-1].name if sections else "",
        "section_id": sections[-1].id if sections else None,
        "section_path": section_path_names,
        "labels": article.get("label_names") or [],
        "promoted": bool(article.get("promoted")),
        "updated_at": article.get("updated_at") or "",
        "edited_at": article.get("edited_at") or "",
    }
    fm_yaml = yaml.safe_dump(
        front_matter, allow_unicode=True, sort_keys=False, default_flow_style=False
    ).rstrip()

    return f"---\n{fm_yaml}\n---\n\n# {article['title']}\n\n{body_md}\n"


_INTERNAL_LINK_RE = re.compile(
    r"https?://support\.nepton\.com/hc/(?P<locale>[a-z\-]+)/articles/(?P<id>\d+)(?:-[^\s\"'<>)]*)?"
)


def _rewrite_internal_links(html: str, id_to_relpath: dict[int, str]) -> str:
    def repl(m: re.Match[str]) -> str:
        article_id = int(m.group("id"))
        rel = id_to_relpath.get(article_id)
        return rel if rel else m.group(0)

    return _INTERNAL_LINK_RE.sub(repl, html)


# ---------------------------------------------------------------------------
# Front-matter helpers
# ---------------------------------------------------------------------------

_FRONT_MATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def read_front_matter(path: Path) -> dict[str, Any] | None:
    try:
        with path.open("r", encoding="utf-8") as f:
            head = f.read(8192)
    except OSError:
        return None
    m = _FRONT_MATTER_RE.match(head)
    if not m:
        return None
    try:
        loaded = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None
    return loaded if isinstance(loaded, dict) else None


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        f.write(content)
    os.replace(tmp, path)


# ---------------------------------------------------------------------------
# Filesystem index of existing articles (id -> existing path)
# ---------------------------------------------------------------------------

_ID_FILE_RE = re.compile(r"^(\d+)-.*\.md$")


def index_existing(locale_root: Path) -> dict[int, Path]:
    found: dict[int, Path] = {}
    if not locale_root.exists():
        return found
    for p in locale_root.rglob("*.md"):
        if p.name.startswith("_"):
            continue
        m = _ID_FILE_RE.match(p.name)
        if not m:
            continue
        try:
            article_id = int(m.group(1))
        except ValueError:
            continue
        found.setdefault(article_id, p)
    return found


# ---------------------------------------------------------------------------
# Asset download
# ---------------------------------------------------------------------------

_IMG_SRC_RE = re.compile(r"""<img[^>]+src=["']([^"']+)["']""", re.IGNORECASE)


def download_assets(
    article_id: int, body_html: str, repo_root: Path, article_dir: Path
) -> dict[str, str]:
    """Download <img src=...> targets into assets/<id>/ and return src->relpath rewrites,
    where the rewritten path is relative to ``article_dir``."""
    rewrites: dict[str, str] = {}
    asset_dir = repo_root / "assets" / str(article_id)
    for m in _IMG_SRC_RE.finditer(body_html):
        src = m.group(1)
        if not src.startswith(("http://", "https://")):
            continue
        if src in rewrites:
            continue
        try:
            data = http_get_bytes(src)
        except Exception as e:
            print(f"    asset download failed: {src} ({e!r})", file=sys.stderr)
            continue
        name = urllib.parse.unquote(urllib.parse.urlparse(src).path.rsplit("/", 1)[-1]) or "asset"
        name = _sanitize_path_segment(name)
        target = asset_dir / name
        n = 1
        while target.exists() and target.read_bytes() != data:
            stem, _, ext = name.rpartition(".")
            if not stem:
                stem, ext = name, ""
            target = asset_dir / (f"{stem}-{n}.{ext}" if ext else f"{stem}-{n}")
            n += 1
        if not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        rel = os.path.relpath(target, article_dir)
        rewrites[src] = rel.replace(os.sep, "/")
    return rewrites


# ---------------------------------------------------------------------------
# Sync orchestration
# ---------------------------------------------------------------------------


def sync_locale(
    locale: str,
    *,
    repo_root: Path,
    force: bool,
    rewrite_internal_links: bool,
    download_assets_flag: bool,
) -> None:
    tax = fetch_taxonomy(locale)
    articles = fetch_articles(locale)

    locale_root = repo_root / locale
    locale_root.mkdir(parents=True, exist_ok=True)
    existing = index_existing(locale_root)

    # First pass: figure out the target path for every article (needed before we render
    # so that --rewrite-internal-links can produce relative links between articles).
    @dataclass
    class Plan:
        article: dict[str, Any]
        category: Category
        sections: list[Section]
        target_path: Path
        target_dir: Path
        existing_path: Path | None

    plans: list[Plan] = []
    seen_ids: set[int] = set()
    skipped_no_section = 0
    skipped_no_category = 0

    for art in articles:
        sec_id = art.get("section_id")
        if not sec_id or sec_id not in tax.sections:
            skipped_no_section += 1
            continue
        sec_chain = tax.section_chain(sec_id)
        if not sec_chain:
            skipped_no_section += 1
            continue
        cat = tax.categories.get(sec_chain[0].category_id)
        if not cat:
            skipped_no_category += 1
            continue

        slug = slug_from_html_url(art.get("html_url"), art.get("name") or art["title"], art["id"])
        filename = f"{art['id']}-{slug}.md"
        target_dir = locale_root / cat.slug
        for s in sec_chain:
            target_dir = target_dir / s.slug
        target_path = target_dir / filename

        plans.append(
            Plan(
                article=art,
                category=cat,
                sections=sec_chain,
                target_path=target_path,
                target_dir=target_dir,
                existing_path=existing.get(art["id"]),
            )
        )
        seen_ids.add(art["id"])

    if skipped_no_section or skipped_no_category:
        print(
            f"[{locale}]   skipped: no_section={skipped_no_section} "
            f"no_category={skipped_no_category}"
        )

    # Lookup of all known article ids -> their absolute target paths. We resolve to a
    # path relative to the *current* article's directory at render time.
    id_to_target: dict[int, Path] | None = None
    if rewrite_internal_links:
        id_to_target = {p.article["id"]: p.target_path for p in plans}

    h = make_html2md()
    written = 0
    moved = 0
    skipped = 0

    for plan in plans:
        art = plan.article

        # Move from stale path/name if needed (cheap regardless of content change).
        if plan.existing_path and plan.existing_path != plan.target_path:
            plan.target_dir.mkdir(parents=True, exist_ok=True)
            try:
                plan.existing_path.replace(plan.target_path)
                moved += 1
                plan.existing_path = plan.target_path
            except OSError as e:
                print(f"    rename failed {plan.existing_path} -> {plan.target_path}: {e!r}",
                      file=sys.stderr)

        if not force and plan.existing_path == plan.target_path and plan.target_path.exists():
            fm = read_front_matter(plan.target_path)
            if (
                fm
                and fm.get("updated_at") == (art.get("updated_at") or "")
                and fm.get("edited_at") == (art.get("edited_at") or "")
                # If the user toggled --rewrite-internal-links / --download-assets after a
                # previous sync, force a rewrite so the body picks up the new linking.
                and not rewrite_internal_links
                and not download_assets_flag
            ):
                skipped += 1
                continue

        asset_rewrites: dict[str, str] | None = None
        if download_assets_flag:
            try:
                asset_rewrites = download_assets(
                    art["id"], art.get("body") or "", repo_root, plan.target_dir
                )
            except Exception as e:
                print(f"    asset pass failed for {art['id']}: {e!r}", file=sys.stderr)
                asset_rewrites = None

        link_rewrites: dict[int, str] | None = None
        if id_to_target:
            link_rewrites = {
                aid: os.path.relpath(target, plan.target_dir).replace(os.sep, "/")
                for aid, target in id_to_target.items()
                if aid != art["id"]
            }

        section_path_names = [s.name for s in plan.sections]
        md = render_markdown(
            art,
            category=plan.category,
            sections=plan.sections,
            section_path_names=section_path_names,
            rewrite_links=link_rewrites,
            asset_rewrites=asset_rewrites,
            h=h,
        )
        atomic_write(plan.target_path, md)
        written += 1

    pruned = prune_deleted(locale_root, seen_ids)
    write_indexes(locale, locale_root, tax, plans)

    print(
        f"[{locale}] done: wrote={written} skipped={skipped} moved={moved} pruned={pruned}"
    )


def prune_deleted(locale_root: Path, seen_ids: set[int]) -> int:
    pruned = 0
    if not locale_root.exists():
        return 0
    for p in locale_root.rglob("*.md"):
        if p.name.startswith("_"):
            continue
        m = _ID_FILE_RE.match(p.name)
        if not m:
            continue
        try:
            aid = int(m.group(1))
        except ValueError:
            continue
        if aid in seen_ids:
            continue
        try:
            p.unlink()
            pruned += 1
        except OSError:
            pass
    # Sweep empty directories left behind by prunes/moves.
    for d in sorted(locale_root.rglob("*"), key=lambda x: len(x.parts), reverse=True):
        if d.is_dir():
            try:
                next(d.iterdir())
            except StopIteration:
                try:
                    d.rmdir()
                except OSError:
                    pass
    return pruned


# ---------------------------------------------------------------------------
# Index pages (_index.md)
# ---------------------------------------------------------------------------


def write_indexes(
    locale: str, locale_root: Path, tax: Taxonomy, plans: list["object"]
) -> None:
    """Generate _index.md at locale root, each category, and each section folder."""
    # Group plans by directory.
    from collections import defaultdict

    articles_by_dir: dict[Path, list[Any]] = defaultdict(list)
    for p in plans:  # type: ignore[assignment]
        articles_by_dir[p.target_dir].append(p)  # type: ignore[attr-defined]

    # Precompute set of section directories that actually have content (article or sub).
    all_dirs: set[Path] = set()
    for d in articles_by_dir:
        cur = d
        while cur != locale_root and cur != cur.parent:
            all_dirs.add(cur)
            cur = cur.parent

    # Locale root index: list categories that have any content.
    cat_dirs = sorted({d for d in all_dirs if d.parent == locale_root})
    lines = [f"# Nepton Help Center ({locale})", ""]
    if cat_dirs:
        lines.append("## Categories")
        for d in cat_dirs:
            cat = _category_for_slug(tax, d.name)
            label = cat.name if cat else d.name
            lines.append(f"- [{label}]({d.name}/_index.md)")
    atomic_write(locale_root / "_index.md", "\n".join(lines) + "\n")

    # Category indexes.
    for cat_dir in cat_dirs:
        cat = _category_for_slug(tax, cat_dir.name)
        title = cat.name if cat else cat_dir.name
        body = [f"# {title}", ""]
        if cat and cat.description:
            body += [cat.description, ""]
        # List immediate child section folders (sorted by name) and any direct articles.
        child_section_dirs = sorted(
            d for d in all_dirs if d.parent == cat_dir
        )
        if child_section_dirs:
            body.append("## Sections")
            for d in child_section_dirs:
                sec = _section_for_slug(tax, d.name, cat.id if cat else None)
                label = sec.name if sec else d.name
                body.append(f"- [{label}]({d.name}/_index.md)")
            body.append("")
        direct_articles = sorted(
            articles_by_dir.get(cat_dir, []), key=lambda p: p.article["title"].lower()
        )
        if direct_articles:
            body.append("## Articles")
            for p in direct_articles:
                body.append(f"- [{p.article['title']}]({p.target_path.name})")
            body.append("")
        atomic_write(cat_dir / "_index.md", "\n".join(body).rstrip() + "\n")

    # Section indexes (every directory that isn't a category).
    section_dirs = sorted(d for d in all_dirs if d.parent != locale_root)
    for sec_dir in section_dirs:
        sec = _section_for_slug(tax, sec_dir.name)
        title = sec.name if sec else sec_dir.name
        body = [f"# {title}", ""]
        if sec and sec.description:
            body += [sec.description, ""]
        child_dirs = sorted(d for d in all_dirs if d.parent == sec_dir)
        if child_dirs:
            body.append("## Subsections")
            for d in child_dirs:
                child_sec = _section_for_slug(tax, d.name)
                body.append(f"- [{child_sec.name if child_sec else d.name}]({d.name}/_index.md)")
            body.append("")
        articles_here = sorted(
            articles_by_dir.get(sec_dir, []), key=lambda p: p.article["title"].lower()
        )
        if articles_here:
            body.append("## Articles")
            for p in articles_here:
                body.append(f"- [{p.article['title']}]({p.target_path.name})")
            body.append("")
        atomic_write(sec_dir / "_index.md", "\n".join(body).rstrip() + "\n")


def _category_for_slug(tax: Taxonomy, slug: str) -> Category | None:
    for c in tax.categories.values():
        if c.slug == slug:
            return c
    return None


def _section_for_slug(tax: Taxonomy, slug: str, category_id: int | None = None) -> Section | None:
    for s in tax.sections.values():
        if s.slug != slug:
            continue
        if category_id is not None and s.category_id != category_id:
            continue
        return s
    return None


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--locale",
        action="append",
        choices=["fi", "en-gb"],
        help="Locale to sync; pass multiple times. Default: both.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Rewrite every article even if updated_at is unchanged.",
    )
    parser.add_argument(
        "--rewrite-internal-links",
        action="store_true",
        help="Rewrite https://support.nepton.com/hc/<locale>/articles/<id>... links to "
        "relative paths to the local Markdown file when the target is in this export.",
    )
    parser.add_argument(
        "--download-assets",
        action="store_true",
        help="Download <img src=...> targets to assets/<id>/ and rewrite the body.",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=REPO_ROOT,
        help="Repo root (default: parent of this script).",
    )
    args = parser.parse_args(argv)

    locales = args.locale or ["fi", "en-gb"]

    for locale in locales:
        sync_locale(
            locale,
            repo_root=args.repo_root,
            force=args.force,
            rewrite_internal_links=args.rewrite_internal_links,
            download_assets_flag=args.download_assets,
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
