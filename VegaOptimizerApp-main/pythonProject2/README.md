# VegaEdge Option Analyzer for macOS

A powerful desktop application for analyzing option strategies, specifically designed for macOS. This application provides real-time analysis of Bullish and Bearish Risk Reversal strategies using Yahoo Finance data.

![VegaEdge Option Analyzer](vegaedge_logo.png)

## 🚀 Quick Download

**Ready to use? Download the app directly:**

- **[Download VegaEdge Option Analyzer (.app)](https://github.com/Adamj-3x3/VegaAnalyzerMAC/releases/latest/download/VegaEdgeOptionAnalyzer.app.zip)**
- **[Download VegaEdge Option Analyzer (.dmg)](https://github.com/Adamj-3x3/VegaAnalyzerMAC/releases/latest/download/VegaEdgeOptionAnalyzer.dmg)**

## ✨ Features

- **Native macOS Application**: Built specifically for macOS with proper integration
- **Real-time Analysis**: Analyzes option chains using live Yahoo Finance data
- **Strategy Types**: Supports both Bullish and Bearish Risk Reversal strategies
- **Customizable Parameters**: Set ticker symbol, minimum/maximum days to expiration (DTE)
- **Threaded Processing**: Analysis runs in background to prevent GUI freezing
- **Detailed Reports**: Comprehensive text-based analysis reports
- **No Installation Required**: Single application bundle that runs anywhere

## 📱 How to Use

### Option 1: Download and Run (Recommended)
1. Download the `.app` file or `.dmg` from the releases page
2. If you downloaded the `.app` file, unzip it first
3. **Right-click** on `VegaEdgeOptionAnalyzer.app` and select **"Open"**
4. Click **"Open"** when macOS asks for confirmation
5. The application will launch and you can start analyzing options!

### Option 2: Build from Source
If you want to build the application yourself:

```bash
# Clone the repository
git clone https://github.com/Adamj-3x3/VegaAnalyzerMAC.git
cd VegaAnalyzerMAC

# Make the build script executable
chmod +x build.sh

# Build the application
./build.sh
```

## 🔧 System Requirements

- **macOS**: 10.14 (Mojave) or later
- **Architecture**: Intel x64 or Apple Silicon (ARM64)
- **Memory**: 4GB RAM minimum
- **Storage**: 100MB free space

## 📖 Usage Instructions

1. **Launch the Application**: Double-click the app or right-click and select "Open"
2. **Enter Parameters**:
   - **Ticker Symbol**: Enter the stock symbol (e.g., AAPL, TSLA, SPY)
   - **Min DTE**: Minimum days to expiration (e.g., 30)
   - **Max DTE**: Maximum days to expiration (e.g., 90)
3. **Select Strategy**: Choose between Bullish or Bearish Risk Reversal
4. **Run Analysis**: Click "Analyze" to start the analysis
5. **View Results**: The analysis will appear in the text area below

## 🛠️ Troubleshooting

### App Won't Open
If the app doesn't open when you double-click it:

1. **Right-click** on the app and select **"Open"**
2. If you see a security warning, click **"Open"** again
3. Go to **System Preferences** > **Security & Privacy** > **General**
4. Look for "VegaEdgeOptionAnalyzer" and click **"Open Anyway"**

### Build Issues
If you encounter issues building from source:

```bash
# Install tkinter support (required for GUI)
brew install python-tk

# Make sure you're using Python 3.8+
python3 --version

# Install dependencies
pip3 install -r requirements.txt
```

## 📁 Project Structure

```
VegaAnalyzerMAC/
├── main_app.py              # Main GUI application
├── analysis_engine.py       # Core analysis logic
├── backend_api.py          # API integration
├── build.sh                # macOS build script
├── requirements.txt        # Python dependencies
├── icon.icns              # macOS application icon
├── README.md              # This file
└── dist/                  # Built application
    └── VegaEdgeOptionAnalyzer.app
```

## 🔄 Updates

To get the latest version:
1. Check the [Releases page](https://github.com/Adamj-3x3/VegaAnalyzerMAC/releases)
2. Download the latest `.app` or `.dmg` file
3. Replace your old version with the new one

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## ⚠️ Disclaimer

This application is for educational and informational purposes only. It is not intended as financial advice. Always consult with a qualified financial advisor before making investment decisions.

## 🆘 Support

If you encounter any issues or have questions:
1. Check the [Issues page](https://github.com/Adamj-3x3/VegaAnalyzerMAC/issues)
2. Create a new issue with detailed information about your problem
3. Include your macOS version and any error messages

---

**Made with ❤️ for the options trading community**