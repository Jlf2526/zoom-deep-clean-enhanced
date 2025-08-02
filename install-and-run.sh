#!/bin/bash

# Zoom Deep Clean Enhanced - Installation and Execution Script
# VM-Aware & System-Wide cleanup utility
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
LOG_FILE="$HOME/Documents/zoom_deep_clean_enhanced_install.log"
DRY_RUN_LOG="$HOME/Documents/zoom_clean_enhanced_dry_run.log"

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
        error "This script is designed for macOS only"
        exit 1
    fi
    success "macOS detected"
}

# Check Python version
check_python() {
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
}

# Check sudo access
check_sudo() {
    info "Checking sudo access..."
    if sudo -n true 2>/dev/null; then
        success "Sudo access available"
    else
        warning "Sudo access not available - some operations may fail"
        echo "Please run 'sudo -v' to cache credentials if needed"
    fi
}

# Detect VM software
detect_vm_software() {
    info "Detecting VM software..."
    
    VM_DETECTED=false
    
    # Check for VMware Fusion
    if [[ -d "/Applications/VMware Fusion.app" ]] || command -v vmware &> /dev/null; then
        success "VMware Fusion detected"
        VM_DETECTED=true
    fi
    
    # Check for VirtualBox
    if [[ -d "/Applications/VirtualBox.app" ]] || command -v VBoxManage &> /dev/null; then
        success "VirtualBox detected"
        VM_DETECTED=true
    fi
    
    # Check for Parallels Desktop
    if [[ -d "/Applications/Parallels Desktop.app" ]] || command -v prlctl &> /dev/null; then
        success "Parallels Desktop detected"
        VM_DETECTED=true
    fi
    
    if [[ "$VM_DETECTED" == "false" ]]; then
        info "No VM software detected - VM-aware features will be available but not utilized"
    fi
}

# Install the enhanced package
install_package() {
    info "Installing Zoom Deep Clean Enhanced..."
    
    cd "$SCRIPT_DIR"
    
    # Install in development mode for local usage
    if pip3 install -e . >> "$LOG_FILE" 2>&1; then
        success "Package installed successfully"
    else
        error "Package installation failed"
        exit 1
    fi
}

# Run dry-run first
run_dry_run() {
    info "Running dry-run to preview operations..."
    
    echo -e "${PURPLE}========================================${NC}"
    echo -e "${PURPLE}  ZOOM DEEP CLEAN ENHANCED - DRY RUN   ${NC}"
    echo -e "${PURPLE}     WITH ADVANCED FEATURES            ${NC}"
    echo -e "${PURPLE}========================================${NC}"
    
    if zoom-deep-clean-enhanced --dry-run --verbose --vm-aware --enable-advanced-features > "$DRY_RUN_LOG" 2>&1; then
        success "Dry-run completed successfully"
        info "Dry-run log saved to: $DRY_RUN_LOG"
    else
        warning "Dry-run completed with warnings - check log file"
    fi
    
    echo ""
    echo -e "${CYAN}Dry-run summary:${NC}"
    tail -30 "$DRY_RUN_LOG" | grep -E "(DRY RUN|Statistics|Files|Directories|Processes|Advanced|Keychain|MDM|UUID)" || true
}

# Get user confirmation
get_confirmation() {
    echo ""
    echo -e "${RED}⚠️  FINAL WARNING ⚠️${NC}"
    echo -e "${YELLOW}This will perform a comprehensive system-wide cleanup including:${NC}"
    echo "  • Stopping all VM services (VMware, VirtualBox, Parallels)"
    echo "  • Terminating all Zoom processes (including VM instances)"
    echo "  • Removing all Zoom files, preferences, and system integration"
    echo "  • Cleaning keychain entries and authentication data"
    echo "  • Performing comprehensive file system search"
    echo "  • Creating backups of removed files"
    echo ""
    echo -e "${CYAN}Advanced fingerprint features will:${NC}"
    echo "  • Scan keychain comprehensively for Zoom-related entries"
    echo "  • Detect MDM profiles and management enrollment"
    echo "  • Identify system UUIDs and hardware identifiers"
    echo "  • Optionally reset hostname and spoof MAC addresses"
    echo ""
    echo -e "${CYAN}After cleanup you will need to:${NC}"
    echo "  1. Restart your computer"
    echo "  2. Restart any VMs you were using"
    echo "  3. Reinstall Zoom completely"
    echo ""
    
    read -p "Do you want to proceed with the enhanced cleanup? (yes/no): " -r
    if [[ ! $REPLY =~ ^[Yy][Ee][Ss]$|^[Yy]$ ]]; then
        info "Operation cancelled by user"
        exit 0
    fi
}

# Run the actual cleanup
run_cleanup() {
    info "Starting enhanced Zoom cleanup..."
    
    echo -e "${PURPLE}============================================${NC}"
    echo -e "${PURPLE}  ZOOM DEEP CLEAN ENHANCED - EXECUTING   ${NC}"
    echo -e "${PURPLE}============================================${NC}"
    
    # Stop VMs first (integrated into the cleaner, but also do it here for safety)
    info "Stopping VM services..."
    sudo launchctl stop com.vmware.fusion 2>/dev/null || true
    sudo launchctl stop org.virtualbox.app.VBoxSVC 2>/dev/null || true
    sudo launchctl stop com.parallels.desktop.launchdaemon 2>/dev/null || true
    sleep 3
    
    # Run the enhanced cleaner with advanced features
    if zoom-deep-clean-enhanced --verbose --force --vm-aware --enable-advanced-features; then
        success "Enhanced cleanup with advanced features completed successfully!"
    else
        error "Enhanced cleanup completed with errors - check log files"
        return 1
    fi
}

# Verify cleanup results
verify_cleanup() {
    info "Verifying cleanup results..."
    
    echo -e "${CYAN}Searching for remaining Zoom files...${NC}"
    
    REMAINING_FILES=()
    
    # Search in common locations
    while IFS= read -r -d '' file; do
        REMAINING_FILES+=("$file")
    done < <(find /Users -iname "*zoom*" -type f -print0 2>/dev/null || true)
    
    while IFS= read -r -d '' file; do
        REMAINING_FILES+=("$file")
    done < <(find /Library -iname "*zoom*" -type f -print0 2>/dev/null || true)
    
    if [[ ${#REMAINING_FILES[@]} -eq 0 ]]; then
        success "No remaining Zoom files found!"
    else
        warning "Found ${#REMAINING_FILES[@]} remaining Zoom files:"
        for file in "${REMAINING_FILES[@]:0:10}"; do  # Show first 10
            echo "  📄 $file"
        done
        if [[ ${#REMAINING_FILES[@]} -gt 10 ]]; then
            echo "  ... and $((${#REMAINING_FILES[@]} - 10)) more files"
        fi
    fi
    
    # Check for remaining processes
    if pgrep -f "[Zz]oom" > /dev/null 2>&1; then
        warning "Some Zoom processes are still running:"
        pgrep -f "[Zz]oom" | while read -r pid; do
            ps -p "$pid" -o pid,comm,args 2>/dev/null || true
        done
    else
        success "No Zoom processes running"
    fi
}

# Offer system reboot
offer_reboot() {
    echo ""
    echo -e "${GREEN}🎉 Enhanced cleanup process completed!${NC}"
    echo ""
    echo -e "${CYAN}Generated files:${NC}"
    echo "  📋 Installation log: $LOG_FILE"
    echo "  📋 Dry-run log: $DRY_RUN_LOG"
    echo "  📋 Cleanup log: $HOME/Documents/zoom_deep_clean_enhanced.log"
    echo "  📊 Cleanup report: $HOME/Documents/zoom_cleanup_enhanced_report.json"
    echo ""
    echo -e "${YELLOW}Recommended next steps:${NC}"
    echo "  1. Review the cleanup logs and report"
    echo "  2. Restart your computer to complete the cleanup"
    echo "  3. Restart any VMs you plan to use"
    echo "  4. Download and install a fresh copy of Zoom"
    echo ""
    
    read -p "Would you like to reboot the system now? (yes/no): " -r
    if [[ $REPLY =~ ^[Yy][Ee][Ss]$|^[Yy]$ ]]; then
        info "Initiating system reboot in 10 seconds..."
        echo "Press Ctrl+C to cancel..."
        sleep 10
        sudo reboot
    else
        info "Please remember to reboot manually when convenient"
    fi
}

# Main execution
main() {
    echo -e "${PURPLE}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${PURPLE}║           ZOOM DEEP CLEAN ENHANCED v2.2.0                   ║${NC}"
    echo -e "${PURPLE}║              VM-Aware & System-Wide                          ║${NC}"
    echo -e "${PURPLE}║                Created by: PHLthy215                         ║${NC}"
    echo -e "${PURPLE}╚══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    
    log "Starting Zoom Deep Clean Enhanced installation and execution"
    
    # Pre-flight checks
    check_macos
    check_python
    check_sudo
    detect_vm_software
    
    # Install and run
    install_package
    run_dry_run
    get_confirmation
    
    if run_cleanup; then
        verify_cleanup
        offer_reboot
    else
        error "Cleanup failed - check log files for details"
        exit 1
    fi
    
    success "All operations completed successfully!"
}

# Handle interrupts gracefully
trap 'echo -e "\n${YELLOW}Operation interrupted by user${NC}"; exit 130' INT TERM

# Run main function
main "$@"
