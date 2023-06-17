# Platform Options

*Molecule LXD* allows a wide degree of customisation via platform arguments. Most of them are passed to the
underlying [Ansible LXD container module](https://docs.ansible.com/ansible/latest/collections/community/general/lxd_container_module.html)
without changes. Because this module uses the LXD API, you can look at
the [LXD OpenAPI documentation](https://linuxcontainers.org/lxd/api/master/#/instances/instances_post) to get the latest
options.

| Variable                | Default                                                                                                                          | Description                                                                                  |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| name                    |                                                                                                                                  | Instance name, used for the internal Ansible inventory and as LXD instance name.             |
| groups                  | `[]`                                                                                                                             | Inventory groups, the instance should be a member of.                                        |
| type                    | `container`                                                                                                                      | Instance type. Choice of: `container`, `virtual-machine`                                     |
| architecture            | `x86_64`                                                                                                                         | Instance architecture. Choice of: `x86_64`, `i686`                                           |
| source_type             | `image`                                                                                                                          | Source type.                                                                                 |
| source_mode             | `pull`                                                                                                                           | Source mode: Whether to use `pull` or `push` mode.                                           |
| source_server           | `https://images.linuxcontainers.org` (if type=container)<br>`https://cloud-images.ubuntu.com/releases` (if type=virtual-machine) | Source remote server URL (to get remote images).                                             |
| source_alias            | `ubuntu/jammy/amd64`                                                                                                             | Source image alias name.                                                                     |
| source_protocol         | `simplestreams`                                                                                                                  | Source protocol name (for remote image).                                                     |
| source                  | `{}`                                                                                                                             | The source for the instance. See [source section](#source).                                  |
| profiles                | `[]`                                                                                                                             | Profiles to be used by the instance.                                                         |
| config                  | `{}`                                                                                                                             | The config for the instance. See [config section](#config).                                  |
| devices                 | `{}`                                                                                                                             | The devices for the instance. See [devices section](#devices).                               |
| ignore_volatile_options | `false`                                                                                                                          | If `true`, config options starting with `volatile.` are ignored                              |
| url                     | `unix:/var/lib/lxd/unix.socket`                                                                                                  | The unix domain socket path or the https URL for the LXD server.                             |
| snap_url                | `unix:/var/snap/lxd/common/lxd/unix.socket`                                                                                      | The unix domain socket path when LXD is installed by snap package manager.                   |
| target                  |                                                                                                                                  | For cluster deployments. Will attempt to create an instance on a target node.                |
| project                 |                                                                                                                                  | Project of an instance.                                                                      |
| cert_file               | `${HOME}/.config/lxc/client.crt`                                                                                                 | The client certificate file path.                                                            |
| key_file                | `${HOME}/.config/lxc/client.key`                                                                                                 | The client certificate key file path.                                                        |
| trust_password          |                                                                                                                                  | The client trusted password.                                                                 |
| wait_for_ipv4_addresses | `true`                                                                                                                           | If `true`, the create playbook waits until IPv4 addresses are set to all network interfaces. |
| timeout                 | `600`                                                                                                                            | Timeout for creating or destroying the instance.                                             |
| force_stop              | `true`                                                                                                                           | If `true`, the instance will be forced to stop.                                              |
| install_basic_packages  | `false`                                                                                                                          | If `true`, some basic packages will be installed in the prepare phase.                       |

## Source

A dict with options to define the source for the instance.
This dict is defaulted to the options starting with `source_`.

Example:

```yaml
platforms:
    -   name: my-instance
        source:
            alias: ubuntu/bionic/amd64
```

The above example is equal to the following example:

```yaml
platforms:
    -   name: my-instance
        source_alias: ubuntu/bionic/amd64
```

## Config

The config for the instance.

Example:

```yaml
platforms:
    -   name: my-instance
        config:
            "limits.cpu": "2"
            "security.nesting": "true"
```

## Devices

The devices for the instance.

Example:

```yaml
platforms:
    -   name: my-instance
        devices:
            kvm:
                path: /dev/kvm
                type: unix-char
```
