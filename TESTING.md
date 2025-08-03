# Testing Guide - Zoom Deep Clean Enhanced

## Overview

This document outlines testing procedures, coverage expectations, and quality standards for the Zoom Deep Clean Enhanced project.

## Quick Start

```bash
# Set up test environment
python3 -m venv test_env
source test_env/bin/activate
pip install -r test-requirements.txt

# Run all tests with coverage
python3 -m pytest tests/ -v --cov=zoom_deep_clean --cov-report=html

# View coverage report
open htmlcov/index.html
```

## Test Environment Setup

### Prerequisites
- macOS 12.x+ (Monterey, Ventura, Sonoma, Sequoia)
- Python 3.9+
- Virtual environment (recommended)
- Zoom application installed (for integration tests)

### Installation
```bash
# Clone repository
git clone https://github.com/Jlf2526/zoom-deep-clean-enhanced.git
cd zoom-deep-clean-enhanced

# Create isolated test environment
python3 -m venv test_env
source test_env/bin/activate

# Install test dependencies
pip install -r test-requirements.txt
pip install black  # Code formatting
pip install -e .
```

## Test Categories

### 1. CLI Tests (`tests/test_cli_enhanced.py`)
- **Purpose**: Test command-line interface functionality  
- **Coverage**: Argument parsing, error handling, exit codes
- **Tests**: 28 comprehensive tests
- **Runtime**: ~0.1 seconds
- **Command**: `pytest tests/test_cli_enhanced.py -v`

### 2. Core Functionality Tests (`tests/test_comprehensive.py`)
- **Purpose**: Test security, file detection, system analysis
- **Coverage**: Main ZoomDeepCleanerEnhanced class and utilities
- **Tests**: 20 tests
- **Runtime**: ~1 second  
- **Command**: `pytest tests/test_comprehensive.py -v`

### 3. macOS Compatibility Tests (`tests/test_macos_compatibility.py`)
- **Purpose**: Test across multiple macOS versions
- **Coverage**: File system, commands, platform-specific behavior
- **Tests**: 26 tests
- **Runtime**: ~0.5 seconds
- **Command**: `pytest tests/test_macos_compatibility.py -v`

### 4. Dry Run Edge Cases (`tests/test_dry_run_edge_cases.py`)
- **Purpose**: Test safe preview mode without system changes
- **Coverage**: Edge cases, error handling, JSON export
- **Tests**: 14 tests
- **Runtime**: ~0.3 seconds
- **Command**: `pytest tests/test_dry_run_edge_cases.py -v`

### 5. Integration Tests (`tests/test_integration.py`)
- **Purpose**: Test module interactions and imports
- **Coverage**: Cross-module compatibility, circular import detection
- **Tests**: 5 tests
- **Runtime**: ~0.2 seconds
- **Command**: `pytest tests/test_integration.py -v`

**Total Test Count**: 93 tests across all modules

## Coverage Expectations

### Current Status (Week 2 - COMPLETED)
```
Module                          Coverage    Target    Status
───────────────────────────────────────────────────────────
cleaner_enhanced.py            65%         60%       ✅ EXCEEDS
security_enhancements.py       59%         50%       ✅ EXCEEDS  
advanced_features.py           53%         50%       ✅ EXCEEDS
cli_enhanced.py                55%         40%       ✅ EXCEEDS
macos_compatibility.py         77%         50%       ✅ EXCEEDS
advanced_detection.py          35%         40%       ⚠️  CLOSE
cross_platform_support.py     20%         30%       ❌ GAP
gui_app.py                     0%          20%       ❌ NOT TESTED
gui_simple.py                  0%          20%       ❌ NOT TESTED
performance_monitoring.py     19%         30%       ❌ GAP
───────────────────────────────────────────────────────────
TOTAL                          35%         40%       ⚠️  CLOSE
```

### Weekly Targets
- **Week 1**: 30% overall (✅ ACHIEVED)
- **Week 2**: 60% core modules, 40% overall (✅ CORE EXCEEDED, OVERALL CLOSE)
- **Week 3**: 70% core modules, 50% overall
- **Week 4**: 80% core modules, 60% overall

### Priority Modules for Coverage
1. `cleaner_enhanced.py` - Core cleanup logic
2. `security_enhancements.py` - Security validation
3. `cli_enhanced.py` - Command line interface
4. `advanced_features.py` - Enhanced functionality

## Running Tests

### Basic Test Execution
```bash
# All tests
pytest tests/ -v

# Specific test file
pytest tests/test_comprehensive.py -v

# Specific test class
pytest tests/test_comprehensive.py::TestZoomDeepCleanerEnhanced -v

# Specific test method
pytest tests/test_comprehensive.py::TestZoomDeepCleanerEnhanced::test_cleaner_initialization -v
```

### Coverage Analysis
```bash
# Generate coverage report
pytest tests/ --cov=zoom_deep_clean --cov-report=html --cov-report=term

# Coverage for specific module
pytest tests/ --cov=zoom_deep_clean.cleaner_enhanced --cov-report=term

# Missing lines report
pytest tests/ --cov=zoom_deep_clean --cov-report=term-missing
```

### Performance Testing
```bash
# Run with timing
pytest tests/ -v --durations=10

# Profile test execution
pytest tests/ --profile

# Memory usage monitoring
pytest tests/ --memray
```

## Test Scenarios

### Scenario 1: Clean System (No Zoom)
```bash
# Simulate system without Zoom installed
pytest tests/ -k "test_no_zoom" -v
```

### Scenario 2: Fresh Zoom Installation
```bash
# Test with newly installed Zoom
pytest tests/ -k "test_fresh_install" -v
```

### Scenario 3: Heavily Used Zoom
```bash
# Test with extensive Zoom usage history
pytest tests/ -k "test_heavy_usage" -v
```

### Scenario 4: VM Environment
```bash
# Test VM-aware functionality
pytest tests/ -k "test_vm" -v
```

### Scenario 5: Permission Restrictions
```bash
# Test with limited permissions
pytest tests/ -k "test_permission" -v
```

## Continuous Integration

### GitHub Actions
- **Trigger**: Every push and pull request
- **Environments**: macOS-latest
- **Python Versions**: 3.9, 3.10, 3.11, 3.12
- **Coverage Threshold**: 30% minimum

### Local CI Simulation
```bash
# Run full CI suite locally
./scripts/run_ci_tests.sh

# Check code quality
black --check setup.py scripts/ tests/ zoom_deep_clean/
flake8 zoom_deep_clean/
mypy zoom_deep_clean/

# Format code (if needed)
black setup.py scripts/ tests/ zoom_deep_clean/
```

## Test Data Management

### Mock Data Location
- `tests/fixtures/` - Test data files
- `tests/mocks/` - Mock objects and responses
- `tests/samples/` - Sample Zoom files for testing

### Creating Test Data
```bash
# Generate test fixtures
python3 tests/generate_fixtures.py

# Create mock Zoom installation
python3 tests/create_mock_zoom.py
```

## Debugging Failed Tests

### Common Issues
1. **Permission Errors**: Run with appropriate permissions
2. **Path Issues**: Check macOS version compatibility
3. **Mock Failures**: Verify mock data is current
4. **Timing Issues**: Increase timeouts for slow systems

### Debug Commands
```bash
# Verbose output with print statements
pytest tests/ -v -s

# Drop into debugger on failure
pytest tests/ --pdb

# Run only failed tests
pytest tests/ --lf

# Show local variables on failure
pytest tests/ -l
```

## Platform-Specific Testing

### macOS Versions
- **Monterey (12.x)**: Core compatibility
- **Ventura (13.x)**: Enhanced features
- **Sonoma (14.x)**: Latest features
- **Sequoia (15.x)**: Beta testing

### VM Software Testing
- **VMware Fusion**: Process detection and control
- **VirtualBox**: Service management
- **Parallels Desktop**: Integration testing

## Quality Gates

### Pre-Commit Checks
- [ ] All tests pass
- [ ] Coverage meets minimum threshold
- [ ] Code formatted with Black
- [ ] No security vulnerabilities
- [ ] Code style compliance
- [ ] Documentation updated

### Release Criteria
- [ ] 100% test pass rate
- [ ] Coverage targets met
- [ ] Manual testing completed
- [ ] Performance benchmarks passed
- [ ] Security audit clean

## Troubleshooting

### Test Environment Issues
```bash
# Reset test environment
rm -rf test_env
python3 -m venv test_env
source test_env/bin/activate
pip install -r test-requirements.txt
```

### Permission Problems
```bash
# Fix test file permissions
chmod +x tests/*.py
sudo chown -R $(whoami) tests/
```

### Coverage Reporting Issues
```bash
# Clear coverage cache
rm -rf .coverage htmlcov/
pytest tests/ --cov=zoom_deep_clean --cov-report=html
```

## Contributing Tests

### Test Writing Guidelines
1. **Descriptive Names**: `test_should_detect_zoom_files_when_present`
2. **Arrange-Act-Assert**: Clear test structure
3. **Single Responsibility**: One concept per test
4. **Mock External Dependencies**: No real system changes
5. **Parameterized Tests**: Test multiple scenarios

### Example Test Structure
```python
def test_should_clean_zoom_files_when_dry_run_disabled(self):
    # Arrange
    cleaner = ZoomDeepCleanerEnhanced(dry_run=False)
    mock_files = ['/path/to/zoom/file.plist']
    
    # Act
    result = cleaner.clean_files(mock_files)
    
    # Assert
    assert result.success is True
    assert result.files_removed == 1
```

## Performance Benchmarks

### Target Execution Times
- **Unit Tests**: < 2 seconds total
- **Integration Tests**: < 5 seconds total
- **Full Test Suite**: < 10 seconds total

### Memory Usage Limits
- **Peak Memory**: < 100MB during testing
- **Memory Leaks**: Zero tolerance
- **Cleanup**: All resources released

## Security Testing

### Security Test Categories
1. **Path Traversal**: Prevent directory escape
2. **Input Validation**: Sanitize all inputs
3. **Permission Escalation**: Verify privilege requirements
4. **Data Exposure**: No sensitive data in logs

### Security Commands
```bash
# Run security-focused tests
pytest tests/ -k "security" -v

# Check for hardcoded secrets
grep -r "password\|secret\|key" zoom_deep_clean/

# Validate file permissions
find . -name "*.py" -perm +111 | head -10
```

---

## Quick Reference

### Essential Commands
```bash
# Full test run with coverage
pytest tests/ -v --cov=zoom_deep_clean --cov-report=html

# Fast test run (no coverage)
pytest tests/ -x

# Test specific functionality
pytest tests/ -k "cleaner" -v

# Generate coverage report
coverage html && open htmlcov/index.html

# Format code with Black
black setup.py scripts/ tests/ zoom_deep_clean/

# Check formatting
black --check setup.py scripts/ tests/ zoom_deep_clean/
```

### Coverage Targets by Week
- Week 1: 30% ✅
- Week 2: 40% 
- Week 3: 50%
- Week 4: 60%

### Support
- **Issues**: Create GitHub issue with `testing` label
- **Questions**: Check existing test files for examples
- **CI Problems**: Review `.github/workflows/tests.yml`

---

*Last Updated: August 3, 2025*
*Version: 1.0*
