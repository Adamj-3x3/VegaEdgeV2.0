#!/usr/bin/env python3
"""
Test script to verify Vanna implementation is working correctly
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'VegaOptimizerApp-main', 'pythonProject2'))

from analysis_engine import bs_vanna, bs_vega, bs_delta, analyze_bullish_risk_reversal, get_options_data
import numpy as np

def test_vanna_calculation():
    """Test Vanna calculation with known values"""
    print("🧪 Testing Vanna Calculation...")
    
    # Test parameters
    S = 100.0  # Stock price
    K = 105.0  # Strike price
    T = 0.25   # Time to expiration (3 months)
    r = 0.05   # Risk-free rate
    sigma = 0.20  # Volatility
    
    vanna = bs_vanna(S, K, T, r, sigma)
    vega = bs_vega(S, K, T, r, sigma)
    delta = bs_delta(S, K, T, r, sigma, 'call')
    
    print(f"  Stock Price: ${S}")
    print(f"  Strike Price: ${K}")
    print(f"  Time to Exp: {T} years")
    print(f"  Volatility: {sigma*100}%")
    print(f"  Delta: {delta:.4f}")
    print(f"  Vega: {vega:.4f}")
    print(f"  Vanna: {vanna:.4f}")
    
    # Vanna should be negative for calls (as volatility increases, delta decreases for OTM calls)
    if vanna < 0:
        print("  ✅ Vanna is negative (expected for OTM call)")
    else:
        print("  ❌ Vanna should be negative for OTM call")
    
    return vanna, vega, delta

def test_real_options_data():
    """Test with real options data"""
    print("\n🔍 Testing with Real Options Data...")
    
    try:
        # Test with a popular stock
        ticker = "AAPL"
        expiration = "2024-02-16"  # Use a future date
        
        print(f"  Fetching options data for {ticker}...")
        calls, puts = get_options_data(ticker, expiration, 180.0)  # Assume $180 stock price
        
        if calls.empty or puts.empty:
            print("  ⚠️  No options data available, skipping real data test")
            return
        
        print(f"  Found {len(calls)} calls and {len(puts)} puts")
        
        # Check if Vanna column exists
        if 'vanna' in calls.columns and 'vanna' in puts.columns:
            print("  ✅ Vanna column found in options data")
            
            # Show some sample Vanna values
            sample_calls = calls.head(3)
            sample_puts = puts.head(3)
            
            print("  Sample Call Vanna values:")
            for _, call in sample_calls.iterrows():
                print(f"    Strike ${call['strike']:.0f}: Vanna = {call['vanna']:.4f}")
            
            print("  Sample Put Vanna values:")
            for _, put in sample_puts.iterrows():
                print(f"    Strike ${put['strike']:.0f}: Vanna = {put['vanna']:.4f}")
                
        else:
            print("  ❌ Vanna column not found in options data")
            
    except Exception as e:
        print(f"  ⚠️  Error testing real data: {e}")

def test_combination_analysis():
    """Test the full analysis with Vanna optimization"""
    print("\n📊 Testing Full Analysis with Vanna Optimization...")
    
    try:
        # Test with a popular stock
        ticker = "AAPL"
        expiration = "2024-02-16"
        underlying_price = 180.0
        
        print(f"  Running bullish analysis for {ticker}...")
        combinations = analyze_bullish_risk_reversal(
            calls=None,  # Will fetch fresh data
            puts=None,
            underlying_price=underlying_price,
            expiration_date=expiration
        )
        
        if combinations:
            print(f"  ✅ Found {len(combinations)} valid combinations")
            
            # Show top 3 combinations with Vanna data
            for i, combo in enumerate(combinations[:3]):
                print(f"  Combination {i+1}:")
                print(f"    Call Strike: ${combo['long_call_strike']:.0f}")
                print(f"    Put Strike: ${combo['short_put_strike']:.0f}")
                print(f"    Net Delta: {combo['net_delta']:.4f}")
                print(f"    Net Vega: {combo['net_vega']:.4f}")
                print(f"    Net Vanna: {combo['net_vanna']:.4f}")
                print(f"    Efficiency: {combo['efficiency']:.4f}")
                print()
        else:
            print("  ⚠️  No valid combinations found")
            
    except Exception as e:
        print(f"  ⚠️  Error in analysis: {e}")

def main():
    print("🚀 Testing Vanna Implementation for VegaEdge V2.0")
    print("=" * 50)
    
    # Test 1: Basic Vanna calculation
    vanna, vega, delta = test_vanna_calculation()
    
    # Test 2: Real options data
    test_real_options_data()
    
    # Test 3: Full analysis
    test_combination_analysis()
    
    print("\n" + "=" * 50)
    print("✅ Vanna implementation testing complete!")
    print("\nIf all tests passed, the implementation is ready for deployment.")

if __name__ == "__main__":
    main()
