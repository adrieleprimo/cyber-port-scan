# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Added functionality to save open ports in an `open_ports.txt` file.
- Added door service type to `open_ports.txt` file.
- Added more type of ports to `port_services`.
- Implemented threading in the port scanning process to improve speed and efficiency

### Changed
- Improved the output message in the terminal to display only open ports.
- Changing the return from None to "" in `scan_port.py`.
- Dictionary `port_services` moved to a separate file `services.py`for better organization.

### Fixed
- Fixed bug where port scanning did not correctly handle unreachable hosts.

## [1.0.0] - 2024-07-07
### Added
- First version of Cyber Port.
- Added basic functionality for scanning ports from 1 to 1024.
- Added MIT license file.
