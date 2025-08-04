#!/usr/bin/env python3
"""
Enhanced CLI for Zoom Deep Clean with comprehensive system cleaning
"""

import argparse
import sys
import logging
import os
from pathlib import Path

# Handle both direct execution and package import
try:
    # Try relative import first (when run as package)
    from .cleaner_enhanced import ZoomDeepCleanerEnhanced
    from .comprehensive_cli import ComprehensiveZoomCLI
    from .auth_fix_cli import main as auth_fix_main
except ImportError:
    # Fall back to absolute import (when run directly)
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from zoom_deep_clean.cleaner_enhanced import ZoomDeepCleanerEnhanced
    from zoom_deep_clean.comprehensive_cli import ComprehensiveZoomCLI
    from zoom_deep_clean.auth_fix_cli import main as auth_fix_main


def setup_logging(verbose: bool = False) -> logging.Logger:
    """Setup logging configuration"""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")
    return logging.getLogger(__name__)


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Zoom Deep Clean Enhanced - Complete Zoom removal tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Standard deep clean
  %(prog)s --force
  
  # ZoomFixer-enhanced clean with secure shredding and network reset
  %(prog)s --force --zoomfixer-mode
  
  # Comprehensive clean with fresh install
  %(prog)s --comprehensive --install-fresh
  
  # Preview what would be cleaned (including ZoomFixer techniques)
  %(prog)s --dry-run --verbose --zoomfixer-mode
  
  # Network reset and hostname randomization only
  %(prog)s --force --network-reset --randomize-hostname
  
  # Deep system clean with reboot
  %(prog)s --comprehensive --system-reboot
        """,
    )

    # Core cleaning options
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

    # Comprehensive cleaning mode
    parser.add_argument(
        "--comprehensive",
        action="store_true",
        help="Run comprehensive clean including deep system artifacts",
    )
    parser.add_argument(
        "--install-fresh",
        action="store_true",
        help="Download and install fresh Zoom after cleaning (requires --comprehensive)",
    )
    parser.add_argument(
        "--system-reboot",
        action="store_true",
        help="Automatically restart system after cleaning (requires --comprehensive)",
    )
    parser.add_argument(
        "--continue-on-error",
        action="store_true",
        help="Continue with next phase even if current phase fails",
    )

    # ZoomFixer-inspired options
    parser.add_argument(
        "--zoomfixer-mode",
        action="store_true",
        help="Enable ZoomFixer-inspired techniques (secure shredding, network reset, hostname randomization)",
    )
    parser.add_argument(
        "--network-reset",
        action="store_true",
        help="Reset Wi-Fi interface as part of device fingerprint cleaning",
    )
    parser.add_argument(
        "--randomize-hostname",
        action="store_true",
        help="Randomize system hostname for complete device identity reset",
    )

    # Legacy options for compatibility
    parser.add_argument(
        "--vm-aware",
        action="store_true",
        help="Enable VM-aware cleaning (default: enabled)",
    )
    parser.add_argument(
        "--backup",
        action="store_true",
        help="Create backups before removal (default: enabled)",
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

    # Validate comprehensive mode requirements
    if (args.install_fresh or args.system_reboot) and not args.comprehensive:
        print("❌ Error: --install-fresh and --system-reboot require --comprehensive")
        sys.exit(1)

    # Setup logging
    logger = setup_logging(args.verbose)

    try:
        if args.comprehensive:
            # Run comprehensive cleaning
            logger.info("🚀 Starting Comprehensive Zoom Deep Clean")
            cli = ComprehensiveZoomCLI()
            success = cli.run_comprehensive_clean(args)
        else:
            # Run standard cleaning
            if args.zoomfixer_mode:
                logger.info("🎯 Starting ZoomFixer-Enhanced Deep Clean")
            else:
                logger.info("🚀 Starting Standard Zoom Deep Clean")

            # Configure ZoomFixer options
            enable_network_reset = args.zoomfixer_mode or args.network_reset
            enable_hostname_randomization = (
                args.zoomfixer_mode or args.randomize_hostname
            )

            cleaner = ZoomDeepCleanerEnhanced(
                verbose=args.verbose,
                dry_run=args.dry_run,
                enable_advanced_features=True,
                reset_hostname=enable_hostname_randomization,
            )
            success = cleaner.run_deep_clean()

        if success:
            logger.info("✅ Zoom Deep Clean completed successfully")
            if not args.dry_run:
                logger.info("💡 Recommendation: Restart your system and reinstall Zoom")
        else:
            logger.error("❌ Zoom Deep Clean completed with errors")
            logger.info("📄 Check the log file for details")

        sys.exit(0 if success else 1)

    except KeyboardInterrupt:
        logger.error("❌ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")
        if args.verbose:
            import traceback

            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
