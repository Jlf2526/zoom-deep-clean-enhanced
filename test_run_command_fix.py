#!/usr/bin/env python3
"""
Test script to verify _run_command method fixes
"""

import sys
import os
import tempfile
import unittest
from unittest.mock import patch, MagicMock
import subprocess

# Add the package to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from zoom_deep_clean.cleaner_enhanced import ZoomDeepCleanerEnhanced


def test_run_command_basic():
    """Test basic _run_command functionality"""
    print("🧪 Testing basic _run_command functionality...")

    temp_log = tempfile.mktemp()
    cleaner = ZoomDeepCleanerEnhanced(log_file=temp_log, dry_run=False)

    # Test that method exists and has correct signature
    if not hasattr(cleaner, "_run_command"):
        print("❌ _run_command method not found")
        return False

    print("✅ _run_command method exists")
    return True


@patch("subprocess.run")
def test_run_command_success(mock_subprocess):
    """Test _run_command with successful execution"""
    print("🧪 Testing _run_command success case...")

    mock_result = MagicMock()
    mock_result.returncode = 0
    mock_result.stdout = "Success output"
    mock_result.stderr = ""
    mock_subprocess.return_value = mock_result

    temp_log = tempfile.mktemp()
    cleaner = ZoomDeepCleanerEnhanced(log_file=temp_log, dry_run=False)

    success, output = cleaner._run_command("echo", ["echo", "test"])

    if success and output == "Success output":
        print("✅ Success case works correctly")
        return True
    else:
        print(f"❌ Success case failed: success={success}, output='{output}'")
        return False


@patch("subprocess.run")
def test_run_command_failure(mock_subprocess):
    """Test _run_command with command failure"""
    print("🧪 Testing _run_command failure case...")

    mock_result = MagicMock()
    mock_result.returncode = 1
    mock_result.stdout = ""
    mock_result.stderr = "Error message"
    mock_subprocess.return_value = mock_result

    temp_log = tempfile.mktemp()
    cleaner = ZoomDeepCleanerEnhanced(log_file=temp_log, dry_run=False)

    success, output = cleaner._run_command("false", ["false"])

    if not success and "Error message" in output:
        print("✅ Failure case works correctly")
        return True
    else:
        print(f"❌ Failure case failed: success={success}, output='{output}'")
        return False


@patch("subprocess.run")
def test_run_command_timeout(mock_subprocess):
    """Test _run_command with timeout"""
    print("🧪 Testing _run_command timeout case...")

    mock_subprocess.side_effect = subprocess.TimeoutExpired("test", 5)

    temp_log = tempfile.mktemp()
    cleaner = ZoomDeepCleanerEnhanced(log_file=temp_log, dry_run=False)

    success, output = cleaner._run_command("sleep", ["sleep", "10"], timeout=1)

    if not success and "timed out" in output:
        print("✅ Timeout case works correctly")
        return True
    else:
        print(f"❌ Timeout case failed: success={success}, output='{output}'")
        return False


@patch("subprocess.run")
def test_run_command_sudo(mock_subprocess):
    """Test _run_command with sudo"""
    print("🧪 Testing _run_command sudo case...")

    mock_result = MagicMock()
    mock_result.returncode = 0
    mock_result.stdout = "Success"
    mock_result.stderr = ""
    mock_subprocess.return_value = mock_result

    temp_log = tempfile.mktemp()
    cleaner = ZoomDeepCleanerEnhanced(log_file=temp_log, dry_run=False)

    success, output = cleaner._run_command(
        "privileged_command", ["privileged_command"], require_sudo=True
    )

    # Check if subprocess.run was called with sudo
    if mock_subprocess.called:
        args = mock_subprocess.call_args[0][0]
        if args[0] == "sudo":
            print("✅ Sudo case works correctly")
            return True
        else:
            print(f"❌ Sudo not prepended: {args}")
            return False
    else:
        print("❌ subprocess.run was not called")
        return False


def main():
    """Run all tests"""
    print("🚀 Testing _run_command Method Fixes")
    print("=" * 50)

    tests = [
        ("Basic Functionality", test_run_command_basic),
        ("Success Case", test_run_command_success),
        ("Failure Case", test_run_command_failure),
        ("Timeout Case", test_run_command_timeout),
        ("Sudo Case", test_run_command_sudo),
    ]

    passed = 0
    total = len(tests)

    for test_name, test_func in tests:
        print(f"\n📋 {test_name}:")
        try:
            if test_func():
                passed += 1
            else:
                print(f"   Test failed!")
        except Exception as e:
            print(f"   Test error: {e}")

    print("\n" + "=" * 50)
    print(f"📊 Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 ALL TESTS PASSED! The _run_command fixes are working correctly.")
        return 0
    else:
        print("❌ SOME TESTS FAILED! Please check the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
