# Makefile for CleanDrop / dropbox-cleaner

# Load environment variables from .env if present
ifneq (,$(wildcard .env))
	include .env
	export $(shell sed 's/=.*//' .env)
endif

.PHONY: install labels test lint clean env help

## 🛠️ Setup and Dependencies
install:
	pip install -r requirements.txt

## 🔖 Sync GitHub Labels (requires GH_LABELS_TOKEN in .env)
labels:
	github-label-sync -l .github/.github-labels.json jasonhuang8/dropbox-cleaner --access-token $(GITHUB_TOKEN) --allow-added-labels
## 🧪 Run Tests
test:
	pytest tests/

## 🧹 Code Linting
lint:
	flake8 core/ cli/ tests/

## 🧼 Cleanup
clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
	rm -rf .pytest_cache

## 🔄 Load .env into current shell
env:
	@echo "Loaded environment variables from .env"

## 🆘 Help
help:
	@echo "Makefile commands:"
	@echo "  make install     - Install dependencies"
	@echo "  make labels      - Sync GitHub labels"
	@echo "  make test        - Run tests"
	@echo "  make lint        - Run flake8 lint checks"
	@echo "  make clean       - Clean up cache files"