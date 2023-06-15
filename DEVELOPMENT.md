# Development

## Requirements

```sh
sudo apt install make python3-venv
```

## Makefile

Use the Makefile targets to run tests or build the package:

```sh
make help

Usage:
  make help                 show this message
  make clean                remove intermediate files

  make lint                 run all linters

  make test-py38            run tests with python 3.8
  make test-py39            run tests with python 3.9
  make test-py310           run tests with python 3.10

  make build                build the package
```
