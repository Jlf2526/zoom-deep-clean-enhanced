#!/usr/bin/env python3
"""
Enhanced TCC Database Cleaner - Fixes the core issue preventing meeting joins
"""

import subprocess
import sqlite3
import os
import logging


def clean_tcc_zoom_entries(dry_run=False):
    """Clean Zoom entries from TCC database - the core fix for meeting join issues"""

    tcc_paths = [
        "/Library/Application Support/com.apple.TCC/TCC.db",
        os.path.expanduser("~/Library/Application Support/com.apple.TCC/TCC.db"),
    ]

    cleaned_entries = 0

    for tcc_path in tcc_paths:
        if not os.path.exists(tcc_path):
            continue

        try:
            print(f"🔍 Processing TCC database: {tcc_path}")

            # First, show what we'll remove
            conn = sqlite3.connect(tcc_path)
            cursor = conn.cursor()
            cursor.execute(
                "SELECT service, client, auth_value FROM access WHERE client LIKE '%zoom%' OR client LIKE '%Zoom%'"
            )
            entries = cursor.fetchall()

            if entries:
                print(f"Found {len(entries)} Zoom TCC entries:")
                for service, client, auth_value in entries:
                    print(f"   {service}: {client} (auth: {auth_value})")

                if not dry_run:
                    # Remove all Zoom-related TCC entries
                    cursor.execute(
                        "DELETE FROM access WHERE client LIKE '%zoom%' OR client LIKE '%Zoom%'"
                    )
                    conn.commit()
                    print(f"✅ Removed {len(entries)} TCC entries from {tcc_path}")
                    cleaned_entries += len(entries)
                else:
                    print(f"[DRY RUN] Would remove {len(entries)} TCC entries")
                    cleaned_entries += len(entries)

            conn.close()

        except Exception as e:
            print(f"❌ Error processing TCC database {tcc_path}: {e}")

    return cleaned_entries


def reset_zoom_permissions():
    """Reset Zoom permissions completely"""
    print("🔄 Resetting Zoom system permissions...")

    # Reset TCC permissions for Zoom
    try:
        subprocess.run(
            ["sudo", "tccutil", "reset", "All", "us.zoom.xos"],
            capture_output=True,
            check=False,
        )
        subprocess.run(
            ["sudo", "tccutil", "reset", "All", "sh.1132.ZoomFixer"],
            capture_output=True,
            check=False,
        )
        print("✅ Reset system permissions")
        return True
    except Exception as e:
        print(f"❌ Error resetting permissions: {e}")
        return False


if __name__ == "__main__":
    import sys

    dry_run = "--dry-run" in sys.argv

    print("🚀 TCC Database Cleaner - Core Fix for Meeting Join Issues")
    print("=" * 60)

    cleaned = clean_tcc_zoom_entries(dry_run)

    if not dry_run and cleaned > 0:
        reset_zoom_permissions()
        print("\n💡 NEXT STEPS:")
        print("1. Restart your Mac")
        print("2. Reinstall Zoom from official website")
        print("3. Grant permissions when prompted")

    print(f"\n📊 Total TCC entries processed: {cleaned}")
