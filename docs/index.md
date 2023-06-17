# Molecule LXD

*Molecule LXD* is a driver plugin for the [Ansible](https://docs.ansible.com/ansible/latest/index.html) test
runner [molecule](https://ansible.readthedocs.io/projects/molecule/) and allows
using [LXD](https://linuxcontainers.org/lxd/) to provision containers or virtual-machines as test resources by using
the [Ansible LXD container module](https://docs.ansible.com/ansible/latest/collections/community/general/lxd_container_module.html).
The plugin supports local and remote LXD environments, and configures molecule to connect to the test resources using
the [Ansible LXD connection plugin](https://docs.ansible.com/ansible/latest/collections/community/general/lxd_connection.html).

## Topics

- [Quickstart](quickstart.md)
- [Requirements](requirements.md)
- [Platform Options](platform-options.md)
- [Examples](examples.md)
- [Development](development.md)
- [Changelog](../CHANGELOG.md)

## Further reading

- [Molecule Documentation](https://molecule.readthedocs.io/)
- [LXD Getting-Started-Guide](https://linuxcontainers.org/lxd/getting-started-cli/)
- [LXD Documentation](https://linuxcontainers.org/lxd/docs/latest/)
