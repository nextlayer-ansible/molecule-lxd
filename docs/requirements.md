# Requirements

## LXD Environment

*Molecule LXD* requires a working [LXD environment](https://linuxcontainers.org/lxd/docs/latest/), either local or remote.

Instructions on installing LXD can be found in the [LXD documentation](https://linuxcontainers.org/lxd/docs/latest/installing/) and on the [LXD website](https://linuxcontainers.org/lxd/getting-started-cli/).

### Example setup on Ubuntu

Install LXD via snaps:
```sh
snap install lxd
```

Initialize LXD:
```sh
lxd init --minimal
```
Other initialization options are described in the [LXD documentation](https://linuxcontainers.org/lxd/docs/latest/howto/initialize/).


