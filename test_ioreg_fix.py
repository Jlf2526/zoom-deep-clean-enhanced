#!/usr/bin/env python3
"""
Test script to verify IORegistry UTF-8 fix
"""

import sys
import os
import logging

# Add the package to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from zoom_deep_clean.deep_system_cleaner import DeepSystemCleaner


def test_ioreg_fix():
    """Test the IORegistry UTF-8 fix"""

    # Setup logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    print("🧪 Testing IORegistry UTF-8 Fix")
    print("=" * 40)

    try:
        # Create deep system cleaner
        cleaner = DeepSystemCleaner(logger, dry_run=True)

        # Test IORegistry clearing (this was causing the UTF-8 error)
        print("🔍 Testing IORegistry entry clearing...")
        cleared = cleaner._clear_ioreg_zoom_entries()
        print(f"✅ IORegistry test completed - would clear {cleared} entries")

        # Test verification method
        print("🔍 Testing deep cleanup verification...")
        verified = cleaner.verify_deep_cleanup()
        print(f"✅ Verification test completed - result: {verified}")

        return True

    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False


if __name__ == "__main__":
    success = test_ioreg_fix()
    sys.exit(0 if success else 1)
