#!/bin/bash

# Verify the app installation and test all launch methods

echo "🔍 Verifying Zoom Deep Clean Enhanced App Installation"
echo "=" * 60

APP_PATH="/Applications/Zoom Deep Clean Enhanced.app"
DESKTOP_SHORTCUT="$HOME/Desktop/Zoom Deep Clean Enhanced.app"
EXECUTABLE="$APP_PATH/Contents/MacOS/Zoom Deep Clean Enhanced"

echo "1. ✅ Checking app installation..."
if [[ -d "$APP_PATH" ]]; then
    echo "   ✅ App found in Applications folder"
else
    echo "   ❌ App not found in Applications folder"
    exit 1
fi

echo "2. ✅ Checking desktop shortcut..."
if [[ -L "$DESKTOP_SHORTCUT" ]]; then
    echo "   ✅ Desktop shortcut exists"
else
    echo "   ❌ Desktop shortcut not found"
fi

echo "3. ✅ Checking executable permissions..."
if [[ -x "$EXECUTABLE" ]]; then
    echo "   ✅ Executable has proper permissions"
else
    echo "   ❌ Executable permissions issue"
    exit 1
fi

echo "4. ✅ Checking Python dependencies..."
cd "$APP_PATH/Contents/Resources"
if python3 -c "import tkinter; print('   ✅ tkinter available')" 2>/dev/null; then
    echo "   ✅ Python and tkinter working"
else
    echo "   ❌ Python or tkinter issue"
fi

echo "5. ✅ Testing app import..."
if python3 -c "
import sys
sys.path.insert(0, '.')
from zoom_deep_clean.gui_app import ZoomCleanerGUI
print('   ✅ GUI app imports successfully')
" 2>/dev/null; then
    echo "   ✅ App imports working"
else
    echo "   ❌ App import issues"
fi

echo ""
echo "🎯 Launch Methods Available:"
echo "   1. Double-click: $APP_PATH"
echo "   2. Desktop shortcut: $DESKTOP_SHORTCUT"
echo "   3. Terminal: open '$APP_PATH'"
echo "   4. Spotlight: Search for 'Zoom Deep Clean Enhanced'"
echo ""

echo "🧪 Quick Launch Test:"
echo "   Running: open '$APP_PATH'"
open "$APP_PATH" 2>&1 &
sleep 2
echo "   ✅ Launch command executed"
echo ""

echo "📋 Debug Information:"
echo "   • Debug log: /tmp/zoom_debug.log"
echo "   • App bundle: $APP_PATH"
echo "   • Resources: $APP_PATH/Contents/Resources"
echo "   • Python path includes app resources"
echo ""

echo "🎉 Verification Complete!"
echo ""
echo "💡 If the GUI doesn't appear:"
echo "   1. Check Activity Monitor for Python processes"
echo "   2. Look at Console.app for error messages"
echo "   3. Check /tmp/zoom_debug.log for debug info"
echo "   4. Try running: python3 '$APP_PATH/Contents/Resources/launch_gui.py'"
