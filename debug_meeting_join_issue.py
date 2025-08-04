#!/usr/bin/env python3
"""
Debug script to identify the specific system component preventing Zoom meeting joins
while allowing successful login.
"""

import subprocess
import sqlite3
import os
import json
from pathlib import Path


def check_ioreg_zoom_entries():
    """Check for IORegistry entries that might block meeting joins"""
    print("🔍 Checking IORegistry for Zoom entries...")
    try:
        result = subprocess.run(["ioreg", "-l"], capture_output=True, text=True)
        zoom_entries = [
            line
            for line in result.stdout.split("\n")
            if "zoom" in line.lower()
            or ("IOUserClientCreator" in line and "zoom" in line.lower())
        ]

        if zoom_entries:
            print("❌ Found IORegistry Zoom entries (CRITICAL for meeting join):")
            for entry in zoom_entries:
                print(f"   {entry.strip()}")
            return True
        else:
            print("✅ No IORegistry Zoom entries found")
            return False
    except Exception as e:
        print(f"❌ Error checking IORegistry: {e}")
        return False


def check_tcc_database():
    """Check TCC database for Zoom privacy permissions"""
    print("\n🔍 Checking TCC database for Zoom permissions...")
    tcc_paths = [
        "/Library/Application Support/com.apple.TCC/TCC.db",
        "~/Library/Application Support/com.apple.TCC/TCC.db",
    ]

    found_entries = False
    for tcc_path in tcc_paths:
        tcc_path = os.path.expanduser(tcc_path)
        if os.path.exists(tcc_path):
            try:
                conn = sqlite3.connect(tcc_path)
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT service, client, auth_value FROM access WHERE client LIKE '%zoom%' OR client LIKE '%Zoom%'"
                )
                entries = cursor.fetchall()

                if entries:
                    print(f"❌ Found TCC entries in {tcc_path}:")
                    for service, client, auth_value in entries:
                        print(
                            f"   Service: {service}, Client: {client}, Auth: {auth_value}"
                        )
                    found_entries = True
                conn.close()
            except Exception as e:
                print(f"❌ Error checking TCC database {tcc_path}: {e}")

    if not found_entries:
        print("✅ No TCC database entries found")
    return found_entries


def check_system_temp_files():
    """Check for system temp files that might interfere with meeting joins"""
    print("\n🔍 Checking system temp files...")
    temp_dirs = ["/private/var/folders", "/tmp", "/private/tmp"]
    found_files = []

    for temp_dir in temp_dirs:
        if os.path.exists(temp_dir):
            try:
                result = subprocess.run(
                    ["find", temp_dir, "-name", "*zoom*", "-o", "-name", "*Zoom*"],
                    capture_output=True,
                    text=True,
                )
                if result.stdout.strip():
                    files = result.stdout.strip().split("\n")
                    found_files.extend(files)
            except Exception as e:
                print(f"❌ Error checking {temp_dir}: {e}")

    if found_files:
        print("❌ Found system temp files:")
        for file in found_files[:10]:  # Show first 10
            print(f"   {file}")
        if len(found_files) > 10:
            print(f"   ... and {len(found_files) - 10} more")
        return True
    else:
        print("✅ No system temp files found")
        return False


def check_audio_video_configs():
    """Check for audio/video configurations that might block meeting media"""
    print("\n🔍 Checking audio/video configurations...")
    av_paths = [
        "/Library/Audio/Plug-Ins/HAL",
        "/Library/CoreMediaIO/Plug-Ins/DAL",
        "/private/var/db/CoreAudio",
    ]

    found_configs = []
    for av_path in av_paths:
        if os.path.exists(av_path):
            try:
                result = subprocess.run(
                    ["find", av_path, "-name", "*zoom*", "-o", "-name", "*Zoom*"],
                    capture_output=True,
                    text=True,
                )
                if result.stdout.strip():
                    files = result.stdout.strip().split("\n")
                    found_configs.extend(files)
            except Exception as e:
                print(f"❌ Error checking {av_path}: {e}")

    if found_configs:
        print("❌ Found audio/video configurations:")
        for config in found_configs:
            print(f"   {config}")
        return True
    else:
        print("✅ No audio/video configurations found")
        return False


def check_network_cache():
    """Check for network cache issues"""
    print("\n🔍 Checking network cache...")
    try:
        # Check DNS cache for Zoom domains
        result = subprocess.run(
            ["dscacheutil", "-q", "host", "-a", "name", "zoom.us"],
            capture_output=True,
            text=True,
        )
        if result.stdout.strip():
            print("❌ Found cached DNS entries for Zoom domains")
            print(f"   {result.stdout.strip()}")
            return True
        else:
            print("✅ No problematic DNS cache found")
            return False
    except Exception as e:
        print(f"❌ Error checking network cache: {e}")
        return False


def check_keychain_entries():
    """Check for keychain entries that might interfere"""
    print("\n🔍 Checking keychain for Zoom entries...")
    try:
        result = subprocess.run(
            ["security", "dump-keychain"], capture_output=True, text=True
        )
        zoom_entries = [
            line for line in result.stdout.split("\n") if "zoom" in line.lower()
        ]

        if zoom_entries:
            print("❌ Found keychain entries:")
            for entry in zoom_entries[:5]:  # Show first 5
                print(f"   {entry.strip()}")
            return True
        else:
            print("✅ No keychain entries found")
            return False
    except Exception as e:
        print(f"❌ Error checking keychain: {e}")
        return False


def main():
    print("🚀 Zoom Meeting Join Issue Diagnostic Tool")
    print("=" * 50)

    issues_found = []

    if check_ioreg_zoom_entries():
        issues_found.append("IORegistry entries (CRITICAL)")

    if check_tcc_database():
        issues_found.append("TCC database permissions")

    if check_system_temp_files():
        issues_found.append("System temp files")

    if check_audio_video_configs():
        issues_found.append("Audio/Video configurations")

    if check_network_cache():
        issues_found.append("Network cache")

    if check_keychain_entries():
        issues_found.append("Keychain entries")

    print("\n" + "=" * 50)
    print("📊 DIAGNOSTIC SUMMARY")
    print("=" * 50)

    if issues_found:
        print("❌ Issues found that could prevent meeting joins:")
        for i, issue in enumerate(issues_found, 1):
            print(f"   {i}. {issue}")

        print("\n💡 RECOMMENDATION:")
        print(
            "Run your zoom-deep-clean-enhanced tool with --force to address these issues."
        )

        if "IORegistry entries (CRITICAL)" in issues_found:
            print(
                "\n⚠️  CRITICAL: IORegistry entries are the most likely cause of meeting join failures!"
            )
    else:
        print("✅ No obvious system-level issues found.")
        print("The problem might be:")
        print("   1. Network connectivity issues")
        print("   2. Zoom server-side problems")
        print("   3. Firewall/security software interference")


if __name__ == "__main__":
    main()
