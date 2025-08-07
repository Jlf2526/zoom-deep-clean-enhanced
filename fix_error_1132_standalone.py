#!/usr/bin/env python3
"""
Standalone Error 1132 Fixer for Zoom

This script provides a standalone solution for diagnosing and fixing Zoom Error 1132,
which typically indicates network or firewall issues preventing connection to Zoom servers.

Usage:
    python3 fix_error_1132_standalone.py [--dry-run] [--verbose]

Examples:
    # Diagnose and fix Error 1132
    python3 fix_error_1132_standalone.py

    # Preview what would be done without making changes
    python3 fix_error_1132_standalone.py --dry-run --verbose
"""

import argparse
import logging
import sys
import os

# Add the package to path so we can import our modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from zoom_deep_clean.error_1132_handler import Error1132Handler


def setup_logging(verbose: bool = False):
    """Setup logging for the application"""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(asctime)s - %(levelname)s - %(message)s")
    return logging.getLogger("error_1132_fixer")


def main():
    """Main entry point for the Error 1132 fixer"""
    print("🔧 Zoom Error 1132 Fixer")
    print("=" * 50)
    print("Diagnose and fix Zoom Error 1132 (network/firewall issues)")
    print()

    parser = argparse.ArgumentParser(
        description="Standalone Error 1132 Fixer for Zoom",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
DESCRIPTION:
This tool specifically addresses Zoom Error 1132, which typically indicates
network or firewall issues preventing connection to Zoom servers.

The tool will:
1. Diagnose connectivity issues to Zoom servers
2. Check firewall rules that might block Zoom
3. Analyze proxy settings
4. Examine Zoom logs for Error 1132 references
5. Run advanced network diagnostics
6. Apply targeted fixes for identified issues

EXAMPLES:
  # Diagnose and fix Error 1132
  python3 fix_error_1132_standalone.py
  
  # Preview what would be done without making changes
  python3 fix_error_1132_standalone.py --dry-run --verbose
        """,
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would be done without making changes",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose output"
    )

    args = parser.parse_args()

    # Setup logging
    logger = setup_logging(args.verbose)

    # Show warning for actual fixes
    if not args.dry_run:
        print("⚠️  WARNING: This will modify system network and firewall settings")
        print("   - Flush DNS cache")
        print("   - Reset firewall rules")
        print("   - Reset network interfaces")
        print("   - Apply advanced network fixes")
        print()

        response = input("Continue? (y/N): ").strip().lower()
        if response not in ["y", "yes"]:
            print("❌ Operation cancelled")
            sys.exit(0)
        print()

    try:
        # Create Error 1132 handler
        handler = Error1132Handler(logger, args.dry_run)

        # Run diagnostic
        print("🔍 Running Error 1132 Diagnostic...")
        diagnostic_results = handler.diagnose_error_1132()

        # Generate and print report
        print("\n" + "=" * 50)
        print("📋 ERROR 1132 DIAGNOSTIC REPORT")
        print("=" * 50)
        report = handler.generate_error_1132_report(diagnostic_results)
        print(report)

        # Apply fixes if not in dry-run mode
        if not args.dry_run:
            print("\n" + "=" * 50)
            print("🔧 APPLYING ERROR 1132 FIXES")
            print("=" * 50)

            if handler.fix_error_1132():
                print("✅ Error 1132 fixes applied successfully")
                print("\n💡 NEXT STEPS:")
                print("1. Restart your network router/modem")
                print("2. Try connecting to a Zoom meeting")
                print("3. If issues persist, contact your network administrator")
            else:
                print("❌ Some Error 1132 fixes failed to apply")
                print("📄 Check the log above for details")
        else:
            print("\n💡 In --dry-run mode, no actual changes were made to your system")
            print("💡 To apply these fixes, run without --dry-run flag")

        sys.exit(0)

    except KeyboardInterrupt:
        print("\n❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
