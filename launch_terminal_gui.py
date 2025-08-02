#!/usr/bin/env python3
"""
Terminal-based launcher that should work reliably
"""

import sys
import os

# Add the package to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'zoom_deep_clean'))

def main():
    """Launch GUI with comprehensive error handling"""
    print("🚀 Zoom Deep Clean Enhanced - Terminal Launcher")
    print("=" * 50)
    
    try:
        # Test tkinter
        print("1. Testing tkinter...")
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        root.destroy()
        print("   ✅ tkinter working")
        
        # Test imports
        print("2. Testing imports...")
        from zoom_deep_clean.gui_simple import SimpleZoomCleanerGUI
        print("   ✅ GUI imports working")
        
        # Launch GUI
        print("3. Launching GUI...")
        app = SimpleZoomCleanerGUI()
        print("   ✅ GUI created successfully")
        
        print("4. Starting GUI mainloop...")
        app.run()
        
        print("✅ GUI session completed")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("\nTroubleshooting:")
        print("• Ensure tkinter is installed: brew install python-tk")
        print("• Check Python version: python3 --version")
        return False
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        print("\nTroubleshooting:")
        print("• Try running from the project directory")
        print("• Check if all files are present")
        print("• Verify Python path and imports")
        return False
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        if not success:
            input("\nPress Enter to exit...")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 Interrupted by user")
        sys.exit(0)
