# Troubleshooting Guide

## Common Issues

### Permission Errors

**Problem**: "Permission denied" when accessing system files
```bash
# Solution: Run with sudo
sudo zoom-deep-clean-enhanced --force
```

**Problem**: Can't modify certain system directories
```bash
# Solution: Disable SIP temporarily (advanced users only)
# Boot into Recovery Mode, open Terminal:
csrutil disable
# Reboot and run cleanup, then re-enable:
csrutil enable
```

### VM-Related Issues

**Problem**: VMs won't stop during cleanup
```bash
# Manual VM shutdown:
# VMware Fusion
sudo launchctl stop com.vmware.fusion

# VirtualBox
sudo launchctl stop org.virtualbox.app.VBoxSVC

# Parallels Desktop
sudo launchctl stop com.parallels.desktop.launchdaemon
```

**Problem**: VM processes keep restarting
```bash
# Disable VM auto-start then run cleanup
zoom-deep-clean-enhanced --no-vm --force
```

### Performance Issues

**Problem**: Cleanup takes too long
```bash
# Skip comprehensive search
zoom-deep-clean-enhanced --force --no-comprehensive-search
```

**Problem**: System becomes unresponsive
```bash
# Use verbose mode to monitor progress
zoom-deep-clean-enhanced --dry-run --verbose
```

### File System Issues

**Problem**: "File not found" errors in log
- **Solution**: Normal - files may have been removed by previous runs

**Problem**: Some files remain after cleanup
```bash
# Run post-cleanup verification
find /Applications -name "*oom*" -type f 2>/dev/null
find ~/Library -name "*oom*" -type f 2>/dev/null
```

### Installation Issues

**Problem**: `zoom-deep-clean-enhanced` command not found
```bash
# Check installation
pip show zoom-deep-clean-enhanced

# Reinstall if needed
pip install --force-reinstall zoom-deep-clean-enhanced
```

**Problem**: Python version compatibility
```bash
# Check Python version (requires 3.9+)
python3 --version

# Install with specific Python version
python3.9 -m pip install zoom-deep-clean-enhanced
```

## Error Codes

| Code | Meaning | Solution |
|------|---------|----------|
| 0 | Success | No action needed |
| 1 | General error | Check log file for details |
| 2 | Security error | Review permissions and security settings |
| 130 | User cancelled | Operation cancelled by user (Ctrl+C) |

## Getting Help

1. **Check the log file**: `~/Documents/zoom_deep_clean_enhanced.log`
2. **Run with verbose output**: `--verbose` flag
3. **Try dry-run mode**: `--dry-run` to see what would happen
4. **Check system requirements**: macOS 12.x+, Python 3.9+

## Log File Analysis

```bash
# View recent errors
tail -n 50 ~/Documents/zoom_deep_clean_enhanced.log | grep ERROR

# Check for permission issues
grep -i "permission" ~/Documents/zoom_deep_clean_enhanced.log

# See VM-related operations
grep -i "vm\|virtualbox\|vmware\|parallels" ~/Documents/zoom_deep_clean_enhanced.log
```

## Reset Instructions

If cleanup fails or causes issues:

```bash
# Restore from backup (if created)
# Backup location: ~/Documents/zoom_backup_[timestamp]/

# Reinstall Zoom normally
# Download from: https://zoom.us/download

# Clear any partial state
rm -f ~/Documents/zoom_deep_clean_enhanced.log
rm -f ~/Documents/zoom_cleanup_enhanced_report.json
```