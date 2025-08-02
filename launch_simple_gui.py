#!/usr/bin/env python3
"""
Zoom Deep Clean Enhanced - Simple Stable GUI Launcher
Launch the simple, stable GUI that should work reliably

Created by: PHLthy215
Enhanced Version: 2.2.0 - Simple Stable GUI Launcher
"""

import sys
import os

# Add the package to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'zoom_deep_clean'))

def main():
    """Main entry point for the simple stable GUI"""
    try:
        # Check tkinter availability first
        try:
            import tkinter as tk
            # Test basic tkinter functionality
            root = tk.Tk()
            root.withdraw()
            root.destroy()
            print("✅ tkinter test passed")
        except ImportError:
            print("❌ Error: tkinter GUI library not available")
            print("Please install tkinter:")
            print("  brew install python-tk")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Error: tkinter test failed: {e}")
            sys.exit(1)
        
        # Import and run the simple stable GUI
        from zoom_deep_clean.gui_simple import SimpleZoomCleanerGUI
        
        print("🚀 Launching Simple Stable GUI...")
        
        app = SimpleZoomCleanerGUI()
        app.run()
        
    except ImportError as e:
        print(f"❌ Error importing GUI application: {e}")
        print("Please ensure all dependencies are installed.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 GUI application interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error starting GUI application: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
