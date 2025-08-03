# Zoom Deep Clean Enhanced - VM-Aware & System-Wide

![Tests](https://github.com/Jlf2526/zoom-deep-clean-enhanced/workflows/Tests/badge.svg)
![Performance Monitoring](https://github.com/Jlf2526/zoom-deep-clean-enhanced/workflows/Performance%20Monitoring/badge.svg)
![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)
![macOS](https://img.shields.io/badge/platform-macOS-lightgrey.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A comprehensive, production-ready Python package for completely removing Zoom's device fingerprinting and persistent identifiers on macOS with enhanced VM support and system-wide cleanup capabilities.

**Created by: PHLthy215**  
**Enhanced Version: 2.2.0 - VM-Aware & System-Wide**

## 📊 Performance Monitoring

This project includes comprehensive performance monitoring to ensure CI/CD pipeline efficiency:

- **Test Execution**: Target <60s (currently ~25-40s)
- **Code Quality**: Target <30s (currently ~15s)  
- **Security Scans**: Target <45s (currently ~25s)
- **Automated Alerts**: Performance regression detection
- **Trend Analysis**: Historical performance tracking

## 🚀 Enhanced Features

### VM-Aware Cleanup
- ✅ **VMware Fusion** detection and process management
- ✅ **VirtualBox** service stopping and cleanup
- ✅ **Parallels Desktop** integration and control
- ✅ **Shared resource** cleanup between host and VMs
- ✅ **Extended grace periods** for VM environments
- ✅ **VM-specific process patterns** detection

### System-Wide Comprehensive Cleanup
- 🔍 **Comprehensive file system search** across all system locations
- 🗂️ **Extended system locations** including /var, /private, /Applications
- 📊 **Detailed remaining file reporting** with full paths
- 🔧 **Enhanced system daemon removal** with better coverage
- 🧹 **Deeper cache cleaning** including VM-related caches
- 🔄 **Optional automatic system reboot** after cleanup

### Production Ready & Secure
- ✅ Comprehensive error handling and logging
- ✅ Enhanced dry-run mode for safe testing
- ✅ Detailed statistics and reporting with VM metrics
- ✅ Graceful failure handling with VM awareness
- ✅ Extended timeout protection for system operations
- ✅ Enhanced JSON report generation
- ✅ Professional CLI interface with VM options
- ✅ **Security hardened** with enhanced validation

### Complete Cleanup (Enhanced)
- 🔄 **VM-aware process termination** (stops VM services first)
- 🔐 Enhanced keychain entries and authentication tokens removal
- 🚫 **System-wide launch agents/daemons** removal with VM support
- 🔧 **Privileged helper tools** and audio drivers with extended patterns
- 🌐 **Enhanced WebKit storage** and HTTP caches cleanup
- 📦 **Extended group containers** and application data removal
- ⚙️ **Comprehensive preference files** and saved states cleanup
- 🧹 **System-wide caches** and receipts with VM-aware patterns
- 🔄 **Enhanced DNS and network** caches flushing
- 🔍 **Post-cleanup verification** with comprehensive file search

### Safety Features (Enhanced)
- 🛡️ macOS platform validation with VM detection
- 🔒 Enhanced permission checks with VM service validation
- 👤 Sudo access verification with extended timeouts
- 📝 Comprehensive logging to file with VM operations
- 🔍 **Enhanced dry-run mode** with VM simulation
- ⚠️ **Detailed user confirmation** prompts with VM warnings
- 💾 **Comprehensive backup functionality** with VM-aware paths
- 🔄 **Optional automatic reboot** with user confirmation

## 📦 Installation

### Option 1: Install Enhanced Package

```bash
# Install the enhanced package
pip install zoom-deep-clean-enhanced

# Run the enhanced cleaner
zoom-deep-clean-enhanced --help
zdce --help  # Short alias
```

### Option 2: Install from Source

```bash
# Clone or download the enhanced package
cd zoom-deep-clean-enhanced

# Install in development mode
pip install -e .

# Or install normally
pip install .
```

### Option 3: Direct Execution

```bash
# Make executable and run directly
chmod +x zoom_deep_clean/cli_enhanced.py
python3 zoom_deep_clean/cli_enhanced.py --help
```

## 🖥️ Enhanced Usage

### Command Line Interface

```bash
# Basic enhanced usage (VM-aware by default)
zoom-deep-clean-enhanced

# Skip confirmation with VM awareness
zoom-deep-clean-enhanced --force

# Preview with VM simulation (safe)
zoom-deep-clean-enhanced --dry-run --verbose

# Full cleanup with automatic reboot
zoom-deep-clean-enhanced --system-reboot --force

# Disable VM awareness if not needed
zoom-deep-clean-enhanced --no-vm

# Comprehensive cleanup with all features
zoom-deep-clean-enhanced --verbose --vm-aware --system-reboot

# Short alias usage
zdce --dry-run --verbose
```

### Python API

```python
from zoom_deep_clean import ZoomDeepCleanerEnhanced

# Create enhanced cleaner instance
cleaner = ZoomDeepCleanerEnhanced(
    log_file="/tmp/zoom_clean_enhanced.log",
    verbose=True,
    dry_run=True,  # Safe preview mode
    vm_aware=True,  # Enable VM support
    system_reboot=False  # Don't auto-reboot
)

# Run the enhanced cleanup
success = cleaner.run_deep_clean()

if success:
    print("Enhanced cleanup completed successfully!")
else:
    print("Enhanced cleanup completed with errors.")
```

## 📋 Enhanced Command Line Options

| Option | Short | Description |
|--------|-------|-------------|
| `--help` | `-h` | Show help message and exit |
| `--version` | | Show version number |
| `--dry-run` | | Preview operations without making changes |
| `--verbose` | `-v` | Enable detailed logging |
| `--log-file LOG_FILE` | | Custom log file path |
| `--force` | `-f` | Skip confirmation prompts |
| `--no-backup` | | Disable automatic backup functionality |
| `--vm-aware` | | Enable VM-aware cleanup (default: enabled) |
| `--no-vm` | | Disable VM-aware cleanup |
| `--system-reboot` | | Automatically reboot system after cleanup |
| `--comprehensive-search` | | Perform comprehensive file system search (default: enabled) |

## 📁 Enhanced Output Files

The enhanced package generates several output files:

1. **Enhanced Log File**: `~/Documents/zoom_deep_clean_enhanced.log` (default)
   - Detailed execution log with timestamps and VM operations
   - Error messages and warnings with VM context
   - Debug information with VM process details (with --verbose)

2. **Enhanced Report File**: `~/Documents/zoom_cleanup_enhanced_report.json`
   - JSON summary with VM-aware cleanup statistics
   - Timestamp and enhanced version information
   - Success/failure status with VM operation results
   - Comprehensive file search results

## 🗂️ What Gets Removed (Enhanced)

### VM-Aware Process Management
- **VMware Fusion** processes and services
- **VirtualBox** VMs and background services
- **Parallels Desktop** VMs and dispatcher services
- **Shared VM resources** and temporary files
- **VM-specific Zoom processes** with extended patterns

### Enhanced Security & Authentication
- **Extended keychain entries** including SSO and presence
- **VM-shared authentication tokens** and certificates
- **Cross-platform stored passwords** and credentials
- **VM-synchronized security data**

### System Integration (Enhanced)
- **VM-aware launch agents** and daemons
- **Extended privileged helper tools** with VM patterns
- **VM-shared audio driver** integration
- **Enhanced system receipts** and caches with VM data
- **Cross-platform system integration** files

### Application Data (Enhanced)
- **VM-synchronized application** support files
- **Extended caches** and temporary files including VM data
- **VM-shared logs** and crash reports
- **Cross-platform preference** files and settings
- **VM-aware saved application** states

### Web & Network (Enhanced)
- **VM-shared WebKit storage** and cookies
- **Cross-platform HTTP storage** and binary cookies
- **Enhanced DNS cache** entries with VM awareness
- **VM-aware network connection** states

## ⚙️ Enhanced Requirements

- **macOS only** (Darwin platform) with VM software detection
- **Python 3.7+** with enhanced libraries
- **sudo privileges** (for system-level and VM cleanup)
- **Terminal/command line access** with extended permissions
- **Optional VM software** (VMware Fusion, VirtualBox, Parallels Desktop)

## 🛡️ Enhanced Safety Notes

⚠️ **Important Enhanced Warnings:**

1. **VM-Aware Complete Removal**: This package stops VMs and completely removes ALL Zoom data
2. **VM Service Interruption**: Running VMs will be stopped during cleanup
3. **System-Wide Search**: Comprehensive file system search may take time
4. **Reinstallation Required**: You will need to reinstall Zoom from scratch after running this
5. **Sudo Required**: System-level and VM cleanup requires administrator privileges
6. **Backup Recommended**: Enhanced backup covers VM-shared data as well
7. **Automatic Reboot**: Optional system reboot ensures complete cleanup

## 🔧 Enhanced Development

### Setting up Enhanced Development Environment

```bash
# Clone the enhanced repository
git clone https://github.com/phlthy215/zoom-deep-clean-enhanced.git
cd zoom-deep-clean-enhanced

# Install in development mode with dev dependencies
pip install -e ".[dev]"

# Run enhanced tests
pytest tests/

# Format code
black zoom_deep_clean/

# Lint code
flake8 zoom_deep_clean/

# Type checking
mypy zoom_deep_clean/
```

## 🚨 Enhanced Troubleshooting

### VM-Related Issues
```bash
# Check VM services status
launchctl list | grep -E "(vmware|virtualbox|parallels)"

# Manually stop VM services if needed
sudo launchctl stop com.vmware.fusion
sudo launchctl stop org.virtualbox.app.VBoxSVC
sudo launchctl stop com.parallels.desktop.launchdaemon
```

### Enhanced Permission Errors
```bash
# Ensure proper permissions for VM operations
chmod +x zoom-deep-clean-enhanced

# For VM and system-level operations
sudo zoom-deep-clean-enhanced --vm-aware
```

### Comprehensive Search Issues
```bash
# If comprehensive search is slow, disable it
zoom-deep-clean-enhanced --no-comprehensive-search

# Or specify custom timeout in code
```

## 📊 Enhanced Example Workflow

1. **Enhanced Preview First** (Recommended):
   ```bash
   zoom-deep-clean-enhanced --dry-run --verbose --vm-aware
   ```

2. **Stop VMs Manually** (Optional):
   ```bash
   # Stop VMs through their interfaces first
   # Or let the script handle it automatically
   ```

3. **Run Enhanced Cleanup**:
   ```bash
   zoom-deep-clean-enhanced --force --vm-aware --system-reboot
   ```

4. **Check Enhanced Results**:
   ```bash
   # View the enhanced log
   cat ~/Documents/zoom_deep_clean_enhanced.log
   
   # View the enhanced report
   cat ~/Documents/zoom_cleanup_enhanced_report.json
   ```

5. **System Restart** (Automatic or Manual):
   ```bash
   # If --system-reboot was used, system reboots automatically
   # Otherwise restart manually:
   sudo reboot
   ```

6. **Reinstall and Verify**:
   ```bash
   # Download and install fresh Zoom
   # Your system will appear as a completely new device
   # VMs will also see Zoom as new installation
   ```

## 📈 Enhanced Exit Codes

- `0`: Success - enhanced cleanup completed without errors
- `1`: Failure - enhanced cleanup completed with errors (check log file)
- `2`: Security Error - operation aborted for security reasons
- `130`: User Cancellation - operation cancelled by user (Ctrl+C) - all completed operations were successful

## 🤝 Contributing to Enhanced Version

1. Fork the enhanced repository
2. Create a feature branch with VM or system-wide improvements
3. Make your changes with enhanced security in mind
4. Add tests for VM-aware functionality if applicable
5. Run the enhanced test suite
6. Submit a pull request with detailed VM/system changes

## 📄 License

MIT License - Use at your own risk. This enhanced package makes significant system and VM changes.

## 🔗 Enhanced Links

- **Enhanced Documentation**: [GitHub Repository](https://github.com/phlthy215/zoom-deep-clean-enhanced)
- **Bug Reports**: [Issues](https://github.com/phlthy215/zoom-deep-clean-enhanced/issues)
- **PyPI Package**: [zoom-deep-clean-enhanced](https://pypi.org/project/zoom-deep-clean-enhanced/)

## ⚡ Enhanced Quick Start

```bash
# Install enhanced version
pip install zoom-deep-clean-enhanced

# Preview with VM awareness (safe)
zoom-deep-clean-enhanced --dry-run --vm-aware

# Run comprehensive cleanup with auto-reboot
zoom-deep-clean-enhanced --force --system-reboot

# Check enhanced results
cat ~/Documents/zoom_deep_clean_enhanced.log
cat ~/Documents/zoom_cleanup_enhanced_report.json
```

## 🆕 What's New in Enhanced v2.2.0

### VM-Aware Features
- **VMware Fusion** complete integration
- **VirtualBox** service management
- **Parallels Desktop** process control
- **VM-specific process patterns** detection
- **Shared resource cleanup** between host and VMs

### System-Wide Enhancements
- **Comprehensive file system search** across all locations
- **Extended system location coverage** (/var, /private, /Applications)
- **Enhanced remaining file detection** and reporting
- **Deeper system cache cleaning** with VM awareness
- **Optional automatic system reboot** functionality

### Security & Reliability
- **Enhanced command validation** with VM context
- **Extended timeout handling** for system operations
- **Improved error handling** with VM-specific errors
- **Enhanced backup functionality** covering VM-shared data
- **Comprehensive audit logging** with VM operations

---

**⚠️ Enhanced Warning: Use at your own risk. This enhanced tool makes significant system and VM changes and requires administrator privileges. Always test with --dry-run first in VM environments.**
