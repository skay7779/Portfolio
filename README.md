# Portfolio Analysis Tool

## Overview

This project builds a discounted cash flow (DCF) model in Python to estimateintrinsic value per share and evaluate sensitivity to key assumptions such as growth rate and discount rate. It is designed to replicate real-world equity valuation workflows while remaining flexible for experimentation and extension.

## Features
- Portfolio valuation (DCF)
- Sensitivity analysis tables
- Data handling and financial modelling with Python
- Risk commentary and research reports

## Tech Stack
- Python
- Pandas / NumPy
- Excel
- Word

## How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/skay7779/Portfolio.git
   ```
2. Navigate into the folder:
   ```bash
   cd Portfolio
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the script:
   ```bash
   python main.py
   ```

## Example Output
Sensitivity Table (PV per Share)            
Growth Rate/ Discount Rate    6%    7%    8
4%    14.13    12.50    11.00
5%    27.28    21.00    18.33
6%    27.53    22.00    19.50

## What I Learned
- Building financial models in Python
- Handling real-world data
- Empirical application of theoretical ideas

## Future Improvements
- Add UI (Streamlit or web app)
- Automate data fetching (APIs)
- Improve model assumptions

