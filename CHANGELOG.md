# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.2.1] - 2025-08-03

### Added
- Testing infrastructure with pytest, pytest-cov, pytest-mock
- GitHub Actions CI/CD pipeline with macOS testing
- Virtual environment setup for development
- Comprehensive test suite with 27 tests
- Test coverage measurement (30% baseline)
- Module integration testing
- METRICS.md for tracking project health
- CHANGELOG.md for version tracking

### Fixed
- User cancellation misleading error messages
- CLI shows clear cancellation vs error distinction
- Exit code 130 for user cancellation (Ctrl+C)
- Exit code 1 for actual errors
- Black code formatting compliance
- Unicode emoji encoding issues in CI

### Changed
- Reorganized enhancement modules into package structure
- Improved error messaging with ASCII text instead of Unicode emojis
- Enhanced user feedback for cancellation scenarios

### Technical
- All 27 tests passing
- 30% code coverage established
- CI pipeline running successfully
- Clean git history with proper tagging

## [2.2.0] - 2025-08-02

### Added
- VM-aware cleanup functionality
- Enhanced system-wide file search
- Advanced fingerprint detection
- Cross-platform support foundation
- Performance monitoring capabilities
- Security enhancements
- GUI applications (simple and advanced)
- Comprehensive documentation

### Features
- VMware Fusion, VirtualBox, Parallels Desktop support
- Keychain comprehensive scanning
- MDM profile detection
- System UUID detection
- MAC address spoofing (VM environments)
- Hostname reset functionality
- Backup and restore capabilities
- JSON report generation

### Security
- Path validation and sanitization
- Command injection prevention
- File verification with signatures
- Comprehensive audit logging
- Enhanced permission checks
