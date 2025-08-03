# Quick Start Guide

## Installation

```bash
# Install from PyPI
pip install zoom-deep-clean-enhanced

# Or install from source
git clone https://github.com/PHLthy215/zoom-deep-clean-enhanced.git
cd zoom-deep-clean-enhanced
pip install -e .
```

## Basic Usage

```bash
# Preview what will be cleaned (safe)
zoom-deep-clean-enhanced --dry-run --verbose

# Run the cleanup
zoom-deep-clean-enhanced --force

# With VM awareness (default)
zoom-deep-clean-enhanced --vm-aware --force
```

## GUI Option

```bash
# Launch graphical interface
python3 -m zoom_deep_clean.gui_enhanced
```

## Important Notes

⚠️ **Always run `--dry-run` first** to preview changes

⚠️ **Requires sudo privileges** for system-level cleanup

⚠️ **Will stop VMs** during cleanup process

⚠️ **Complete Zoom removal** - reinstallation required

## Quick Commands

| Command | Purpose |
|---------|---------|
| `zoom-deep-clean-enhanced --dry-run` | Preview cleanup |
| `zoom-deep-clean-enhanced --force` | Run cleanup |
| `zoom-deep-clean-enhanced --help` | Show all options |

## After Cleanup

1. System will optionally reboot (if `--system-reboot` used)
2. Reinstall Zoom from scratch
3. Device will appear as completely new to Zoom