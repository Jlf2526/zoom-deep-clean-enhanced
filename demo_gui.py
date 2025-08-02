#!/usr/bin/env python3
"""
Zoom Deep Clean Enhanced - GUI Demo
Demonstrate the GUI application features

Created by: PHLthy215
Enhanced Version: 2.2.0 - GUI Demo
"""

import sys
import os

# Add the package to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'zoom_deep_clean'))

def main():
    print("🎨 Zoom Deep Clean Enhanced - GUI Demo")
    print("=" * 50)
    print()
    print("This demo will show you the user-friendly GUI interface")
    print("for the advanced Zoom cleanup utility.")
    print()
    print("Features you'll see:")
    print("✅ Modern macOS-style interface")
    print("✅ Real-time progress tracking")
    print("✅ Interactive configuration options")
    print("✅ Live log output with color coding")
    print("✅ Built-in help and safety features")
    print("✅ Advanced fingerprint removal options")
    print()
    
    try:
        input("Press Enter to launch the GUI demo...")
        
        # Import and launch GUI
        from zoom_deep_clean.gui_app import ZoomCleanerGUI
        
        print("🚀 Launching GUI application...")
        app = ZoomCleanerGUI()
        
        # Add demo message to the output
        app.log_message("🎨 Welcome to Zoom Deep Clean Enhanced GUI!", "info")
        app.log_message("✅ This is a demonstration of the user interface", "success")
        app.log_message("🔍 Try the Preview Mode to see how it works", "info")
        app.log_message("⚙️ Configure options and explore the features", "info")
        app.log_message("❓ Click Help for detailed documentation", "info")
        
        app.run()
        
    except KeyboardInterrupt:
        print("\n👋 Demo cancelled by user")
    except ImportError as e:
        print(f"❌ Error importing GUI: {e}")
        print("Please ensure tkinter is installed:")
        print("  brew install python-tk")
    except Exception as e:
        print(f"❌ Error running demo: {e}")

if __name__ == "__main__":
    main()
