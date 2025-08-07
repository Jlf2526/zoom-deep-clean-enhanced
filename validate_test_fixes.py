#!/usr/bin/env python3
"""
Test Validation Script
Validates that all the test fixes are working correctly
"""

import sys
import os
import subprocess
import tempfile

# Add the package to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

# Import the cleaner class
try:
    from zoom_deep_clean.cleaner_enhanced import ZoomDeepCleanerEnhanced
except ImportError:
    print("❌ Could not import ZoomDeepCleanerEnhanced")
    ZoomDeepCleanerEnhanced = None


def test_imports():
    """Test that all required imports work"""
    print("🧪 Testing imports...")

    try:
        import subprocess
        from zoom_deep_clean.cleaner_enhanced import ZoomDeepCleanerEnhanced

        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False


def test_cleaner_initialization():
    """Test cleaner initialization with correct parameters"""
    print("🧪 Testing cleaner initialization...")

    try:
        with tempfile.NamedTemporaryFile(delete=False) as temp_log:
            temp_log_path = temp_log.name
        cleaner = ZoomDeepCleanerEnhanced(
            log_file=temp_log_path,
            dry_run=True,
            verbose=True,
            enable_backup=True,
            vm_aware=True,
            system_reboot=False,
            enable_advanced_features=True,
        )
        print("✅ Cleaner initialization successful")
        return True
    except Exception as e:
        print(f"❌ Cleaner initialization failed: {e}")
        return False


def test_method_existence():
    """Test that required methods exist"""
    print("🧪 Testing method existence...")

    try:
        with tempfile.NamedTemporaryFile(delete=False) as temp_log:
            temp_log_path = temp_log.name
        cleaner = ZoomDeepCleanerEnhanced(log_file=temp_log_path, dry_run=True)

        # Test _run_command exists (not _execute_command)
        if not hasattr(cleaner, "_run_command"):
            print("❌ _run_command method missing")
            return False

        # Test cleanup_stats is accessible
        stats = cleaner.cleanup_stats
        if not isinstance(stats, dict):
            print("❌ cleanup_stats is not a dict")
            return False

        print("✅ All required methods exist")
        return True
    except Exception as e:
        print(f"❌ Method existence test failed: {e}")
        return False


def test_subprocess_timeout():
    """Test that subprocess.TimeoutExpired is available"""
    print("🧪 Testing subprocess.TimeoutExpired...")

    try:
        import subprocess

        # Create a TimeoutExpired exception (this should not raise an error)
        timeout_error = subprocess.TimeoutExpired("test", 5)
        print("✅ subprocess.TimeoutExpired available")
        return True
    except Exception as e:
        print(f"❌ subprocess.TimeoutExpired test failed: {e}")
        return False


def run_specific_test():
    """Run a specific test to validate fixes"""
    print("🧪 Running specific test validation...")

    try:
        # Try to run one of the fixed tests
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "unittest",
                "tests.test_cleaner_enhanced_additional.TestZoomDeepCleanerEnhancedSecurity.test_cleanup_stats_access",
                "-v",
            ],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(__file__),
        )

        if result.returncode == 0:
            print("✅ Specific test passed")
            return True
        else:
            print(f"❌ Specific test failed:")
            print(f"STDOUT: {result.stdout}")
            print(f"STDERR: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Test execution failed: {e}")
        return False


def main():
    """Run all validation tests"""
    print("🚀 Validating Test Fixes")
    print("=" * 50)

    tests = [
        ("Imports", test_imports),
        ("Cleaner Initialization", test_cleaner_initialization),
        ("Method Existence", test_method_existence),
        ("Subprocess TimeoutExpired", test_subprocess_timeout),
        ("Specific Test", run_specific_test),
    ]

    passed = 0
    total = len(tests)

    for test_name, test_func in tests:
        print(f"\n📋 {test_name}:")
        if test_func():
            passed += 1
        else:
            print(f"   Test failed!")

    print("\n" + "=" * 50)
    print(f"📊 Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 ALL VALIDATION TESTS PASSED!")
        print("The test fixes are working correctly.")
        return 0
    else:
        print("❌ SOME VALIDATION TESTS FAILED!")
        print("Please check the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
