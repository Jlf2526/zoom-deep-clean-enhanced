#!/usr/bin/env python3
"""
Test script to verify PySide6 GUI parameter fix
"""

import sys
import os

# Add the package to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))


def test_cleaner_config():
    """Test that the cleaner can be initialized with the GUI config"""
    print("🧪 Testing ZoomDeepCleanerEnhanced initialization...")

    try:
        from zoom_deep_clean.cleaner_enhanced import ZoomDeepCleanerEnhanced

        # Test config that matches what the GUI sends
        test_config = {
            "dry_run": True,
            "verbose": True,
            "enable_backup": True,
            "enable_advanced_features": True,
            "vm_aware": True,
            "system_reboot": False,
        }

        print(f"📋 Test config: {test_config}")

        # Try to create cleaner instance
        cleaner = ZoomDeepCleanerEnhanced(**test_config)

        print("✅ SUCCESS: Cleaner initialized successfully!")
        print(f"   - Dry run: {cleaner.dry_run}")
        print(f"   - Verbose: {cleaner.verbose}")
        print(f"   - Backup enabled: {cleaner.enable_backup}")
        print(f"   - Advanced features: {cleaner.enable_advanced_features}")
        print(f"   - VM aware: {cleaner.vm_aware}")
        print(f"   - System reboot: {cleaner.system_reboot}")

        return True

    except Exception as e:
        print(f"❌ FAILED: {e}")
        import traceback

        print(f"Full traceback:\n{traceback.format_exc()}")
        return False


def test_gui_config_processing():
    """Test the GUI config processing"""
    print("\n🎨 Testing GUI config processing...")

    try:
        # Simulate GUI config
        gui_config = {
            "dry_run": True,
            "verbose": True,
            "enable_backup": True,
            "enable_advanced_features": True,
            "vm_aware": True,
            "system_reboot": False,
            "_force_cleanup": False,
            "_enable_performance_monitoring": True,
        }

        print(f"📋 GUI config: {gui_config}")

        # Process config like the CleanupWorker does
        force_cleanup = gui_config.pop("_force_cleanup", False)
        enable_performance_monitoring = gui_config.pop(
            "_enable_performance_monitoring", True
        )

        print(f"🔧 Processed config: {gui_config}")
        print(f"💪 Force cleanup: {force_cleanup}")
        print(f"📊 Performance monitoring: {enable_performance_monitoring}")

        # Test cleaner initialization
        from zoom_deep_clean.cleaner_enhanced import ZoomDeepCleanerEnhanced

        cleaner = ZoomDeepCleanerEnhanced(**gui_config)

        print("✅ SUCCESS: GUI config processing works!")
        return True

    except Exception as e:
        print(f"❌ FAILED: {e}")
        import traceback

        print(f"Full traceback:\n{traceback.format_exc()}")
        return False


def main():
    """Run all tests"""
    print("🚀 Testing PySide6 GUI Parameter Fix")
    print("=" * 50)

    success = True

    # Test 1: Basic cleaner config
    if not test_cleaner_config():
        success = False

    # Test 2: GUI config processing
    if not test_gui_config_processing():
        success = False

    print("\n" + "=" * 50)
    if success:
        print("🎉 ALL TESTS PASSED! The PySide6 GUI fix is working correctly.")
        print("\n🚀 You can now run the GUI with:")
        print("   python launch_pyside6_gui.py")
    else:
        print("❌ SOME TESTS FAILED! Please check the errors above.")

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
