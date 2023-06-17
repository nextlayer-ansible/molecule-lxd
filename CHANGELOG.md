# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [0.5.0] - 2023-06-17

### Added

- Add test scenarios
- Add documentation and examples

### Changed
- Use canonical/setup-lxd Github action to set up LXD

### Fixed
- Hardcoded "security.nesting" key from config in create.yml should be removed (#1)
- Fix destroy playbook for virtual-machines

## [v0.4.0a0] - 2022-02-18

### Changed
- Update driver to match latest requirements (#25) @bonddim
- Update ansible connection options (#26) @bonddim

### Fixed
- Fix functional tests after pytest-helpers-namespace drop (#17) @bonddim

## [0.3] - 2021-06-22

### Changed
- Added retries to create and destroy playbooks (#14) @bonddim
- Switch from freenode to libera.chat (#15) @bonddim

## [0.2] - 2021-03-02

### Changed
- Updated plugin to use newer molecule APIs (#7) @bonddim

## [0.1] - 2020-10-29

### Changed
- Made driver compatible with molecule 3.2 (#6) @ssbarnea

