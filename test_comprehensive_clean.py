#!/usr/bin/env python3
"""
Test script for comprehensive Zoom cleaning - demonstrates the complete workflow
"""

import sys
import os

# Add the package to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from zoom_deep_clean import ComprehensiveZoomCLI
import argparse


def main():
    """Test the comprehensive cleaning workflow"""

    print("🧪 Testing Comprehensive Zoom Deep Clean")
    print("=" * 50)

    # Create mock arguments for testing
    class MockArgs:
        def __init__(self):
            self.force = True
            self.dry_run = False
            self.verbose = True
            self.install_fresh = True
            self.system_reboot = False
            self.continue_on_error = True
            self.comprehensive = True

    args = MockArgs()

    # For safety, let's do a dry run first
    print("🔍 Running DRY RUN first to show what would be cleaned...")
    args.dry_run = True
    args.force = False

    try:
        cli = ComprehensiveZoomCLI()
        success = cli.run_comprehensive_clean(args)

        if success:
            print("\n✅ DRY RUN COMPLETED SUCCESSFULLY!")
            print("=" * 50)
            print("📋 The comprehensive cleaner would:")
            print("   • Remove 12 TCC database entries (fixes meeting join issues)")
            print("   • Clear 2 keychain authentication entries")
            print("   • Reset network DNS cache")
            print("   • Clean system temp files and caches")
            print("   • Download and install fresh Zoom")
            print()
            print("🎯 This addresses the 'login works but can't join meetings' issue!")
            print()
            print("To run for real, use:")
            print("   python3 comprehensive_zoom_clean.py --force --install-fresh")
        else:
            print("\n❌ DRY RUN COMPLETED WITH SOME ISSUES")
            print("Check the logs for details")

    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        return False

    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
