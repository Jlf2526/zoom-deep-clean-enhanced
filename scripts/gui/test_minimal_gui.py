#!/usr/bin/env python3
"""
Minimal GUI test to identify crash issues
"""

import sys
import os


def test_minimal_gui():
    """Test the most basic GUI functionality"""
    try:
        print("1. Testing tkinter import...")
        import tkinter as tk

        print("✅ tkinter imported successfully")

        print("2. Testing basic window creation...")
        root = tk.Tk()
        root.title("Minimal Test")
        root.geometry("300x200")
        print("✅ Window created successfully")

        print("3. Testing label widget...")
        label = tk.Label(root, text="🔥 Zoom Deep Clean Enhanced\nMinimal Test")
        label.pack(pady=20)
        print("✅ Label created successfully")

        print("4. Testing button widget...")

        def on_click():
            print("Button clicked!")
            root.quit()

        button = tk.Button(root, text="Test Button", command=on_click)
        button.pack(pady=10)
        print("✅ Button created successfully")

        print("5. Testing auto-close...")
        root.after(3000, root.quit)  # Auto-close after 3 seconds

        print("6. Starting mainloop...")
        root.mainloop()
        print("✅ GUI test completed successfully")

        return True

    except Exception as e:
        print(f"❌ GUI test failed: {e}")
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    print("🧪 Running minimal GUI test...")
    success = test_minimal_gui()
    if success:
        print("🎉 Minimal GUI test passed!")
    else:
        print("💥 Minimal GUI test failed!")
        sys.exit(1)
