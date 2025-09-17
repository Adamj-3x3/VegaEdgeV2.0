import type { NextApiRequest, NextApiResponse } from 'next';

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { ticker, min_dte, max_dte } = req.body;

    // Validate input
    if (!ticker || !min_dte || !max_dte) {
      return res.status(400).json({ error: 'Missing required parameters' });
    }

    // Call Python script directly
    const { spawn } = await import('child_process');
    const path = await import('path');
    
    return new Promise((resolve) => {
      const pythonProcess = spawn('python3', [
        path.default.join(process.cwd(), 'run_analysis.py'),
        'bearish',
        ticker,
        min_dte.toString(),
        max_dte.toString()
      ]);
      
      let result = '';
      let error = '';
      
      pythonProcess.stdout.on('data', (data: Buffer) => {
        result += data.toString();
      });
      
      pythonProcess.stderr.on('data', (data: Buffer) => {
        error += data.toString();
      });
      
      pythonProcess.on('close', (code: number | null) => {
        if (code !== 0) {
          console.error('Python script error:', error);
          return res.status(500).json({ 
            error: 'Analysis failed',
            details: error
          });
        }
        
        // Parse the result
        const lines = result.split('\n');
        
        const summary_lines = [];
        const risk_lines = [];
        const pricing_lines = [];
        const top_5_data = [];
        
        let current_section = null;
        
        for (const line of lines) {
          const trimmedLine = line.trim();
          if (!trimmedLine) continue;
            
          // Detect sections
          if (trimmedLine.toUpperCase().includes("TOP RECOMMENDED TRADE")) {
            current_section = "summary";
            continue;
          } else if (trimmedLine.toUpperCase().includes("STRATEGY OVERVIEW") || trimmedLine.toUpperCase().includes("RISK")) {
            current_section = "risk";
            continue;
          } else if (trimmedLine.toUpperCase().includes("PRICING COMPARISON")) {
            current_section = "pricing";
            continue;
          } else if (trimmedLine.toUpperCase().includes("TOP 5 COMBINATIONS")) {
            current_section = "top5";
            continue;
          } else if (trimmedLine.includes("No valid strategies found")) {
            return res.status(200).json({
              result: {
                summary: "No valid strategies found for these parameters.",
                risk: "",
                pricing_comparison: "",
                top_5: []
              }
            });
          }
          
          // Add lines to appropriate section
          if (current_section === "summary") {
            summary_lines.push(trimmedLine);
          } else if (current_section === "risk") {
            risk_lines.push(trimmedLine);
          } else if (current_section === "pricing") {
            pricing_lines.push(trimmedLine);
          } else if (current_section === "top5") {
            // Parse table data, skip header and separator lines
            if (trimmedLine.includes("|") && !trimmedLine.startsWith("---")) {
              // Skip the header row
              if (trimmedLine.toUpperCase().includes("RANK") && trimmedLine.toUpperCase().includes("EXPIRATION")) {
                continue;
              }
              const parts = trimmedLine.split("|").map(part => part.trim()).filter(part => part);
              if (parts.length >= 8) {
                top_5_data.push(parts.slice(0, 8)); // Rank, Expiration, Strikes, Net Cost, Net Vega, Net Volga, Efficiency, Score
              }
            }
          }
        }
        
        const parsed_result = {
          summary: summary_lines.join('\n'),
          risk: risk_lines.join('\n'),
          pricing_comparison: pricing_lines.join('\n'),
          top_5: top_5_data
        };
        
        res.status(200).json({ result: parsed_result });
        resolve(undefined);
      });
    });
  } catch (error) {
    console.error('API error:', error);
    res.status(500).json({ 
      error: 'Internal server error',
      details: error instanceof Error ? error.message : 'Unknown error'
    });
  }
} 