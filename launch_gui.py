#!/usr/bin/env python3
"""
Zoom Deep Clean Enhanced - Improved GUI Launcher
Launch the user-friendly GUI application with enhanced scrolling and performance

Created by: PHLthy215
Enhanced Version: 2.2.0 - Improved GUI Launcher
"""

import sys
import os

# Add the package to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'zoom_deep_clean'))

def main():
    """Main entry point for the improved GUI"""
    try:
        # Check tkinter availability first
        try:
            import tkinter as tk
            # Test basic tkinter functionality
            root = tk.Tk()
            root.withdraw()
            root.destroy()
        except ImportError:
            print("❌ Error: tkinter GUI library not available")
            print("Please install tkinter:")
            print("  brew install python-tk")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Error: tkinter test failed: {e}")
            sys.exit(1)
        
        # Import and run the improved GUI
        from zoom_deep_clean.gui_app import ZoomCleanerGUI
        
        print("🚀 Launching Zoom Deep Clean Enhanced GUI...")
        print("✨ Features: Improved scrolling, better performance, context menus")
        
        app = ZoomCleanerGUI()
        
        # Add welcome message
        app.log_message("🎨 Welcome to Zoom Deep Clean Enhanced!", "info")
        app.log_message("✨ GUI improvements: Better scrolling, performance, and usability", "success")
        app.log_message("📝 Right-click in output area for context menu", "info")
        app.log_message("🔍 Always start with Preview Mode for safety", "warning")
        
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
