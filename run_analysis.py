#!/usr/bin/env python3
"""
Standalone script to run options analysis
Usage: python run_analysis.py <strategy_type> <ticker> <min_dte> <max_dte>
"""

import sys
import os

# Add the api directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'api', 'analyze'))

from analysis_engine import run_bullish_analysis, run_bearish_analysis

def main():
    if len(sys.argv) != 5:
        print("Usage: python run_analysis.py <strategy_type> <ticker> <min_dte> <max_dte>")
        sys.exit(1)
    
    strategy_type = sys.argv[1].lower()
    ticker = sys.argv[2].upper()
    min_dte = int(sys.argv[3])
    max_dte = int(sys.argv[4])
    
    try:
        if strategy_type == 'bullish':
            result = run_bullish_analysis(ticker, min_dte, max_dte)
        elif strategy_type == 'bearish':
            result = run_bearish_analysis(ticker, min_dte, max_dte)
        else:
            print(f"Error: Unknown strategy type '{strategy_type}'. Use 'bullish' or 'bearish'.")
            sys.exit(1)
        
        print(result)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
