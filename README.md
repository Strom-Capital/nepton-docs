# nepton-docs

Markdown mirror of the public [Nepton Help Center](https://support.nepton.com/hc/fi),
maintained by a single Python script that hits the public Zendesk Help Center API.

The mirror exists so the docs can be:

- Browsed/searched locally in Cursor (Cmd-P, `rg`, semantic search).
- Ingested into [Context7](https://context7.com/) — Context7's hosted Zendesk crawl
  didn't work for this site, so this repo is a stable substitute.

Current snapshot: **606 articles** in `fi/`, **481 articles** in `en-gb/`, organised
into 5 categories and 83 sections (some nested two levels deep).

## Layout

```
fi/<category-slug>/<section-slug>[/<sub-section-slug>]/<article-id>-<slug>.md
en-gb/...
```

- One Markdown file per article, named `<article_id>-<slug>.md`. The id prefix is what
  lets the crawler detect renames cheaply (rename in Zendesk → `git mv` here, history
  preserved).
- Each article starts with YAML front matter: `id`, `title`, `url`, `locale`,
  `category` / `category_id`, `section` / `section_id`, `section_path`, `labels`,
  `promoted`, `updated_at`, `edited_at`.
- Every category and section folder has an `_index.md` listing its children. These
  are regenerated on every sync so they stay in step with the article tree.
- Article images stay as remote URLs (`https://support.nepton.com/hc/article_attachments/...`).
  Pass `--download-assets` to the script to mirror them into `assets/<id>/` instead.

## Refresh

```sh
make install        # one-time: creates .venv and installs html2text + PyYAML
make sync           # both locales
make sync-fi        # only Finnish
make sync-en        # only English (en-gb)
```

A no-op refresh (everything up to date) takes ~10 seconds and only the taxonomy +
article-list endpoints are hit. The crawler is incremental:

- For each article it compares the API's `updated_at` / `edited_at` against the local
  front matter and **skips** writing if both are unchanged.
- If the title (and thus the slug) changed, the file is **moved** (`<id>-old.md` →
  `<id>-new.md`) instead of being recreated.
- If the article moved to a different section, the file is moved across folders.
- After the article pass, any local `<id>-*.md` whose id no longer exists upstream is
  **pruned**, and empty section folders left behind are removed.

Direct invocations, useful for one-offs:

```sh
.venv/bin/python scripts/sync_help_center.py --locale fi
.venv/bin/python scripts/sync_help_center.py --force                    # rewrite every file
.venv/bin/python scripts/sync_help_center.py --rewrite-internal-links   # rewrite https://support.nepton.com/hc/<locale>/articles/<id>... to relative paths into this repo
.venv/bin/python scripts/sync_help_center.py --download-assets          # mirror <img src=...> targets to assets/<id>/
```

`--rewrite-internal-links` and `--download-assets` are off by default. Toggling either
of them on automatically forces a rewrite of all articles in that run so the body
catches up — they don't replay otherwise unchanged content on every sync.

### Periodic refresh

Run `make sync` on a schedule. Two ready-made options:

- **macOS cron** — daily at 06:00:

  ```cron
  0 6 * * * cd /Users/<you>/code/nepton-docs && /usr/bin/make -s sync >> .venv/sync.log 2>&1
  ```

- **GitHub Actions** — drop this at `.github/workflows/sync.yml`:

  ```yaml
  name: sync
  on:
    schedule: [{ cron: "0 6 * * *" }]
    workflow_dispatch:
  jobs:
    sync:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - uses: actions/setup-python@v5
          with: { python-version: "3.12" }
        - run: pip install -r requirements.txt
        - run: python scripts/sync_help_center.py --locale fi --locale en-gb
        - uses: peter-evans/create-pull-request@v6
          with:
            title: "chore: refresh help-center mirror"
            branch: chore/refresh-help-center
            commit-message: "chore: refresh help-center mirror"
  ```

## Context7 ingestion

Context7 supports public GitHub repos as a source. Push this repo to GitHub and add it
through the Context7 dashboard. The per-article front matter (`title`, `url`, `category`,
`section`) gives Context7 stable anchors that link back to the live help-center URL,
so citations stay accurate even when titles change.

## Internals (script)

[`scripts/sync_help_center.py`](scripts/sync_help_center.py) is a single-file Python
script using only `html2text` + `PyYAML` on top of the standard library. The flow:

1. `categories.json` + `sections.json` → build category/section index, including
   `parent_section_id` chains.
2. `articles.json` (paginated) → list every article for the locale.
3. For each article: figure out the target path, skip / move / write as needed.
4. Walk the locale root, drop articles whose id is gone upstream, remove empty
   directories.
5. Regenerate `_index.md` at the locale root + every category + every section folder.

HTTP failures (429 / 5xx / network) retry up to 3 times with 1s/3s/7s backoff.
Filesystem writes go through a tmp file + `os.replace` so a Ctrl-C never leaves a
half-written article.

## What's deliberately not exported

- Article comments, votes, drafts.
- Cross-locale translation links (each locale is pulled independently).
- The auth-only `/help_center/incremental/articles.json` endpoint — overkill for ~1000
  articles; the public list + per-file `updated_at` diff is enough.
