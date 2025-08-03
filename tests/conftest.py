#!/usr/bin/env python3
"""
Test configuration for Zoom Deep Clean Enhanced
Ensures proper module discovery and imports
"""

import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Ensure we can import the main package
try:
    import zoom_deep_clean

    print(f"✅ Successfully imported zoom_deep_clean from {zoom_deep_clean.__file__}")
except ImportError as e:
    print(f"❌ Failed to import zoom_deep_clean: {e}")
    print(f"Python path: {sys.path}")
    print(f"Project root: {project_root}")
    print(f"Contents: {list(project_root.iterdir())}")
