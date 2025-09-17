# macOS Setup Guide for VegaEdge Option Analyzer

## Overview
This guide explains how to run the VegaEdge Option Analyzer on macOS. The application has been successfully adapted from Windows to work natively on macOS.

## What Was Changed

### 1. Build System
- **Windows**: `build.bat` (batch file)
- **macOS**: `build.sh` (shell script)
- **Icon**: Converted from `.ico` to `.icns` format
- **Architecture**: Optimized for ARM64 (Apple Silicon)

### 2. Dependencies
- Updated `requirements.txt` for macOS compatibility
- Added Pillow for image processing
- Used virtual environment to avoid system package conflicts

### 3. PyInstaller Configuration
- Added macOS-specific flags (`--osx-bundle-identifier`)
- Used ARM64 architecture instead of universal2
- Proper icon handling for macOS

## Quick Start

### Prerequisites
- macOS 10.14 or later
- Python 3.8 or higher
- Internet connection for data fetching

### Installation & Build

1. **Clone/Download the project**
   ```bash
   cd /path/to/VegaOptimizerApp-main/pythonProject2
   ```

2. **Set up virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Build the application**
   ```bash
   chmod +x build.sh
   ./build.sh
   ```

5. **Run the application**
   ```bash
   open dist/VegaEdgeOptionAnalyzer.app
   ```

## Files Created/Modified

### New Files
- `build.sh` - macOS build script
- `icon.icns` - macOS application icon
- `test_mac_app.py` - Test script for macOS functionality
- `MACOS_SETUP.md` - This guide

### Modified Files
- `requirements.txt` - Updated for macOS compatibility
- `README.md` - Added macOS instructions

## Application Features

The macOS version includes all the same features as the Windows version:

- **Real-time Analysis**: Analyzes option chains using Yahoo Finance data
- **Strategy Types**: Supports both Bullish and Bearish Risk Reversal strategies
- **Customizable Parameters**: Set ticker symbol, minimum/maximum days to expiration (DTE)
- **Threaded Processing**: Analysis runs in background to prevent GUI freezing
- **Detailed Reports**: Comprehensive text-based analysis reports
- **Native GUI**: Uses CustomTkinter for a modern, native macOS interface

## Troubleshooting

### Common Issues

1. **"App can't be opened because it is from an unidentified developer"**
   - Right-click the app and select "Open"
   - Or go to System Preferences > Security & Privacy > General and click "Open Anyway"

2. **Build fails with architecture errors**
   - Make sure you're using the correct architecture (ARM64 for Apple Silicon)
   - Check that all dependencies are installed in the virtual environment

3. **Tkinter issues**
   - The app uses CustomTkinter which should work on macOS
   - If you encounter GUI issues, try running the test script first

### Testing
Run the test script to verify functionality:
```bash
source venv/bin/activate
python3 test_mac_app.py
```

## Distribution

### Creating a DMG
To create a distributable .dmg file:
```bash
hdiutil create -volname 'VegaEdge Option Analyzer' -srcfolder dist/VegaEdgeOptionAnalyzer.app -ov -format UDZO dist/VegaEdgeOptionAnalyzer.dmg
```

### Distribution Notes
- The `.app` bundle can be distributed to any macOS computer
- No Python installation required on target machines
- Users may need to allow the app to run due to macOS security restrictions

## Technical Details

### Build Process
1. Creates virtual environment
2. Installs all dependencies
3. Converts Windows icon to macOS format
4. Builds application bundle using PyInstaller
5. Signs the application for macOS

### Architecture
- **Target**: ARM64 (Apple Silicon)
- **Bundle**: Native macOS .app bundle
- **Dependencies**: All included in the bundle
- **Size**: ~60MB (includes all Python libraries)

## Support

The macOS version maintains full compatibility with the original Windows functionality while providing a native macOS experience. All analysis features, data sources, and user interface elements work identically across both platforms.
