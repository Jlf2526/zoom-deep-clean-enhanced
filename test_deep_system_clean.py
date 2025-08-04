#!/usr/bin/env python3
"""
Test script for the enhanced deep system cleaner
Demonstrates the capabilities for addressing "login works but can't join meetings" issue
"""

import sys
import os
import logging
from pathlib import Path

# Add the project directory to Python path
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))

from zoom_deep_clean.cleaner_enhanced import ZoomDeepCleanerEnhanced


def main():
    """Test the enhanced deep system cleaner"""
    print("🔍 Zoom Deep Clean Enhanced - Deep System Artifact Test")
    print("=" * 60)
    print()
    print("This test demonstrates the enhanced deep system cleaning capabilities")
    print("that address the 'login works but can't join meetings' issue.")
    print()

    # Ask user for test mode
    print("Choose test mode:")
    print("1. Dry run (safe preview - recommended)")
    print("2. Full cleanup (requires sudo)")
    print()

    choice = input("Enter choice (1 or 2): ").strip()

    if choice == "1":
        dry_run = True
        print("🔍 Running in DRY RUN mode (safe preview)")
    elif choice == "2":
        dry_run = False
        print("⚠️  Running in FULL CLEANUP mode")
        confirm = (
            input("Are you sure? This will make system changes (y/N): ").strip().lower()
        )
        if confirm != "y":
            print("Cancelled.")
            return
    else:
        print("Invalid choice. Exiting.")
        return

    print()
    print("=" * 60)

    try:
        # Initialize the enhanced cleaner
        cleaner = ZoomDeepCleanerEnhanced(
            verbose=True,
            dry_run=dry_run,
            enable_backup=True,
            vm_aware=True,
            enable_advanced_features=True,
        )

        # Run the deep clean
        success = cleaner.run_deep_clean()

        print()
        print("=" * 60)
        if success:
            print("✅ Deep system cleanup completed successfully!")
            print()
            print("Key improvements for 'login works but can't join meetings' issue:")
            print(
                "• IORegistry entries cleared (removes system-level Zoom integration)"
            )
            print("• System temp files cleaned (removes cached connection data)")
            print("• Network configurations reset (clears DNS and connection caches)")
            print("• Audio/video configs reset (removes device binding issues)")
            print("• System identifiers cleared (removes device fingerprinting)")
            print("• Package receipts removed (prevents reinstallation conflicts)")
            print("• Deep system caches cleared (removes kernel-level caches)")
            print("• Kernel extensions cleared (removes low-level system hooks)")
            print()
            print("📄 Check the detailed report at:")
            print(f"   ~/Documents/zoom_cleanup_enhanced_report.json")
            print()
            print("📋 Check the log file at:")
            print(f"   ~/Documents/zoom_deep_clean_enhanced.log")
        else:
            print("❌ Deep system cleanup encountered issues.")
            print("Check the log file for details.")

    except Exception as e:
        print(f"❌ Error during cleanup: {e}")
        return False

    print()
    print("=" * 60)
    print("🔧 Next Steps:")
    print("1. Restart your Mac to ensure all changes take effect")
    print("2. Reinstall Zoom from scratch")
    print("3. Test meeting join functionality")
    print()
    print("If you still experience issues, the detailed report contains")
    print("information about any remaining artifacts that may need manual removal.")


if __name__ == "__main__":
    main()
