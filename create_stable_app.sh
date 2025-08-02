#!/bin/bash

# Create a stable, crash-resistant app bundle

set -e

APP_NAME="Zoom Deep Clean Enhanced"
BUNDLE_DIR="$APP_NAME.app"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🔨 Creating stable app bundle..."

# Remove existing bundle
if [[ -d "$BUNDLE_DIR" ]]; then
    echo "Removing existing app bundle..."
    rm -rf "$BUNDLE_DIR"
fi

# Create app bundle structure
echo "Creating app bundle structure..."
mkdir -p "$BUNDLE_DIR/Contents/MacOS"
mkdir -p "$BUNDLE_DIR/Contents/Resources"

# Copy all Python files into the app bundle
echo "Copying Python files..."
cp -r zoom_deep_clean "$BUNDLE_DIR/Contents/Resources/"
cp launch_simple_gui.py "$BUNDLE_DIR/Contents/Resources/"

# Create the main executable script with error handling
echo "Creating stable executable..."
cat > "$BUNDLE_DIR/Contents/MacOS/$APP_NAME" << 'EOF'
#!/bin/bash

# Stable launcher with comprehensive error handling

# Get paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUNDLE_DIR="$(dirname "$SCRIPT_DIR")"
RESOURCES_DIR="$BUNDLE_DIR/Resources"

# Create debug log
DEBUG_LOG="/tmp/zoom_app_debug.log"
echo "=== App Launch $(date) ===" >> "$DEBUG_LOG"
echo "Script dir: $SCRIPT_DIR" >> "$DEBUG_LOG"
echo "Bundle dir: $BUNDLE_DIR" >> "$DEBUG_LOG"
echo "Resources dir: $RESOURCES_DIR" >> "$DEBUG_LOG"

# Function to show error dialog
show_error() {
    local message="$1"
    echo "ERROR: $message" >> "$DEBUG_LOG"
    osascript -e "display dialog \"$message\" buttons {\"OK\"} default button \"OK\" with icon stop"
}

# Check if resources directory exists
if [[ ! -d "$RESOURCES_DIR" ]]; then
    show_error "App bundle is corrupted. Resources directory not found."
    exit 1
fi

# Change to resources directory
cd "$RESOURCES_DIR" || {
    show_error "Cannot access app resources directory."
    exit 1
}

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    show_error "Python 3 is required but not installed. Please install Python 3 from python.org or using Homebrew."
    exit 1
fi

echo "Python 3 found: $(which python3)" >> "$DEBUG_LOG"

# Check if tkinter is available
if ! python3 -c "import tkinter" 2>>"$DEBUG_LOG"; then
    show_error "tkinter GUI library is required but not available. Please install it using: brew install python-tk"
    exit 1
fi

echo "tkinter available" >> "$DEBUG_LOG"

# Check if our GUI module exists
if [[ ! -f "launch_simple_gui.py" ]]; then
    show_error "GUI launcher not found in app bundle."
    exit 1
fi

echo "GUI launcher found" >> "$DEBUG_LOG"

# Set up Python path
export PYTHONPATH="$RESOURCES_DIR:$PYTHONPATH"
echo "PYTHONPATH: $PYTHONPATH" >> "$DEBUG_LOG"

# Launch the GUI with error handling
echo "Launching GUI..." >> "$DEBUG_LOG"
if python3 launch_simple_gui.py 2>>"$DEBUG_LOG"; then
    echo "GUI launched successfully" >> "$DEBUG_LOG"
else
    echo "GUI launch failed" >> "$DEBUG_LOG"
    show_error "Failed to launch GUI. Check debug log at $DEBUG_LOG for details."
fi
EOF

# Make the executable script executable
chmod +x "$BUNDLE_DIR/Contents/MacOS/$APP_NAME"

# Create Info.plist with compatibility settings
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
    <string>10.12</string>
    <key>NSHighResolutionCapable</key>
    <true/>
    <key>LSApplicationCategoryType</key>
    <string>public.app-category.utilities</string>
    <key>NSHumanReadableCopyright</key>
    <string>© 2025 PHLthy215. All rights reserved.</string>
    <key>LSUIElement</key>
    <false/>
</dict>
</plist>
EOF

# Set proper permissions
echo "Setting permissions..."
chmod -R 755 "$BUNDLE_DIR"
chmod +x "$BUNDLE_DIR/Contents/MacOS/$APP_NAME"

echo "✅ Stable app bundle created successfully!"
echo "📍 Location: $SCRIPT_DIR/$BUNDLE_DIR"
echo ""
echo "🧪 Test the stable app:"
echo "  open '$BUNDLE_DIR'"
