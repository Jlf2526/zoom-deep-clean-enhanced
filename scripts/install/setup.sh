#!/bin/bash

# Zoom Deep Clean Enhanced - Automated Setup Script
# Version 2.2.0 - VM-Aware & System-Wide
# Created by: PHLthy215

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
LOG_FILE="$SCRIPT_DIR/setup.log"
VENV_DIR="$SCRIPT_DIR/venv"

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

# Header
show_header() {
    echo -e "${PURPLE}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${PURPLE}║        ZOOM DEEP CLEAN ENHANCED SETUP v2.2.0                ║${NC}"
    echo -e "${PURPLE}║              VM-Aware & System-Wide                          ║${NC}"
    echo -e "${PURPLE}║                Created by: PHLthy215                         ║${NC}"
    echo -e "${PURPLE}╚══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

# Check system requirements
check_requirements() {
    log "Checking system requirements..."
    
    # Check macOS
    if [[ "$OSTYPE" != "darwin"* ]]; then
        error "This tool is designed for macOS only"
        exit 1
    fi
    success "macOS detected"
    
    # Check Python
    if ! command -v python3 &> /dev/null; then
        error "Python 3 is required but not installed"
        echo "Please install Python 3 from python.org or using Homebrew"
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
    
    # Check tkinter
    if python3 -c "import tkinter" 2>/dev/null; then
        success "tkinter GUI library available"
    else
        warning "tkinter GUI library not available"
        echo "To install tkinter: brew install python-tk"
        echo "GUI features will be limited without tkinter"
    fi
}

# Create virtual environment
setup_venv() {
    log "Setting up virtual environment..."
    
    if [[ -d "$VENV_DIR" ]]; then
        warning "Virtual environment already exists, removing..."
        rm -rf "$VENV_DIR"
    fi
    
    python3 -m venv "$VENV_DIR"
    success "Virtual environment created"
    
    # Activate virtual environment
    source "$VENV_DIR/bin/activate"
    success "Virtual environment activated"
    
    # Upgrade pip
    pip install --upgrade pip >> "$LOG_FILE" 2>&1
    success "pip upgraded"
}

# Install package
install_package() {
    log "Installing Zoom Deep Clean Enhanced package..."
    
    # Install in development mode
    if pip install -e . >> "$LOG_FILE" 2>&1; then
        success "Package installed successfully"
    else
        error "Package installation failed"
        echo "Check $LOG_FILE for details"
        exit 1
    fi
    
    # Verify installation
    if zoom-deep-clean-enhanced --version >> "$LOG_FILE" 2>&1; then
        success "Package verification successful"
    else
        warning "Package verification failed, but installation may still work"
    fi
}

# Set up permissions
setup_permissions() {
    log "Setting up file permissions..."
    
    # Make scripts executable
    chmod +x *.sh 2>/dev/null || true
    chmod +x *.py 2>/dev/null || true
    chmod +x *.command 2>/dev/null || true
    
    success "File permissions set"
}

# Create desktop launcher
create_desktop_launcher() {
    log "Creating desktop launcher..."
    
    DESKTOP_DIR="$HOME/Desktop"
    LAUNCHER_PATH="$DESKTOP_DIR/ZoomCleanGUI.command"
    
    if [[ -d "$DESKTOP_DIR" ]]; then
        cat > "$LAUNCHER_PATH" << EOF
#!/bin/bash
cd "$SCRIPT_DIR"
source venv/bin/activate
python3 launch_terminal_gui.py
EOF
        chmod +x "$LAUNCHER_PATH"
        success "Desktop launcher created: $LAUNCHER_PATH"
    else
        warning "Desktop directory not found, skipping launcher creation"
    fi
}

# Test installation
test_installation() {
    log "Testing installation..."
    
    # Test Python imports
    if python3 -c "
import sys
sys.path.insert(0, 'zoom_deep_clean')
from zoom_deep_clean.cleaner_enhanced import ZoomDeepCleanerEnhanced
from zoom_deep_clean.advanced_features import AdvancedFeatures
print('✅ All imports successful')
" 2>/dev/null; then
        success "Python imports working"
    else
        warning "Python import test failed"
    fi
    
    # Test CLI
    if zoom-deep-clean-enhanced --help > /dev/null 2>&1; then
        success "CLI interface working"
    else
        warning "CLI interface test failed"
    fi
    
    # Test GUI imports
    if python3 -c "
import sys
sys.path.insert(0, 'zoom_deep_clean')
from zoom_deep_clean.gui_simple import SimpleZoomCleanerGUI
print('✅ GUI imports successful')
" 2>/dev/null; then
        success "GUI imports working"
    else
        warning "GUI import test failed"
    fi
}

# Show completion message
show_completion() {
    echo ""
    echo -e "${PURPLE}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${PURPLE}║                    SETUP COMPLETE!                          ║${NC}"
    echo -e "${PURPLE}║        Zoom Deep Clean Enhanced v2.2.0 Ready to Use         ║${NC}"
    echo -e "${PURPLE}╚══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${GREEN}🎉 Installation completed successfully!${NC}"
    echo ""
    echo -e "${CYAN}🚀 How to use:${NC}"
    echo ""
    echo -e "${YELLOW}GUI Interface (Recommended):${NC}"
    echo "  python3 launch_terminal_gui.py"
    echo ""
    echo -e "${YELLOW}Desktop Launcher:${NC}"
    if [[ -f "$HOME/Desktop/ZoomCleanGUI.command" ]]; then
        echo "  Double-click: ~/Desktop/ZoomCleanGUI.command"
    else
        echo "  Not created (Desktop folder not found)"
    fi
    echo ""
    echo -e "${YELLOW}Command Line Interface:${NC}"
    echo "  source venv/bin/activate"
    echo "  zoom-deep-clean-enhanced --help"
    echo "  zoom-deep-clean-enhanced --dry-run --verbose"
    echo ""
    echo -e "${CYAN}📚 Documentation:${NC}"
    echo "  • Setup Guide: SETUP_GUIDE.md"
    echo "  • Main Documentation: README.md"
    echo "  • Advanced Features: ADVANCED_FEATURES.md"
    echo "  • Usage Guide: USAGE_GUIDE.md"
    echo "  • Troubleshooting: CRASH_FIX_GUIDE.md"
    echo ""
    echo -e "${CYAN}🛡️ Safety Reminders:${NC}"
    echo "  • Always start with Preview Mode (--dry-run)"
    echo "  • Test advanced features in VM environments first"
    echo "  • Backup important data before cleanup"
    echo "  • Read all output messages carefully"
    echo ""
    echo -e "${GREEN}✅ Ready to clean Zoom fingerprints safely and effectively!${NC}"
    echo ""
    
    # Offer to launch GUI
    read -p "Would you like to launch the GUI now? (y/n): " -r
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        log "Launching GUI..."
        python3 launch_terminal_gui.py &
        success "GUI launched in background"
    fi
}

# Main execution
main() {
    show_header
    log "Starting Zoom Deep Clean Enhanced setup"
    
    # Setup steps
    check_requirements
    setup_venv
    install_package
    setup_permissions
    create_desktop_launcher
    test_installation
    
    # Show completion
    show_completion
    
    success "Setup completed successfully!"
}

# Handle interrupts gracefully
trap 'echo -e "\n${YELLOW}Setup interrupted by user${NC}"; exit 130' INT TERM

# Run main function
main "$@"
