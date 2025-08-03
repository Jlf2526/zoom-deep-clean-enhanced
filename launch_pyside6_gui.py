#!/usr/bin/env python3
"""
PySide6 GUI Launcher
Easy launcher for the modern Zoom Deep Clean Enhanced GUI

Created by: PHLthy215 (Enhanced by Amazon Q)
Version: 2.3.0 - PySide6 Launcher
"""

import sys
import os
import subprocess
from pathlib import Path

def check_pyside6():
    """Check if PySide6 is installed"""
    try:
        import PySide6
        return True, PySide6.__version__
    except ImportError:
        return False, None

def install_pyside6():
    """Install PySide6 and dependencies"""
    print("📦 Installing PySide6 and dependencies...")
    
    try:
        # Install from requirements file if available
        requirements_file = Path(__file__).parent / "requirements-pyside6.txt"
        if requirements_file.exists():
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", 
                "-r", str(requirements_file)
            ])
        else:
            # Fallback to basic installation
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", 
                "PySide6>=6.5.0", "psutil>=5.9.0"
            ])
        
        print("✅ Installation completed successfully!")
        return True
    
    except subprocess.CalledProcessError as e:
        print(f"❌ Installation failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error during installation: {e}")
        return False

def launch_gui():
    """Launch the PySide6 GUI"""
    try:
        # Add current directory to Python path
        current_dir = Path(__file__).parent
        sys.path.insert(0, str(current_dir))
        
        # Import and launch GUI
        from zoom_deep_clean.gui_pyside6 import main
        return main()
    
    except ImportError as e:
        print(f"❌ Failed to import GUI module: {e}")
        print("   Make sure all files are in the correct location.")
        return 1
    except Exception as e:
        print(f"❌ Failed to launch GUI: {e}")
        return 1

def main():
    """Main launcher function"""
    print("🚀 Zoom Deep Clean Enhanced - PySide6 GUI Launcher")
    print("="*60)
    
    # Check if PySide6 is available
    pyside6_available, version = check_pyside6()
    
    if not pyside6_available:
        print("⚠️  PySide6 not found!")
        print("   PySide6 is required for the modern GUI interface.")
        print()
        
        response = input("Would you like to install PySide6 now? (y/N): ").strip().lower()
        if response in ['y', 'yes']:
            if not install_pyside6():
                print("\n❌ Installation failed. Please install manually:")
                print("   pip install PySide6 psutil")
                return 1
            
            # Check again after installation
            pyside6_available, version = check_pyside6()
            if not pyside6_available:
                print("❌ PySide6 still not available after installation.")
                return 1
        else:
            print("\n💡 To install PySide6 manually, run:")
            print("   pip install PySide6 psutil")
            print("\n   Or use the requirements file:")
            print("   pip install -r requirements-pyside6.txt")
            return 1
    
    print(f"✅ PySide6 {version} is available")
    print("🎨 Launching modern GUI interface...")
    print()
    
    # Launch the GUI
    try:
        return launch_gui()
    except KeyboardInterrupt:
        print("\n🛑 Launch cancelled by user")
        return 0

if __name__ == "__main__":
    sys.exit(main())
