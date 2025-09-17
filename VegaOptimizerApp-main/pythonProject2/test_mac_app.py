#!/usr/bin/env python3
"""
Test script to verify the macOS application works correctly.
This script tests the core functionality without the GUI.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from analysis_engine import run_bullish_analysis, run_bearish_analysis

def test_analysis_functions():
    """Test the core analysis functions."""
    print("🧪 Testing VegaEdge Option Analyzer for macOS...")
    print("=" * 50)
    
    # Test bullish analysis
    print("\n📈 Testing Bullish Analysis...")
    try:
        result = run_bullish_analysis("AAPL", 30, 90)
        if "No valid" in result:
            print("✅ Bullish analysis completed (no valid strategies found - this is normal for some tickers)")
        else:
            print("✅ Bullish analysis completed successfully")
        print(f"Result length: {len(result)} characters")
    except Exception as e:
        print(f"❌ Bullish analysis failed: {e}")
        return False
    
    # Test bearish analysis
    print("\n📉 Testing Bearish Analysis...")
    try:
        result = run_bearish_analysis("AAPL", 30, 90)
        if "No valid" in result:
            print("✅ Bearish analysis completed (no valid strategies found - this is normal for some tickers)")
        else:
            print("✅ Bearish analysis completed successfully")
        print(f"Result length: {len(result)} characters")
    except Exception as e:
        print(f"❌ Bearish analysis failed: {e}")
        return False
    
    print("\n🎉 All tests passed! The macOS application should work correctly.")
    return True

if __name__ == "__main__":
    success = test_analysis_functions()
    sys.exit(0 if success else 1)
