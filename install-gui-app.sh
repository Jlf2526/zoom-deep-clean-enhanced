#!/bin/bash

# Zoom Deep Clean Enhanced - GUI App Installation Script
# VM-Aware & System-Wide cleanup utility with user-friendly interface
# Created by: PHLthy215
# Enhanced Version: 2.2.0

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="$HOME/Documents/zoom_deep_clean_gui_install.log"
APP_NAME="Zoom Deep Clean Enhanced.app"
INSTALL_DIR="/Applications"

# Logging function
log() {
    echo -e "${CYAN}[$(date '+%Y-%m-%d %H:%M:%S')]${NC} $1" | tee -a "$LOG_FILE"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1" | tee -a "$LOG_FILE"
}

success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1" | tee -a "$LOG_FILE"
}

warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1" | tee -a "$LOG_FILE"
}

info() {
    echo -e "${BLUE}[INFO]${NC} $1" | tee -a "$LOG_FILE"
}

# Check if running on macOS
check_macos() {
    if [[ "$OSTYPE" != "darwin"* ]]; then
        error "This GUI app is designed for macOS only"
        exit 1
    fi
    success "macOS detected"
}

# Check Python and tkinter
check_python_gui() {
    if ! command -v python3 &> /dev/null; then
        error "Python 3 is required but not installed"
        exit 1
    fi
    
    PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    info "Python version: $PYTHON_VERSION"
    
    # Check if version is >= 3.7
    if python3 -c 'import sys; exit(0 if sys.version_info >= (3, 7) else 1)'; then
        success "Python version is compatible"
    else
        error "Python 3.7 or higher is required"
        exit 1
    fi
    
    # Check tkinter availability
    if python3 -c "import tkinter" 2>/dev/null; then
        success "tkinter GUI library available"
    else
        error "tkinter GUI library not available"
        echo "Please install tkinter:"
        echo "  brew install python-tk"
        exit 1
    fi
}

# Install the package
install_package() {
    info "Installing Zoom Deep Clean Enhanced with GUI support..."
    
    cd "$SCRIPT_DIR"
    
    # Create virtual environment for the app
    if [[ ! -d "gui_env" ]]; then
        python3 -m venv gui_env
        success "Created virtual environment"
    fi
    
    # Activate virtual environment and install
    source gui_env/bin/activate
    
    if pip install -e . >> "$LOG_FILE" 2>&1; then
        success "Package installed successfully in virtual environment"
    else
        error "Package installation failed"
        exit 1
    fi
    
    # Update the app launcher to use the virtual environment
    cat > "$APP_NAME/Contents/MacOS/zoom_deep_clean_gui" << 'EOF'
#!/bin/bash

# Zoom Deep Clean Enhanced - macOS App Launcher with Virtual Environment
# Created by: PHLthy215

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"

# Activate virtual environment
source "$APP_DIR/gui_env/bin/activate"

# Set up Python path
export PYTHONPATH="$APP_DIR:$PYTHONPATH"

# Change to app directory
cd "$APP_DIR"

# Launch the GUI application
python3 launch_gui.py
EOF
    
    chmod +x "$APP_NAME/Contents/MacOS/zoom_deep_clean_gui"
    success "Updated app launcher with virtual environment"
}

# Install app to Applications folder
install_to_applications() {
    info "Installing app to Applications folder..."
    
    # Remove existing app if present
    if [[ -d "$INSTALL_DIR/$APP_NAME" ]]; then
        warning "Removing existing app installation"
        rm -rf "$INSTALL_DIR/$APP_NAME"
    fi
    
    # Copy app to Applications
    if cp -R "$SCRIPT_DIR/$APP_NAME" "$INSTALL_DIR/"; then
        success "App installed to $INSTALL_DIR/$APP_NAME"
    else
        error "Failed to install app to Applications folder"
        exit 1
    fi
    
    # Set proper permissions
    chmod -R 755 "$INSTALL_DIR/$APP_NAME"
    success "Set proper permissions"
}

# Create desktop shortcut
create_desktop_shortcut() {
    info "Creating desktop shortcut..."
    
    DESKTOP_DIR="$HOME/Desktop"
    SHORTCUT_PATH="$DESKTOP_DIR/$APP_NAME"
    
    if [[ -d "$DESKTOP_DIR" ]]; then
        # Create symbolic link to Applications
        if ln -sf "$INSTALL_DIR/$APP_NAME" "$SHORTCUT_PATH" 2>/dev/null; then
            success "Desktop shortcut created"
        else
            warning "Could not create desktop shortcut"
        fi
    else
        warning "Desktop directory not found"
    fi
}

# Test the installation
test_installation() {
    info "Testing GUI application..."
    
    # Test command line version
    if "$INSTALL_DIR/$APP_NAME/Contents/MacOS/zoom_deep_clean_gui" --help &>/dev/null; then
        success "Command line interface working"
    else
        warning "Command line interface test failed"
    fi
    
    info "GUI app installation complete!"
}

# Show completion message
show_completion() {
    echo ""
    echo -e "${PURPLE}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${PURPLE}║        ZOOM DEEP CLEAN ENHANCED GUI - INSTALLED!            ║${NC}"
    echo -e "${PURPLE}║                    v2.2.0 by PHLthy215                      ║${NC}"
    echo -e "${PURPLE}╚══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${GREEN}🎉 Installation completed successfully!${NC}"
    echo ""
    echo -e "${CYAN}How to use:${NC}"
    echo "  1. 📱 Double-click the app in Applications folder"
    echo "  2. 🖥️ Or use the desktop shortcut (if created)"
    echo "  3. 🔍 Always run Preview Mode first to see what will be changed"
    echo "  4. ⚙️ Configure advanced features as needed"
    echo "  5. 🔥 Run cleanup when ready"
    echo ""
    echo -e "${CYAN}App locations:${NC}"
    echo "  📁 Main app: $INSTALL_DIR/$APP_NAME"
    if [[ -L "$HOME/Desktop/$APP_NAME" ]]; then
        echo "  🖥️ Desktop shortcut: $HOME/Desktop/$APP_NAME"
    fi
    echo "  📋 Installation log: $LOG_FILE"
    echo ""
    echo -e "${YELLOW}⚠️ Important:${NC}"
    echo "  • Always backup important data before cleanup"
    echo "  • Test with Preview Mode first"
    echo "  • Advanced features require admin privileges"
    echo "  • MAC spoofing should only be used in VM environments"
    echo ""
    
    read -p "Would you like to launch the app now? (y/n): " -r
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        info "Launching Zoom Deep Clean Enhanced GUI..."
        open "$INSTALL_DIR/$APP_NAME"
    fi
}

# Main execution
main() {
    echo -e "${PURPLE}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${PURPLE}║      ZOOM DEEP CLEAN ENHANCED GUI INSTALLER v2.2.0          ║${NC}"
    echo -e "${PURPLE}║              VM-Aware & System-Wide                          ║${NC}"
    echo -e "${PURPLE}║                Created by: PHLthy215                         ║${NC}"
    echo -e "${PURPLE}╚══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    
    log "Starting Zoom Deep Clean Enhanced GUI installation"
    
    # Pre-flight checks
    check_macos
    check_python_gui
    
    # Install and setup
    install_package
    install_to_applications
    create_desktop_shortcut
    test_installation
    
    # Show completion
    show_completion
    
    success "GUI installation completed successfully!"
}

# Handle interrupts gracefully
trap 'echo -e "\n${YELLOW}Installation interrupted by user${NC}"; exit 130' INT TERM

# Run main function
main "$@"
