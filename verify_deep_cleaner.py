#!/usr/bin/env python3
"""
Verify Deep System Cleaner Integration
Quick test to ensure the deep system cleaner is properly integrated
"""

import sys
import os
from pathlib import Path

# Add the project directory to Python path
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))


def test_deep_cleaner_integration():
    """Test if the deep system cleaner is properly integrated"""
    print("🔍 Verifying Deep System Cleaner Integration...")
    print("=" * 50)

    try:
        # Test 1: Import the deep system cleaner
        print("1. Testing deep system cleaner import...", end=" ")
        from zoom_deep_clean.deep_system_cleaner import DeepSystemCleaner

        print("✅ SUCCESS")

        # Test 2: Import the main cleaner
        print("2. Testing main cleaner import...", end=" ")
        from zoom_deep_clean.cleaner_enhanced import ZoomDeepCleanerEnhanced

        print("✅ SUCCESS")

        # Test 3: Initialize the cleaner (dry run mode)
        print("3. Testing cleaner initialization...", end=" ")
        cleaner = ZoomDeepCleanerEnhanced(
            verbose=False,
            dry_run=True,
            enable_backup=False,
            vm_aware=True,
            enable_advanced_features=True,
        )
        print("✅ SUCCESS")

        # Test 4: Check if deep system cleaner is initialized
        print("4. Testing deep system cleaner initialization...", end=" ")
        if (
            hasattr(cleaner, "deep_system_cleaner")
            and cleaner.deep_system_cleaner is not None
        ):
            print("✅ SUCCESS")
        else:
            print("❌ FAILED - Deep system cleaner not initialized")
            return False

        # Test 5: Check if deep system cleaner has required methods
        print("5. Testing deep system cleaner methods...", end=" ")
        required_methods = [
            "clean_deep_system_artifacts",
            "verify_deep_cleanup",
            "generate_deep_cleanup_report",
        ]

        for method in required_methods:
            if not hasattr(cleaner.deep_system_cleaner, method):
                print(f"❌ FAILED - Missing method: {method}")
                return False
        print("✅ SUCCESS")

        print()
        print("🎉 All tests passed! Deep system cleaner is properly integrated.")
        print()
        print("Available deep system cleaning features:")
        print("• IORegistry Zoom entry clearing")
        print("• System temp file deep scanning")
        print("• Network configuration reset")
        print("• Audio/video system cleanup")
        print("• System identifier clearing")
        print("• Package receipt removal")
        print("• Deep cache clearing")
        print("• Kernel extension cleanup")
        print()
        print("Ready to run enhanced deep system cleaning!")
        return True

    except ImportError as e:
        print(f"❌ IMPORT ERROR: {e}")
        return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False


if __name__ == "__main__":
    success = test_deep_cleaner_integration()
    if success:
        print("\n🚀 To run the enhanced deep system cleaning:")
        print("   python3 run_deep_system_clean.py")
        print("\n   or with sudo for full system access:")
        print("   sudo python3 run_deep_system_clean.py")
    else:
        print("\n❌ Deep system cleaner integration failed.")
        print("   Please check the error messages above.")
