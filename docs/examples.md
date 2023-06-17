# Examples

## Minimal

```yaml
driver:
  name: lxd

platforms:
  - name: instance
    source_alias: ubuntu/jammy/amd64
```

## Container

```yaml
driver:
  name: lxd

platforms:
  - name: instance
    groups:
        - my_group
    source:
       alias: ubuntu/jammy/amd64
       type: image
       mode: pull
       server: https://images.linuxcontainers.org
       protocol: simplestreams
    config:
      security.nesting: "true"
      security.syscalls.intercept.mknod: "true"
      security.syscalls.intercept.setxattr: "true"
```

## Virtual-Machine

```yaml
driver:
  name: lxd

platforms:
  - name: instance
    groups:
      - my_group
    source_alias: focal
    type: virtual-machine
    config:
      limits.cpu: "2"
      limits.memory: 2GB
      user.user-data: |
          #cloud-config
          growpart:
            mode: auto
            devices:
              - '/'
              - '/dev/sda'
              - '/dev/sda2'
            ignore_growroot_disabled: false
    devices:
      config:
        source: cloud-init:config
        type: disk
      eth0:
        nictype: bridged
        parent: lxdbr0
        type: nic
      root:
        path: /
        pool: default
        size: 5GB
        type: disk
```

