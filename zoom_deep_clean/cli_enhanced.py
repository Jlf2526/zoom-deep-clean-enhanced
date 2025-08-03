#!/usr/bin/env python3
"""
Zoom Deep Clean - Enhanced Command Line Interface (VM-Aware & System-Wide)

Created by: PHLthy215
Enhanced Version: 2.2.0 - VM-Aware & System-Wide
"""

import sys
import argparse

# Handle both direct execution and package import
try:
    # Try relative import first (when run as package)
    from .cleaner_enhanced import (
        ZoomDeepCleanerEnhanced,
        DEFAULT_LOG_FILE,
        SecurityError,
    )
except ImportError:
    # Fall back to absolute import (when run directly)
    import os

    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from zoom_deep_clean.cleaner_enhanced import (
        ZoomDeepCleanerEnhanced,
        DEFAULT_LOG_FILE,
        SecurityError,
    )


def main() -> None:
    """Enhanced main entry point with VM-aware options and system-wide cleanup"""
    parser = argparse.ArgumentParser(
        description="Zoom Deep Clean Enhanced - VM-Aware & System-Wide Device Fingerprint Removal",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Enhanced Security Features:
  • VM-aware process detection and termination
  • Comprehensive system-wide file search
  • Enhanced command injection prevention
  • Path validation and sanitization
  • Zoom file verification with extended patterns
  • Automatic backup functionality
  • Comprehensive audit logging
  • Optional automatic system reboot

VM Support:
  • VMware Fusion detection and management
  • VirtualBox process handling
  • Parallels Desktop integration
  • Shared resource cleanup

Examples:
  %(prog)s                           # Run with default settings
  %(prog)s --dry-run                 # Preview what would be removed
  %(prog)s --verbose --vm-aware      # Enable detailed logging with VM support
  %(prog)s --system-reboot           # Automatically reboot after cleanup
  %(prog)s --no-vm --no-backup       # Disable VM awareness and backup
  %(prog)s --comprehensive-search    # Perform thorough file system search
        """,
    )

    parser.add_argument(
        "--version",
        action="version",
        version="Zoom Deep Clean Enhanced v2.2.0 (VM-Aware & System-Wide) by PHLthy215",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview operations without making changes",
    )

    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose logging"
    )

    parser.add_argument(
        "--log-file",
        default=DEFAULT_LOG_FILE,
        help=f"Log file path (default: {DEFAULT_LOG_FILE})",
    )

    parser.add_argument(
        "--force", "-f", action="store_true", help="Skip confirmation prompts"
    )

    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Disable automatic backup functionality",
    )

    parser.add_argument(
        "--vm-aware",
        action="store_true",
        default=True,
        help="Enable VM-aware cleanup (default: enabled)",
    )

    parser.add_argument("--no-vm", action="store_true", help="Disable VM-aware cleanup")

    parser.add_argument(
        "--system-reboot",
        action="store_true",
        help="Automatically reboot system after cleanup",
    )

    parser.add_argument(
        "--comprehensive-search",
        action="store_true",
        default=True,
        help="Perform comprehensive file system search (default: enabled)",
    )

    # Advanced Features Group
    advanced_group = parser.add_argument_group(
        "Advanced Features", "Advanced fingerprint detection and modification"
    )

    advanced_group.add_argument(
        "--enable-advanced-features",
        action="store_true",
        default=True,
        help="Enable advanced fingerprint features (default: enabled)",
    )

    advanced_group.add_argument(
        "--disable-advanced-features",
        action="store_true",
        help="Disable all advanced features",
    )

    advanced_group.add_argument(
        "--enable-mac-spoofing",
        action="store_true",
        help="Enable MAC address spoofing (VM environments only - use with caution)",
    )

    advanced_group.add_argument(
        "--reset-hostname",
        action="store_true",
        help="Reset system hostname to random value",
    )

    advanced_group.add_argument(
        "--new-hostname",
        type=str,
        help="Specify custom hostname (requires --reset-hostname)",
    )

    try:
        args = parser.parse_args()
    except SystemExit:
        # Handle --help and --version gracefully
        raise

    # Handle VM awareness flags
    vm_aware = args.vm_aware and not args.no_vm

    # Handle advanced features flags
    enable_advanced = (
        args.enable_advanced_features and not args.disable_advanced_features
    )

    # Validate hostname arguments
    if args.new_hostname and not args.reset_hostname:
        print("Error: --new-hostname requires --reset-hostname")
        sys.exit(1)

    # Show enhanced warning and get confirmation
    if not args.force and not args.dry_run:
        print("🔒 ZOOM DEEP CLEAN ENHANCED - VM-Aware & System-Wide v2.2.0")
        print("=" * 70)
        print(
            "⚠️  WARNING: This will completely remove ALL Zoom data and system integration"
        )
        print(
            "   • All keychain entries, launch agents, and system drivers will be removed"
        )
        print("   • VM services will be stopped to ensure complete cleanup")
        print("   • Comprehensive system-wide search will be performed")
        print("   • You will need to reinstall Zoom completely after this operation")
        print("   • Your current Zoom installation will be unusable")
        print("   • This operation requires sudo privileges for system-level cleanup")
        print()
        print("🛡️  Enhanced Security Features:")
        print("   • VM-aware process detection and termination")
        print("   • Comprehensive system-wide file search")
        print("   • Enhanced command injection prevention")
        print("   • Path validation and sanitization")
        print("   • Zoom file verification with extended patterns")
        if not args.no_backup:
            print("   • Automatic backup functionality")
        print("   • Comprehensive audit logging")
        if args.system_reboot:
            print("   • Automatic system reboot after cleanup")
        print()

        if enable_advanced:
            print("🚀 Advanced Fingerprint Features:")
            print("   • Comprehensive keychain scanning")
            print("   • MDM profile detection")
            print("   • System UUID and identifier detection")
            if args.reset_hostname:
                hostname_text = (
                    f" (to: {args.new_hostname})" if args.new_hostname else " (random)"
                )
                print(f"   • Hostname reset{hostname_text}")
            if args.enable_mac_spoofing:
                print("   • MAC address spoofing (VM environments)")
            print()
        print("🖥️  VM Support:")
        if vm_aware:
            print("   • VMware Fusion detection and management")
            print("   • VirtualBox process handling")
            print("   • Parallels Desktop integration")
            print("   • Shared resource cleanup")
        else:
            print("   • VM awareness disabled")
        print()

        response = (
            input(
                "Do you want to continue with enhanced cleanup including advanced features? (yes/no): "
            )
            .lower()
            .strip()
        )
        if response not in ["yes", "y"]:
            print("Operation cancelled.")
            sys.exit(0)

    # Initialize and run enhanced cleaner with security validation
    try:
        cleaner = ZoomDeepCleanerEnhanced(
            log_file=args.log_file,
            verbose=args.verbose,
            dry_run=args.dry_run,
            enable_backup=not args.no_backup,
            vm_aware=vm_aware,
            system_reboot=args.system_reboot,
            enable_advanced_features=enable_advanced,
            enable_mac_spoofing=args.enable_mac_spoofing,
            reset_hostname=args.reset_hostname,
            new_hostname=args.new_hostname,
        )

        success = cleaner.run_deep_clean()

        if success:
            print(
                f"\n✅ Enhanced deep clean completed successfully! Check {args.log_file} for details."
            )
            if args.system_reboot and not args.dry_run:
                print("🔄 System reboot initiated...")
            sys.exit(0)
        else:
            # Check if operation was cancelled by user
            if cleaner.was_cancelled_by_user():
                print(f"\n⏹️  Enhanced deep clean was cancelled by user.")
                print(
                    f"✅ All operations completed before cancellation were successful."
                )
                print(f"📋 Check {args.log_file} for details of what was completed.")
                sys.exit(130)  # Standard exit code for user cancellation (Ctrl+C)
            else:
                print(
                    f"\n❌ Enhanced deep clean completed with errors or security violations."
                )
                print(f"Check {args.log_file} for details.")
                sys.exit(1)

    except SecurityError as e:
        print(f"\n🚨 Security Error: {e}")
        print("Operation aborted for security reasons.")
        sys.exit(2)
    except KeyboardInterrupt:
        print("\n⚠️  Operation cancelled by user.")
        sys.exit(130)
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        print("Please check the log file for more details.")
        sys.exit(1)


if __name__ == "__main__":
    main()
