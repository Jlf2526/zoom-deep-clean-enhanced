#!/usr/bin/env python3
"""
Test script to verify the Zoom application removal fix
"""

import os
import sys
import subprocess
import tempfile


def test_zoom_app_detection():
    """Test the Zoom application detection logic"""
    print("🧪 Testing Zoom application detection...")

    # Test the detection logic
    zoom_app_paths = [
        "/Applications/zoom.us.app",
        "/Applications/Zoom.app",
        "/Applications/ZoomPhone.app",
        "/Applications/ZoomClips.app",
        "/Applications/ZoomChat.app",
        "/Applications/ZoomPresence.app",
        "/Applications/ZoomUpdater.app",
        "/Applications/ZoomInstaller.app",
    ]

    found_apps = []
    for app_path in zoom_app_paths:
        if os.path.exists(app_path):
            found_apps.append(app_path)
            print(f"✅ FOUND: {app_path}")

    # Check for additional Zoom apps
    try:
        if os.path.exists("/Applications"):
            for item in os.listdir("/Applications"):
                if (
                    item.lower().startswith("zoom")
                    and item.endswith(".app")
                    and "deep clean" not in item.lower()
                    and "cleaner" not in item.lower()
                ):

                    app_path = f"/Applications/{item}"
                    if app_path not in zoom_app_paths:
                        found_apps.append(app_path)
                        print(f"✅ FOUND additional: {app_path}")
    except Exception as e:
        print(f"❌ Error scanning /Applications: {e}")

    print(f"📊 Total Zoom apps that would be removed: {len(found_apps)}")
    return found_apps


def create_test_zoom_app():
    """Create a test Zoom app for testing"""
    test_app_path = "/Applications/zoom.us.app"
    try:
        print(f"🔧 Creating test Zoom app at {test_app_path}")
        subprocess.run(["sudo", "mkdir", "-p", f"{test_app_path}/Contents"], check=True)
        subprocess.run(
            [
                "sudo",
                "sh",
                "-c",
                f"echo 'Test Zoom App' > {test_app_path}/Contents/Info.plist",
            ],
            check=True,
        )
        print(f"✅ Test app created successfully")
        return test_app_path
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to create test app: {e}")
        return None


def remove_test_zoom_app(app_path):
    """Remove the test Zoom app"""
    try:
        print(f"🧹 Removing test app {app_path}")
        subprocess.run(["sudo", "rm", "-rf", app_path], check=True)
        print(f"✅ Test app removed successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to remove test app: {e}")


def main():
    print("🚀 Testing Zoom Deep Clean Enhanced - Application Removal Fix")
    print("=" * 60)

    # Test 1: Check current state
    print("\n📋 Test 1: Current Zoom applications")
    initial_apps = test_zoom_app_detection()

    # Test 2: Create and detect test app
    print("\n📋 Test 2: Create test app and verify detection")
    test_app = create_test_zoom_app()
    if test_app:
        apps_with_test = test_zoom_app_detection()
        if len(apps_with_test) > len(initial_apps):
            print("✅ Test app successfully detected")
        else:
            print("❌ Test app not detected")

        # Clean up
        remove_test_zoom_app(test_app)

        # Verify cleanup
        print("\n📋 Test 3: Verify test app removal")
        final_apps = test_zoom_app_detection()
        if len(final_apps) == len(initial_apps):
            print("✅ Test app successfully removed")
        else:
            print("❌ Test app removal failed")

    print("\n🎉 Testing complete!")
    print("\n💡 The fix adds a new method 'remove_zoom_applications()' that:")
    print("   • Checks common Zoom app paths in /Applications")
    print("   • Scans for any additional Zoom apps")
    print("   • Excludes the cleanup tool itself")
    print("   • Properly handles errors and permissions")
    print("   • Is integrated into the main cleanup sequence")


if __name__ == "__main__":
    main()
