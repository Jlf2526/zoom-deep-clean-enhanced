#!/usr/bin/env python3
"""
Run Enhanced Zoom Deep Clean with Deep System Cleaning
Addresses the "login works but can't join meetings" issue
"""

import sys
import os
import subprocess
from pathlib import Path

# Add the project directory to Python path
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))

from zoom_deep_clean.cleaner_enhanced import ZoomDeepCleanerEnhanced


def check_sudo_access():
    """Check if we have sudo access"""
    try:
        result = subprocess.run(["sudo", "-n", "true"], capture_output=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False


def main():
    """Run the enhanced deep system cleaner"""
    print("🔍 Zoom Deep Clean Enhanced - Deep System Cleaning")
    print("=" * 60)
    print()
    print("This version includes enhanced deep system cleaning that addresses")
    print("the 'login works but can't join meetings' issue by cleaning:")
    print("• IORegistry system integration entries")
    print("• System temporary files with Zoom signatures")
    print("• Network configuration caches")
    print("• Audio/video system integration artifacts")
    print("• System identifiers and device fingerprints")
    print("• Package receipt conflicts")
    print("• Kernel-level caches and extensions")
    print()

    # Check sudo access
    has_sudo = check_sudo_access()
    if not has_sudo:
        print("⚠️  SUDO ACCESS REQUIRED")
        print("Deep system cleaning requires administrator privileges.")
        print("Please run: sudo python3 run_deep_system_clean.py")
        print()
        choice = (
            input("Continue anyway? (some features will be limited) [y/N]: ")
            .strip()
            .lower()
        )
        if choice != "y":
            print("Exiting. Please run with sudo for full functionality.")
            return False
        print()

    # Ask user for mode
    print("Choose cleaning mode:")
    print("1. Dry run (safe preview - see what would be cleaned)")
    print("2. Full deep system cleanup (requires sudo)")
    print()

    choice = input("Enter choice (1 or 2): ").strip()

    if choice == "1":
        dry_run = True
        print("🔍 Running in DRY RUN mode (safe preview)")
    elif choice == "2":
        dry_run = False
        print("⚠️  Running FULL DEEP SYSTEM CLEANUP")
        print()
        print("This will:")
        print("• Kill all Zoom processes")
        print("• Remove all Zoom files and configurations")
        print("• Clear deep system-level artifacts")
        print("• Reset network and audio/video configurations")
        print("• Clear IORegistry entries")
        print("• Remove system identifiers")
        print()
        confirm = (
            input("Are you sure? This will make extensive system changes (y/N): ")
            .strip()
            .lower()
        )
        if confirm != "y":
            print("Cancelled.")
            return False
    else:
        print("Invalid choice. Exiting.")
        return False

    print()
    print("=" * 60)
    print("🚀 Starting Enhanced Deep System Cleanup...")
    print()

    try:
        # Initialize the enhanced cleaner with deep system cleaning
        cleaner = ZoomDeepCleanerEnhanced(
            verbose=True,
            dry_run=dry_run,
            enable_backup=True,
            vm_aware=True,
            system_reboot=False,  # We'll ask about reboot separately
            enable_advanced_features=True,
            enable_mac_spoofing=False,
            reset_hostname=False,
        )

        # Run the deep clean
        success = cleaner.run_deep_clean()

        print()
        print("=" * 60)
        if success:
            print("✅ Enhanced deep system cleanup completed successfully!")
            print()
            print("🔍 Deep System Cleanup Results:")
            print("Check the log file for detailed information about:")
            print("• IORegistry entries cleared")
            print("• System temp files cleaned")
            print("• Network configurations reset")
            print("• Audio/video configs reset")
            print("• System identifiers cleared")
            print("• Package receipts removed")
            print("• Deep caches cleared")
            print("• Kernel extensions cleared")
            print()
            print("📄 Detailed reports saved to:")
            print(f"   Log: ~/Documents/zoom_deep_clean_enhanced.log")
            print(f"   Report: ~/Documents/zoom_cleanup_enhanced_report.json")

            if not dry_run:
                print()
                print("🔄 IMPORTANT: System Reboot Recommended")
                print("For complete cleanup effectiveness, especially for deep system")
                print("artifacts, a system reboot is highly recommended.")
                print()
                reboot_choice = input("Reboot now? (y/N): ").strip().lower()
                if reboot_choice == "y":
                    print("🔄 Rebooting system...")
                    subprocess.run(["sudo", "shutdown", "-r", "now"])
                else:
                    print("⚠️  Please reboot manually when convenient.")
                    print(
                        "   Some deep system changes may not take effect until reboot."
                    )
        else:
            print("❌ Deep system cleanup encountered issues.")
            print("Check the log file for details:")
            print("   ~/Documents/zoom_deep_clean_enhanced.log")

    except Exception as e:
        print(f"❌ Error during cleanup: {e}")
        print("Check the log file for detailed error information.")
        return False

    print()
    print("=" * 60)
    print("🔧 Next Steps After Reboot:")
    print("1. Download fresh Zoom installer from zoom.us")
    print("2. Install Zoom as if on a new device")
    print("3. Test both login AND meeting join functionality")
    print("4. The 'login works but can't join meetings' issue should be resolved")
    print()
    print("If you still experience issues, check the detailed report for")
    print("any remaining artifacts that may need manual attention.")

    return True


if __name__ == "__main__":
    main()
