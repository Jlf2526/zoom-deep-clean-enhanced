"""
Zoom Deep Clean Enhanced - VM-Aware & System-Wide cleanup utility

Created by: PHLthy215
Enhanced Version: 2.2.0 - VM-Aware & System-Wide

This package provides comprehensive Zoom cleanup functionality with:
- VM-aware process detection and termination
- System-wide file search and removal
- Enhanced security features
- Comprehensive backup functionality
- Automatic system reboot option
"""

from .cleaner_enhanced import ZoomDeepCleanerEnhanced, SecurityError

__version__ = "2.2.0"
__author__ = "PHLthy215"
__email__ = "phlthy215@example.com"
__description__ = "Enhanced VM-Aware & System-Wide Zoom cleanup utility for macOS"

__all__ = [
    "ZoomDeepCleanerEnhanced",
    "SecurityError",
    "__version__",
    "__author__",
    "__email__",
    "__description__",
]


# CLI main function available via lazy import to avoid warnings
def main():
    """Entry point for CLI - lazy import to avoid module loading issues"""
    from .cli_enhanced import main as cli_main

    return cli_main()
