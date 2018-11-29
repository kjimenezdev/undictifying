SHELL=/bin/bash

.DEFAULT_GOAL := help

.PHONY: help
help: ## Prints target and a help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) |  \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


#################################################################
# Project
#################################################################

.PHONY: lint
lint:  ## Run lint tools
	@pylint --output-format=colorized main.py
	@mypy main.py

.PHONY: install
install: ## Install the application dependencies
	@poetry install

.PHONY: run
run: ## Run the project
	@python main.py
