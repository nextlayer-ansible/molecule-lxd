# Quickstart

This tutorial requires a working local LXD environment. Learn how to set up one in the [requirements section](requirements.md) of the docs.   

## Installation

Install the *molecule LXD* plugin:
```sh
pip install git+https://github.com/nextlayer-ansible/molecule-lxd.git@main#egg=molecule-lxd
```

## Create a scenario

### With a new role

Create a new role `my-role` with a molecule default scenario using the `lxd` driver:
```sh
molecule init role -d lxd my-role
```

### In a pre-existing role

Create a molecule default scenario using the `lxd` driver:
```sh
molecule init scenario -d lxd
```

### Example scenario definition

Here's a simple `molecule.yml` example scenario definition, if you want to add it by hand:
```yml
driver:
  name: lxd
platforms:
  - name: instance
    source_alias: ubuntu/jammy/amd64
provisioner:
  name: ansible
verifier:
  name: ansible
```

## Run tests

After configuration, you can run molecule:  
```sh
molecule test
```

## Further reading

More examples can be found in the [example section](examples.md).
