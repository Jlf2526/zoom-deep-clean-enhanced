# Development Guide

## Setting Up Development Environment

```bash
# Clone repository
git clone https://github.com/PHLthy215/zoom-deep-clean-enhanced.git
cd zoom-deep-clean-enhanced

# Create virtual environment
python3 -m venv dev_env
source dev_env/bin/activate

# Install in development mode
pip install -e ".[dev]"
```

## Running Tests

```bash
# Run all tests with coverage
pytest tests/ -v --cov=zoom_deep_clean --cov-report=html

# Run specific test file
pytest tests/test_comprehensive.py -v

# View coverage report
open htmlcov/index.html
```

## Code Quality

```bash
# Format code with Black
black zoom_deep_clean/

# Lint with flake8
flake8 zoom_deep_clean/

# Type checking with mypy
mypy zoom_deep_clean/
```

## Project Structure

```
zoom-deep-clean-enhanced/
├── zoom_deep_clean/           # Main package
│   ├── __init__.py
│   ├── cli_enhanced.py        # Command-line interface
│   ├── cleaner_enhanced.py    # Core cleanup logic
│   ├── gui_enhanced.py        # GUI interface
│   └── cross_platform_support.py  # Platform detection
├── tests/                     # Test suite
│   ├── test_comprehensive.py
│   └── test_cli.py
├── docs/                      # Documentation
└── setup.py                   # Package configuration
```

## Testing Strategy

### Unit Tests
- Test individual functions in isolation
- Mock external dependencies
- Cover edge cases and error conditions

### Integration Tests
- Test component interactions
- Validate file system operations
- Test CLI argument parsing

### Coverage Goals
- Core modules: 80%+ coverage
- CLI modules: 60%+ coverage
- Overall project: 70%+ coverage

## Contributing Guidelines

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Write Tests First**
   - Add tests for new functionality
   - Ensure existing tests pass

3. **Follow Code Style**
   - Use Black for formatting
   - Follow PEP 8 guidelines
   - Add type hints where appropriate

4. **Update Documentation**
   - Update relevant .md files
   - Add docstrings to new functions
   - Update CLI help text

5. **Submit Pull Request**
   - Include clear description
   - Reference any issues
   - Ensure CI passes

## Debugging

### Enable Debug Logging
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Common Debug Scenarios
```bash
# Test specific file detection
python3 -c "from zoom_deep_clean.cleaner_enhanced import *; detect_zoom_files(dry_run=True)"

# Test VM detection
python3 -c "from zoom_deep_clean.cross_platform_support import *; print(get_platform_info())"

# Test CLI parsing
python3 zoom_deep_clean/cli_enhanced.py --help
```

## Release Process

1. **Update Version**
   - Bump version in `setup.py`
   - Update `__version__` in `__init__.py`

2. **Update Changelog**
   - Document new features
   - List bug fixes
   - Note breaking changes

3. **Run Full Test Suite**
   ```bash
   pytest tests/ -v --cov=zoom_deep_clean
   ```

4. **Create Release**
   ```bash
   git tag v2.2.1
   git push origin v2.2.1
   ```

## Security Considerations

- Validate all file paths
- Sanitize user inputs
- Use allowlists for system operations
- Log all privileged operations
- Never execute arbitrary user code

## Performance Optimization

- Profile file I/O operations
- Batch filesystem operations
- Use efficient search patterns
- Minimize subprocess calls
- Cache expensive computations