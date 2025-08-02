#!/bin/bash

# Create a proper macOS app bundle for Zoom Deep Clean Enhanced
# This script creates a self-contained app that can run from Finder

set -e

APP_NAME="Zoom Deep Clean Enhanced"
BUNDLE_DIR="$APP_NAME.app"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🔨 Creating macOS app bundle..."

# Remove existing bundle
if [[ -d "$BUNDLE_DIR" ]]; then
    echo "Removing existing app bundle..."
    rm -rf "$BUNDLE_DIR"
fi

# Create app bundle structure
echo "Creating app bundle structure..."
mkdir -p "$BUNDLE_DIR/Contents/MacOS"
mkdir -p "$BUNDLE_DIR/Contents/Resources"
mkdir -p "$BUNDLE_DIR/Contents/Frameworks"

# Copy all Python files into the app bundle
echo "Copying Python files..."
cp -r zoom_deep_clean "$BUNDLE_DIR/Contents/Resources/"
cp launch_gui.py "$BUNDLE_DIR/Contents/Resources/"
cp setup.py "$BUNDLE_DIR/Contents/Resources/"
cp requirements.txt "$BUNDLE_DIR/Contents/Resources/"

# Create the main executable script
echo "Creating main executable..."
cat > "$BUNDLE_DIR/Contents/MacOS/$APP_NAME" << 'EOF'
#!/bin/bash

# Get the directory where this app bundle is located
BUNDLE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RESOURCES_DIR="$BUNDLE_DIR/Contents/Resources"

# Set up Python path
export PYTHONPATH="$RESOURCES_DIR:$PYTHONPATH"

# Change to resources directory
cd "$RESOURCES_DIR"

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    osascript -e 'display dialog "Python 3 is required but not installed. Please install Python 3 from python.org or using Homebrew." buttons {"OK"} default button "OK" with icon stop'
    exit 1
fi

# Check if tkinter is available
if ! python3 -c "import tkinter" 2>/dev/null; then
    osascript -e 'display dialog "tkinter GUI library is required but not available. Please install it using: brew install python-tk" buttons {"OK"} default button "OK" with icon stop'
    exit 1
fi

# Launch the GUI application
python3 launch_gui.py 2>&1 | logger -t "ZoomDeepClean"
EOF

# Make the executable script executable
chmod +x "$BUNDLE_DIR/Contents/MacOS/$APP_NAME"

# Create Info.plist
echo "Creating Info.plist..."
cat > "$BUNDLE_DIR/Contents/Info.plist" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleDisplayName</key>
    <string>Zoom Deep Clean Enhanced</string>
    <key>CFBundleExecutable</key>
    <string>$APP_NAME</string>
    <key>CFBundleIconFile</key>
    <string>app_icon</string>
    <key>CFBundleIdentifier</key>
    <string>com.phlthy215.zoom-deep-clean-enhanced</string>
    <key>CFBundleInfoDictionaryVersion</key>
    <string>6.0</string>
    <key>CFBundleName</key>
    <string>Zoom Deep Clean Enhanced</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleShortVersionString</key>
    <string>2.2.0</string>
    <key>CFBundleVersion</key>
    <string>2.2.0</string>
    <key>LSMinimumSystemVersion</key>
    <string>10.14</string>
    <key>NSHighResolutionCapable</key>
    <true/>
    <key>NSRequiresAquaSystemAppearance</key>
    <false/>
    <key>LSApplicationCategoryType</key>
    <string>public.app-category.utilities</string>
    <key>NSHumanReadableCopyright</key>
    <string>© 2025 PHLthy215. All rights reserved.</string>
    <key>CFBundleGetInfoString</key>
    <string>Zoom Deep Clean Enhanced v2.2.0 - VM-Aware &amp; System-Wide Device Fingerprint Removal</string>
    <key>LSUIElement</key>
    <false/>
</dict>
</plist>
EOF

# Create a simple app icon (text-based)
echo "Creating app icon..."
cat > "$BUNDLE_DIR/Contents/Resources/app_icon.icns" << 'EOF'
# This is a placeholder for the app icon
# In a real app, this would be a proper .icns file
EOF

# Set proper permissions
echo "Setting permissions..."
chmod -R 755 "$BUNDLE_DIR"
chmod +x "$BUNDLE_DIR/Contents/MacOS/$APP_NAME"

# Test the app bundle
echo "Testing app bundle..."
if [[ -x "$BUNDLE_DIR/Contents/MacOS/$APP_NAME" ]]; then
    echo "✅ App bundle created successfully!"
    echo "📍 Location: $SCRIPT_DIR/$BUNDLE_DIR"
    echo ""
    echo "🚀 You can now:"
    echo "  1. Double-click the app in Finder"
    echo "  2. Drag it to Applications folder"
    echo "  3. Create shortcuts on Desktop"
    echo ""
    echo "🧪 Test the app:"
    echo "  open '$BUNDLE_DIR'"
else
    echo "❌ Failed to create executable app bundle"
    exit 1
fi
EOF
