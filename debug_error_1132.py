#!/usr/bin/env python3
"""
Debug script to identify the specific causes of Zoom error 1132
"""
import subprocess
import os
import sys
import socket
from pathlib import Path

# Add the package to path so we can import our modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from zoom_deep_clean.error_1132_handler import Error1132Handler
import logging


def setup_simple_logging():
    """Setup simple logging for the debug script"""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    return logging.getLogger("error_1132_debug")


def main():
    print("🚀 Zoom Error 1132 Diagnostic Tool")
    print("=" * 50)

    # Setup logging
    logger = setup_simple_logging()

    # Create Error 1132 handler
    handler = Error1132Handler(logger, dry_run=True)  # Use dry_run=True for debugging

    # Run diagnostic
    print("🔍 Running Error 1132 Diagnostic...")
    results = handler.diagnose_error_1132()

    # Generate and print report
    print("\n" + "=" * 50)
    print("📋 ERROR 1132 DIAGNOSTIC REPORT")
    print("=" * 50)
    report = handler.generate_error_1132_report(results)
    print(report)

    print("\n💡 RECOMMENDATIONS:")
    print("1. Run the standalone fix script: python3 fix_error_1132_standalone.py")
    print("2. Or use the comprehensive tool with --fix-error-1132 flag")
    print("3. Restart your network router/modem")
    print("4. Try connecting from a different network if issues persist")


if __name__ == "__main__":
    main()
