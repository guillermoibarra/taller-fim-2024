.DEFAULT_GOAL := help
.PHONY: test help

help:  ## these help instructions
	@sed -rn 's/^([a-zA-Z_-]+):.*?## (.*)$$/"\1" "\2"/p' < $(MAKEFILE_LIST)|xargs printf "make %-20s# %s\n"

hidden: # example undocumented, for internal usage only
	@true

install: ## Run `poetry install`
	poetry install

showdeps: ## run poetry to show deps
	@echo "CURRENT:"
	poetry show --tree
	@echo
	@echo "LATEST:"
	poetry show --latest

check: ## runs a pre-commit check
	poetry run pre-commit run --all-files

lint: ## run poetry flake8 for linking
	poetry run flake8 --statistic --show-source

sort: ## run isort for formatting
	poetry run isort .

mypy: ## run mypy type hinting error
	poetry run mypy .

test: hidden ## run pytest with coverage
	poetry run pytest --cov -v tests --cov-branch --cov-report term-missing
