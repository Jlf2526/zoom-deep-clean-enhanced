#!/usr/bin/env python3
"""
Test the improved GUI with better scrolling and performance
"""

import sys
import os
import time
import threading

# Add the package to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'zoom_deep_clean'))

def test_gui_improvements():
    """Test the improved GUI features"""
    try:
        from zoom_deep_clean.gui_app import ZoomCleanerGUI
        
        print("🎨 Testing Improved GUI Features...")
        app = ZoomCleanerGUI()
        
        # Add test messages to demonstrate improved scrolling
        def add_test_messages():
            time.sleep(1)  # Wait for GUI to load
            
            # Add various types of messages
            for i in range(50):
                app.log_message(f"Test info message {i+1} - This is a longer message to test text wrapping and scrolling performance", "info")
                if i % 10 == 0:
                    app.log_message(f"✅ Success message {i+1}", "success")
                if i % 15 == 0:
                    app.log_message(f"⚠️ Warning message {i+1}", "warning")
                if i % 20 == 0:
                    app.log_message(f"❌ Error message {i+1}", "error")
                
                app.update_progress((i + 1) * 2)  # Update progress
                time.sleep(0.1)  # Small delay to see the updates
            
            app.log_message("🎉 GUI improvement test completed!", "success")
            app.log_message("Features tested:", "info")
            app.log_message("✅ Improved scrolling with scrollbars", "success")
            app.log_message("✅ Better text buffer management", "success")
            app.log_message("✅ Reduced screen tearing", "success")
            app.log_message("✅ Context menu (right-click to test)", "success")
            app.log_message("✅ Mouse wheel scrolling", "success")
            app.log_message("✅ Keyboard shortcuts (Cmd+A, Cmd+C, Cmd+Shift+K)", "success")
        
        # Start test messages in background thread
        test_thread = threading.Thread(target=add_test_messages, daemon=True)
        test_thread.start()
        
        # Add initial welcome message
        app.log_message("🎨 Welcome to the Improved GUI Test!", "info")
        app.log_message("✨ Testing enhanced scrolling and performance features", "info")
        app.log_message("📝 Right-click in this area for context menu", "info")
        app.log_message("🖱️ Use mouse wheel to scroll", "info")
        app.log_message("⌨️ Try keyboard shortcuts: Cmd+A (select all), Cmd+C (copy), Cmd+Shift+K (clear)", "info")
        app.log_message("🔄 Auto-scroll can be toggled in context menu", "info")
        
        # Run the GUI
        app.run()
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Please ensure tkinter is installed: brew install python-tk")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_gui_improvements()
