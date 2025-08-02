#!/bin/bash

# Install the working app bundle to Applications and create shortcuts

set -e

APP_NAME="Zoom Deep Clean Enhanced"
SOURCE_APP="$APP_NAME.app"
DEST_APP="/Applications/$APP_NAME.app"
DESKTOP_SHORTCUT="$HOME/Desktop/$APP_NAME.app"

echo "🚀 Installing Zoom Deep Clean Enhanced App..."

# Check if source app exists
if [[ ! -d "$SOURCE_APP" ]]; then
    echo "❌ Source app not found: $SOURCE_APP"
    exit 1
fi

# Remove existing app in Applications
if [[ -d "$DEST_APP" ]]; then
    echo "🗑️ Removing existing app from Applications..."
    rm -rf "$DEST_APP"
fi

# Copy app to Applications
echo "📦 Installing app to Applications folder..."
cp -R "$SOURCE_APP" "/Applications/"

# Set proper permissions
chmod -R 755 "$DEST_APP"
chmod +x "$DEST_APP/Contents/MacOS/$APP_NAME"

# Create desktop shortcut (symbolic link)
if [[ -d "$HOME/Desktop" ]]; then
    echo "🖥️ Creating desktop shortcut..."
    if [[ -L "$DESKTOP_SHORTCUT" ]]; then
        rm "$DESKTOP_SHORTCUT"
    fi
    ln -s "$DEST_APP" "$DESKTOP_SHORTCUT"
fi

# Test the installed app
echo "🧪 Testing installed app..."
if [[ -x "$DEST_APP/Contents/MacOS/$APP_NAME" ]]; then
    echo "✅ App installed successfully!"
    echo ""
    echo "📍 App location: $DEST_APP"
    if [[ -L "$DESKTOP_SHORTCUT" ]]; then
        echo "🖥️ Desktop shortcut: $DESKTOP_SHORTCUT"
    fi
    echo ""
    echo "🎯 How to use:"
    echo "  1. Double-click the app in Applications folder"
    echo "  2. Or double-click the desktop shortcut"
    echo "  3. Or run: open '$DEST_APP'"
    echo ""
    
    # Offer to launch the app
    read -p "Would you like to test launch the app now? (y/n): " -r
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "🚀 Launching app..."
        open "$DEST_APP"
        echo "✅ App launch command sent to system"
        echo "💡 If the app doesn't appear, check Activity Monitor for 'Python' processes"
    fi
else
    echo "❌ Installation failed - executable not found or not executable"
    exit 1
fi

echo ""
echo "🎉 Installation completed!"
echo ""
echo "📋 Troubleshooting tips:"
echo "  • If app doesn't launch, check Console.app for error messages"
echo "  • Ensure Python 3 and tkinter are installed"
echo "  • Try running from Terminal: open '$DEST_APP'"
echo "  • Check /tmp/zoom_debug.log for debug information"
