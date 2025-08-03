# Zoom Deep Clean Enhanced - Comprehensive Usage Guide

## Quick Start

### Option 1: Automated Installation and Execution (Recommended)
```bash
cd /Users/user/Documents/zoom-deep-clean-enhanced
./install-and-run.sh
```

### Option 2: Manual Installation and Execution
```bash
# Install the package
cd /Users/user/Documents/zoom-deep-clean-enhanced
pip3 install -e .

# Run dry-run first (safe preview)
zoom-deep-clean-enhanced --dry-run --verbose --vm-aware

# Run actual cleanup
zoom-deep-clean-enhanced --force --vm-aware --system-reboot
```

## VM Environment Specific Usage

### For VMware Fusion Users
```bash
# The script automatically detects and handles VMware Fusion
zoom-deep-clean-enhanced --vm-aware --verbose

# If you want to manually stop VMs first:
# 1. Close all VMs through VMware Fusion interface
# 2. Quit VMware Fusion completely
# 3. Run the cleanup
zoom-deep-clean-enhanced --force --vm-aware
```

### For VirtualBox Users
```bash
# The script handles VirtualBox automatically
zoom-deep-clean-enhanced --vm-aware --verbose

# Manual VM shutdown (optional):
# 1. Save state or shut down all VMs
# 2. Close VirtualBox Manager
# 3. Run cleanup
zoom-deep-clean-enhanced --force --vm-aware
```

### For Parallels Desktop Users
```bash
# Automatic Parallels handling
zoom-deep-clean-enhanced --vm-aware --verbose

# Manual preparation (optional):
# 1. Shut down all VMs
# 2. Quit Parallels Desktop
# 3. Run cleanup
zoom-deep-clean-enhanced --force --vm-aware
```

### For Multiple VM Software
```bash
# The script handles all VM software simultaneously
zoom-deep-clean-enhanced --vm-aware --verbose --system-reboot
```

## Command Line Options Explained

### Basic Options
- `--dry-run`: Preview what would be removed without making changes
- `--verbose`: Show detailed logging and progress information
- `--force`: Skip confirmation prompts (use with caution)

### VM-Specific Options
- `--vm-aware`: Enable VM detection and management (default: enabled)
- `--no-vm`: Disable VM-aware features if not needed

### System Options
- `--system-reboot`: Automatically reboot after cleanup
- `--comprehensive-search`: Perform thorough file system search (default: enabled)

### Safety Options
- `--no-backup`: Disable automatic backup (not recommended)
- `--log-file PATH`: Specify custom log file location

## Step-by-Step Workflow

### 1. Preparation Phase
```bash
# Check system status
ps aux | grep -i zoom
launchctl list | grep -E "(vmware|virtualbox|parallels)"

# Run dry-run to preview
zoom-deep-clean-enhanced --dry-run --verbose
```

### 2. Execution Phase
```bash
# Full cleanup with all features
zoom-deep-clean-enhanced --force --vm-aware --system-reboot --verbose
```

### 3. Verification Phase
```bash
# Check cleanup results
cat ~/Documents/zoom_deep_clean_enhanced.log
cat ~/Documents/zoom_cleanup_enhanced_report.json

# Manual verification
find /Users -iname "*zoom*" 2>/dev/null
find /Library -iname "*zoom*" 2>/dev/null
ps aux | grep -i zoom
```

## Troubleshooting Common Issues

### VM Services Won't Stop
```bash
# Force stop VM services
sudo launchctl stop com.vmware.fusion
sudo launchctl stop org.virtualbox.app.VBoxSVC  
sudo launchctl stop com.parallels.desktop.launchdaemon

# Kill VM processes directly
sudo pkill -f "vmware"
sudo pkill -f "VirtualBox"
sudo pkill -f "prl_"
```

### Permission Denied Errors
```bash
# Ensure sudo access
sudo -v

# Run with explicit sudo for system operations
sudo zoom-deep-clean-enhanced --force --vm-aware
```

### Cleanup Incomplete
```bash
# Run comprehensive search manually
find / -iname "*zoom*" -type f 2>/dev/null | head -20

# Re-run cleanup with extended options
zoom-deep-clean-enhanced --force --vm-aware --comprehensive-search --verbose
```

### Log Files Too Large
```bash
# Check log file sizes
ls -lh ~/Documents/zoom_deep_clean_enhanced.log

# Use custom log location if needed
zoom-deep-clean-enhanced --log-file /tmp/zoom_clean.log
```

## Advanced Usage Scenarios

### Corporate/Managed Environment
```bash
# Disable interactive prompts and auto-reboot
zoom-deep-clean-enhanced --force --no-reboot --vm-aware

# Use custom log location for centralized logging
zoom-deep-clean-enhanced --force --log-file /var/log/zoom_cleanup.log
```

### Development/Testing Environment
```bash
# Safe testing with comprehensive logging
zoom-deep-clean-enhanced --dry-run --verbose --vm-aware

# Test without VM features
zoom-deep-clean-enhanced --dry-run --no-vm --verbose
```

### Automated Deployment
```bash
#!/bin/bash
# Automated cleanup script
cd /path/to/zoom-deep-clean-enhanced
pip3 install -e .
zoom-deep-clean-enhanced --force --vm-aware --system-reboot --log-file /var/log/zoom_cleanup.log
```

## Output Files and Reports

### Log Files
- **Installation Log**: `~/Documents/zoom_deep_clean_enhanced_install.log`
- **Dry-run Log**: `~/Documents/zoom_clean_enhanced_dry_run.log`  
- **Main Log**: `~/Documents/zoom_deep_clean_enhanced.log`

### Report Files
- **JSON Report**: `~/Documents/zoom_cleanup_enhanced_report.json`
- **Backup Location**: `~/Documents/zoom_deep_clean_backup/`

### Understanding the JSON Report
```json
{
  "timestamp": "2025-08-02T09:00:00",
  "version": "2.2.0-vm-aware-system-wide",
  "statistics": {
    "files_removed": 45,
    "directories_removed": 12,
    "processes_killed": 8,
    "vm_services_stopped": 3,
    "remaining_files_found": 0
  }
}
```

## Best Practices

### Before Running
1. **Close all applications** including VMs
2. **Save your work** in all applications
3. **Run dry-run first** to preview changes
4. **Ensure sudo access** is available
5. **Check disk space** for backups

### During Execution
1. **Don't interrupt** the process
2. **Monitor logs** for any errors
3. **Let VM services stop** completely
4. **Wait for comprehensive search** to complete

### After Completion
1. **Review all log files** for errors
2. **Check the JSON report** for statistics
3. **Verify no Zoom processes** are running
4. **Restart the system** as recommended
5. **Restart VMs** after system reboot
6. **Install fresh Zoom** from official source

## Security Considerations

### What the Script Does
- **Validates all paths** to prevent directory traversal
- **Sanitizes command arguments** to prevent injection
- **Verifies Zoom files** before removal
- **Creates backups** of all removed files
- **Logs all operations** for audit trail

### What You Should Do
- **Review dry-run output** before actual execution
- **Keep backup files** until you verify Zoom works correctly
- **Monitor system behavior** after cleanup
- **Use official Zoom installer** for reinstallation

## Integration with Your Bash Script

Your original bash script has been fully integrated into the enhanced version:

```bash
# Your original workflow is now:
zoom-deep-clean-enhanced --force --vm-aware --system-reboot --verbose

# Which automatically:
# 1. Stops all VMs and Zoom processes
# 2. Runs comprehensive cleanup
# 3. Verifies remaining files  
# 4. Reboots system
```

The enhanced version provides all the functionality of your bash script plus:
- Enhanced error handling and logging
- Security validation and backup
- Comprehensive file system search
- Detailed reporting and statistics
- VM-aware process management
- Cross-platform VM support

## Support and Troubleshooting

If you encounter issues:

1. **Check the log files** for detailed error messages
2. **Run with --verbose** for maximum detail
3. **Try --dry-run** to identify problems without making changes
4. **Disable VM features** with --no-vm if VM software causes issues
5. **Use manual VM shutdown** before running the script

The enhanced version addresses all your original concerns about VMs and parallel execution while providing a comprehensive, secure, and reliable cleanup solution.
