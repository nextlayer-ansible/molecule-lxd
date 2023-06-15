.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo "Usage:"
	@echo "  make help                 show this message"
	@echo "  make clean                remove intermediate files"
	@echo
	@echo "  make lint                 run all linters"
	@echo
	@echo "  make test-py38            run tests with python 3.8"
	@echo "  make test-py39            run tests with python 3.9"
	@echo "  make test-py310           run tests with python 3.10"
	@echo
	@echo "  make build                build the package"


RUN_VENV = .venv
RUN_VENV_BIN = $(RUN_VENV)/bin

$(RUN_VENV_BIN)/activate: setup.cfg tox.ini pyproject.toml
	python3 -m venv $(RUN_VENV)
	$(RUN_VENV_BIN)/pip install tox
	. $(RUN_VENV_BIN)/activate && python3 --version

# Allow to pass-through arguments to ansible-playbook
ifeq (tox,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "good"
  RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(RUN_ARGS):;@:)
endif

.PHONY: tox
tox: $(RUN_VENV_BIN)/activate
	. $(RUN_VENV_BIN)/activate && tox $(RUN_ARGS)

.PHONY: lint
lint: $(RUN_VENV_BIN)/activate
	. $(RUN_VENV_BIN)/activate && tox -e lint

.PHONY: test-py38
test-py38: $(RUN_VENV_BIN)/activate
	. $(RUN_VENV_BIN)/activate && tox -e py38

.PHONY: test-py39
test-py39: $(RUN_VENV_BIN)/activate
	. $(RUN_VENV_BIN)/activate && tox -e py39

.PHONY: test-py310
test-py310: $(RUN_VENV_BIN)/activate
	. $(RUN_VENV_BIN)/activate && tox -e py310

.PHONY: build
build: $(RUN_VENV_BIN)/activate
	. $(RUN_VENV_BIN)/activate && tox -e packaging

clean:
	rm -rf .venv/
	rm -rf .tox/
	rm -rf .molecule/
	rm -rf dist
	rm -rf src/molecule_lxd.egg-info/
