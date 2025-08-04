#!/usr/bin/env python3
"""
Comprehensive Zoom Clean - Complete removal and fresh installation
Demonstrates the full workflow of the enhanced deep cleaning system
"""

import sys
import os
import argparse
import logging

# Add the package to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from zoom_deep_clean import ComprehensiveZoomCLI


def main():
    """Main entry point for comprehensive Zoom cleaning"""

    print("🚀 Zoom Deep Clean Enhanced - Comprehensive Edition")
    print("=" * 60)
    print("Complete Zoom removal with deep system cleaning and fresh installation")
    print()

    parser = argparse.ArgumentParser(
        description="Comprehensive Zoom Deep Clean - Complete workflow",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
COMPREHENSIVE WORKFLOW:
  1. Standard Zoom application removal
  2. Deep system artifact cleaning (TCC, IORegistry, etc.)
  3. Optional system restart
  4. Fresh Zoom download and installation
  5. Comprehensive reporting

EXAMPLES:
  # Complete clean and reinstall (RECOMMENDED)
  python3 comprehensive_zoom_clean.py --force --install-fresh
  
  # Deep clean with system restart
  python3 comprehensive_zoom_clean.py --force --system-reboot
  
  # Preview what would be cleaned
  python3 comprehensive_zoom_clean.py --dry-run --verbose
  
  # Clean and continue on errors
  python3 comprehensive_zoom_clean.py --force --continue-on-error

WHAT THIS FIXES:
  ✅ "Login works but can't join meetings" issue
  ✅ TCC database permission conflicts
  ✅ IORegistry system integration problems
  ✅ Stale system temp files and caches
  ✅ Corrupted keychain entries
  ✅ Network configuration issues
        """,
    )

    # Core options
    parser.add_argument(
        "--force",
        action="store_true",
        help="Execute cleanup (required for actual cleaning)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would be cleaned without making changes",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose output"
    )

    # Advanced options
    parser.add_argument(
        "--install-fresh",
        action="store_true",
        help="Download and install fresh Zoom after cleaning",
    )
    parser.add_argument(
        "--system-reboot",
        action="store_true",
        help="Automatically restart system after cleaning",
    )
    parser.add_argument(
        "--continue-on-error",
        action="store_true",
        help="Continue with next phase even if current phase fails",
    )

    args = parser.parse_args()

    # Validate arguments
    if not args.force and not args.dry_run:
        print("❌ Error: Must specify either --force or --dry-run")
        print("Use --help for more information")
        sys.exit(1)

    if args.force and args.dry_run:
        print("❌ Error: Cannot use both --force and --dry-run")
        sys.exit(1)

    # Show warning for actual cleanup
    if args.force:
        print("⚠️  WARNING: This will perform comprehensive system cleaning")
        print("   - Remove all Zoom files and configurations")
        print("   - Clear TCC database permissions")
        print("   - Clean system registries and caches")
        if args.install_fresh:
            print("   - Download and install fresh Zoom")
        if args.system_reboot:
            print("   - Restart your system")
        print()

        response = input("Continue? (y/N): ").strip().lower()
        if response not in ["y", "yes"]:
            print("❌ Operation cancelled")
            sys.exit(0)
        print()

    # Set comprehensive mode
    args.comprehensive = True

    # Run comprehensive cleaning
    try:
        cli = ComprehensiveZoomCLI()
        success = cli.run_comprehensive_clean(args)

        if success:
            print("\n🎉 COMPREHENSIVE CLEAN COMPLETED SUCCESSFULLY!")
            print("=" * 60)

            if args.dry_run:
                print("📋 This was a preview run. Use --force to execute.")
            else:
                print("✅ All phases completed successfully")

                if args.install_fresh:
                    print("📦 Fresh Zoom has been installed")
                    print("🎯 You can now launch Zoom and test meeting functionality")
                else:
                    print("📦 Install Zoom from: https://zoom.us/download")

                if not args.system_reboot:
                    print("🔄 Restart your system for full effect")
        else:
            print("\n❌ COMPREHENSIVE CLEAN COMPLETED WITH ERRORS")
            print("📄 Check the log files for details")

        sys.exit(0 if success else 1)

    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
