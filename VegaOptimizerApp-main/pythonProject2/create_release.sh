#!/bin/bash

# VegaEdge Option Analyzer - Release Creation Script
# This script creates a new release with the built application

echo "🚀 Creating release for VegaEdge Option Analyzer..."

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ Not in a git repository. Please run this from the project root."
    exit 1
fi

# Check if the app exists
if [ ! -d "dist/VegaEdgeOptionAnalyzer.app" ]; then
    echo "❌ Application not found. Please run ./build.sh first."
    exit 1
fi

# Get version from user
read -p "Enter version number (e.g., 1.0.0): " VERSION

if [ -z "$VERSION" ]; then
    echo "❌ Version number is required."
    exit 1
fi

# Create release directory
RELEASE_DIR="release_$VERSION"
mkdir -p "$RELEASE_DIR"

# Copy the app to release directory
echo "📦 Preparing release files..."
cp -r dist/VegaEdgeOptionAnalyzer.app "$RELEASE_DIR/"

# Create a zip file of the app
cd "$RELEASE_DIR"
zip -r "VegaEdgeOptionAnalyzer.app.zip" VegaEdgeOptionAnalyzer.app
cd ..

# Copy the DMG if it exists
if [ -f "dist/VegaEdgeOptionAnalyzer.dmg" ]; then
    cp dist/VegaEdgeOptionAnalyzer.dmg "$RELEASE_DIR/"
fi

# Create release notes
cat > "$RELEASE_DIR/RELEASE_NOTES.md" << EOF
# VegaEdge Option Analyzer v$VERSION

## What's New
- Native macOS application
- Real-time option strategy analysis
- Bullish and Bearish Risk Reversal strategies
- No installation required

## Installation
1. Download \`VegaEdgeOptionAnalyzer.app.zip\` or \`VegaEdgeOptionAnalyzer.dmg\`
2. If using .zip, extract the file
3. Right-click on \`VegaEdgeOptionAnalyzer.app\` and select "Open"
4. Click "Open" when macOS asks for confirmation

## System Requirements
- macOS 10.14 or later
- Intel x64 or Apple Silicon (ARM64)

## Troubleshooting
If the app won't open:
1. Right-click and select "Open"
2. Go to System Preferences > Security & Privacy > General
3. Look for "VegaEdgeOptionAnalyzer" and click "Open Anyway"
EOF

echo "✅ Release files created in $RELEASE_DIR/"
echo ""
echo "📋 Next steps:"
echo "1. Go to https://github.com/Adamj-3x3/VegaAnalyzerMAC/releases"
echo "2. Click 'Create a new release'"
echo "3. Tag version: v$VERSION"
echo "4. Title: VegaEdge Option Analyzer v$VERSION"
echo "5. Upload the files from $RELEASE_DIR/"
echo "6. Publish the release"
echo ""
echo "🎉 Release ready for upload!"
