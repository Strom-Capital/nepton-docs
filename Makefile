PYTHON ?= python3
VENV   := .venv
PIP    := $(VENV)/bin/pip
PY     := $(VENV)/bin/python

.PHONY: sync sync-fi sync-en venv install clean help

help:
	@echo "Targets:"
	@echo "  make sync       - sync both locales (fi, en-gb)"
	@echo "  make sync-fi    - sync only Finnish"
	@echo "  make sync-en    - sync only English (en-gb)"
	@echo "  make install    - create .venv and install requirements"
	@echo "  make clean      - remove .venv"

$(VENV)/bin/activate: requirements.txt
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --quiet --upgrade pip
	$(PIP) install --quiet -r requirements.txt
	@touch $(VENV)/bin/activate

install: $(VENV)/bin/activate
venv: $(VENV)/bin/activate

sync: install
	$(PY) scripts/sync_help_center.py --locale fi --locale en-gb --llms-full

sync-fi: install
	$(PY) scripts/sync_help_center.py --locale fi --llms-full

sync-en: install
	$(PY) scripts/sync_help_center.py --locale en-gb --llms-full

clean:
	rm -rf $(VENV)
