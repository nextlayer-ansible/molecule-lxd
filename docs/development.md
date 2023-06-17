# Development

## Requirements

```sh
sudo apt install make python3-venv
```

## Testing

*Molecule LXD* has a few codestyle, unit and functional tests. It uses [Tox](https://tox.readthedocs.io/en/latest/)
factors to generate a matrix of python x unit/functional tests.
Please note, that you have to set up python on your own.

### Run all tests

```sh
make test
```

### Run linter

```sh
make lint
```

### Run tests for a specific python version

```sh
make test-py39
```

## Makefile

Use the Makefile target `help` to get all options:

```sh
make help
```

Output:

```text
Usage:
  make help                 show this message
  make clean                remove intermediate files

  make lint                 run all linters

  make test                 run all tests. Allows passing arguments to tox.
  make test-py38            run tests with python 3.8
  make test-py39            run tests with python 3.9
  make test-py310           run tests with python 3.10

  make build                build the package
```
