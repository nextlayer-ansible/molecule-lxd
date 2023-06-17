# Molecule LXD Plugin

[![CI](https://github.com/nextlayer-ansible/molecule-lxd/actions/workflows/tox.yml/badge.svg)](https://github.com/nextlayer-ansible/molecule-lxd/actions/workflows/tox.yml)
[![Python Black Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![Ansible Code of Conduct](https://img.shields.io/badge/Code%20of%20Conduct-Ansible-silver.svg)](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)
[![Repository License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)

*Molecule LXD* allows using [LXD](https://linuxcontainers.org/lxd/) to provision containers or virtual-machines as test resources for [molecule](https://ansible.readthedocs.io/projects/molecule/).

This project is a maintained fork of [ansible-community/molecule-lxd](https://github.com/ansible-community/molecule-lxd), which was archived on January 8, 2023.

## Features

- Use Linux-Containers and Virtual-Machines as test resources for molecule.  
- Configures molecule to connect to the test resources.
- Supports local and remote LXD environments.

## Documentation

A [Quickstart-Tutorial](docs/quickstart.md), [examples](docs/examples.md) and more can be found in the [documentation](docs/index.md).

## Changelog

Notable changes to this project are documented in the [CHANGELOG](CHANGELOG.md).

## License

The [MIT](https://github.com/ansible/molecule/blob/master/LICENSE) License.

The Molecule logo is licensed under the [Creative Commons NoDerivatives 4.0 License](https://creativecommons.org/licenses/by-nd/4.0/).

If you have some other use in mind, contact us.
