#!/bin/bash

# VegaEdge Option Analyzer - macOS Build Script
# This script creates a standalone macOS application bundle

echo "🚀 Building VegaEdge Option Analyzer for macOS..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "📦 Activating virtual environment..."
source venv/bin/activate

# Install/upgrade required packages
echo "📦 Installing/updating dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create the application bundle using PyInstaller
echo "🔨 Building application bundle..."

# Clean previous builds
rm -rf build/ dist/ *.spec

# Build the application
python -m PyInstaller \
    --onedir \
    --windowed \
    --name="VegaEdgeOptionAnalyzer" \
    --icon=icon.icns \
    --collect-submodules numpy \
    --collect-submodules scipy \
    --collect-submodules customtkinter \
    --collect-submodules PIL \
    --collect-submodules tkinter \
    --add-data="vegaedge_logo.png:." \
    --add-data="icon.ico:." \
    --osx-bundle-identifier="com.vegaedge.optionanalyzer" \
    --target-arch=arm64 \
    --hidden-import=tkinter \
    --hidden-import=tkinter.ttk \
    --hidden-import=tkinter.messagebox \
    --hidden-import=tkinter.filedialog \
    main_app.py

# Check if build was successful
if [ $? -eq 0 ]; then
    echo "✅ Build successful!"
    echo "📱 Application created: dist/VegaEdgeOptionAnalyzer.app"
    echo ""
    echo "To run the application:"
    echo "  open dist/VegaEdgeOptionAnalyzer.app"
    echo ""
    echo "To create a distributable .dmg file, you can use:"
    echo "  hdiutil create -volname 'VegaEdge Option Analyzer' -srcfolder dist/VegaEdgeOptionAnalyzer.app -ov -format UDZO dist/VegaEdgeOptionAnalyzer.dmg"
else
    echo "❌ Build failed. Please check the error messages above."
    exit 1
fi