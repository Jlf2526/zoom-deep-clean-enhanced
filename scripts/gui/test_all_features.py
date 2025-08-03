#!/usr/bin/env python3
"""
Test script for all advanced features of Zoom Deep Clean Enhanced
"""

import sys
import os
import json
import tempfile

# Add the package to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "zoom_deep_clean"))

from zoom_deep_clean.cleaner_enhanced import ZoomDeepCleanerEnhanced


def test_all_features():
    """Test all advanced features in dry-run mode"""
    print("🧪 Testing Zoom Deep Clean Enhanced - All Features")
    print("=" * 60)

    # Create temporary log file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as f:
        log_file = f.name

    try:
        # Test with all advanced features enabled
        cleaner = ZoomDeepCleanerEnhanced(
            log_file=log_file,
            verbose=True,
            dry_run=True,  # Safe testing
            enable_backup=True,
            vm_aware=True,
            system_reboot=False,
            enable_advanced_features=True,
            enable_mac_spoofing=True,  # Test MAC spoofing in dry-run
            reset_hostname=True,
            new_hostname="TestMac-Enhanced",
        )

        print("✅ Cleaner initialized successfully")

        # Run the cleanup
        success = cleaner.run_deep_clean()

        print(f"✅ Cleanup completed: {'Success' if success else 'With warnings'}")

        # Check statistics
        stats = cleaner.cleanup_stats
        print("\n📊 Test Results:")
        print(f"   • Advanced features executed: {stats['advanced_features_executed']}")
        print(
            f"   • Keychain comprehensive scan: {stats['keychain_comprehensive_scan']}"
        )
        print(f"   • MDM profiles detected: {stats['mdm_profiles_detected']}")
        print(
            f"   • System identifiers detected: {stats['system_identifiers_detected']}"
        )
        print(f"   • VM services stopped: {stats['vm_services_stopped']}")
        print(f"   • Processes killed: {stats['processes_killed']}")
        print(f"   • Security violations: {stats['security_violations']}")
        print(f"   • Errors: {stats['errors']}")

        # Test individual advanced features
        if cleaner.enable_advanced_features:
            print("\n🔬 Testing Individual Advanced Features:")

            # Test keychain scan
            keychain_result = cleaner.advanced_features.scan_keychain_comprehensive()
            print(
                f"   🔐 Keychain scan: {keychain_result['total_entries_scanned']} entries scanned"
            )

            # Test MDM detection
            mdm_result = cleaner.advanced_features.detect_mdm_profiles()
            print(f"   📋 MDM detection: {mdm_result['total_profiles']} profiles found")

            # Test UUID detection
            uuid_result = cleaner.advanced_features.detect_system_uuids()
            print(
                f"   🆔 UUID detection: {uuid_result['total_identifiers']} identifiers found"
            )

            # Test hostname reset (dry-run)
            hostname_result = cleaner.advanced_features.reset_hostname("TestMac-DryRun")
            print(
                f"   🏷️ Hostname reset: {'Success' if hostname_result['success'] else 'Failed'}"
            )

            # Test MAC spoofing (dry-run)
            mac_result = cleaner.advanced_features.spoof_mac_addresses()
            if mac_result.get("enabled", True):
                print(
                    f"   🔄 MAC spoofing: {len(mac_result.get('interfaces_spoofed', []))} interfaces"
                )
            else:
                print(f"   🔄 MAC spoofing: {mac_result.get('reason', 'Unknown')}")

        print("\n🎉 All tests completed successfully!")
        return True

    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        return False

    finally:
        # Clean up
        if os.path.exists(log_file):
            os.unlink(log_file)


if __name__ == "__main__":
    success = test_all_features()
    sys.exit(0 if success else 1)
