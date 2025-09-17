#!/bin/bash

# VegaEdge Option Analyzer - macOS Launcher Script
# This script provides an easy way to run the application

echo "🚀 Starting VegaEdge Option Analyzer..."

# Check if the app exists
if [ ! -d "dist/VegaEdgeOptionAnalyzer.app" ]; then
    echo "❌ Application not found. Please run ./build.sh first."
    exit 1
fi

# Run the application
echo "📱 Launching application..."
open dist/VegaEdgeOptionAnalyzer.app

echo "✅ Application launched successfully!"
echo "   If the app doesn't open, you may need to right-click and select 'Open'"
echo "   due to macOS security restrictions."
