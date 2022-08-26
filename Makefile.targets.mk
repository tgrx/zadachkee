.PHONY: setup
setup: setup-python
	$(call log, configuring the project)


.PHONY: setup-python
setup-python:
	$(call log, configuring Python)
	./setup_python.sh


.PHONY: format
format:
	$(call log, reorganizing imports & formatting code)
	isort --virtual-env="$(DIR_VENV)" .
	black .


.PHONY: qa
qa: clean-garbage tests coverage code-typing code-format code-linters
	$(call log, QA checks)


.PHONY: tests
tests:
	$(call log, running all tests)
	pytest


.PHONY: coverage
coverage:
	$(call log, calculating coverage)
	coverage html
	coverage xml


.PHONY: clean-garbage-coverage
clean-garbage-coverage:
	$(call log, cleaning Coverage garbage)
	coverage erase
	rm -rf "$(DIR_ARTIFACTS)/coverage"


.PHONY: clean-garbage-mypy
clean-garbage-mypy:
	$(call log, cleaning Mypy garbage)
	rm -rf "$(DIR_ARTIFACTS)/mypy"


.PHONY: clean-garbage-pytest
clean-garbage-pytest:
	$(call log, cleaning Mypy garbage)
	rm -rf "$(DIR_ARTIFACTS)/pytest"


.PHONY: clean-garbage
clean-garbage: clean-garbage-mypy clean-garbage-pytest clean-garbage-coverage
	$(call log, cleaning garbage)


.PHONY: code-typing
code-typing:
	$(call log, checking code typing)
	mypy


.PHONY: code-format
code-format:
	$(call log, checking code format)
	isort --virtual-env="$(DIR_VENV)" --check-only .
	black --check .


.PHONY: code-linters
code-linters:
	$(call log, linting)
	flake8


.PHONY: sh
sh:
	$(call log, starting Python shell)
	ipython


.PHONY: venv
venv:
	$(call log, installing packages)
	poetry install --no-root


.PHONY: venv-update
venv-update:
	$(call log, upgrading all packages in virtualenv)
	poetry update
