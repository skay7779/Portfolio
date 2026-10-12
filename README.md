# Portfolio Analysis & Equity Research

A self-directed project combining Python, SQL and Excel to analyse a five-asset portfolio and value individual companies.

## What's inside

| File | What it shows |
|---|---|
| `Portfolio 1.ipynb` / `Portfolio 2.pdf` | Python + SQLite pipeline pulling daily prices (2018–2026) for Apple, JPMorgan, BP, Unilever and an S&P 500 ETF via `yfinance`, then measuring portfolio risk: annualised return and volatility, Sharpe ratio, 1-day 95% Value at Risk, correlation matrix, rolling volatility and each asset's contribution to total risk. |
| `Portfolio Risk and Exposure.xlsx` | Asset-class, sector and geographic exposure of a simulated £25,000 portfolio. |
| `Risk commentary.docx` | Weekly risk commentary written during a five-week portfolio simulation, covering concentration, sector and macro risk (including the 2026 Middle East oil shock). |
| `DCF for BP.xlsx` / `BP DCF Analysis report.docx` | Free cash flow DCF valuation of BP plc with a WACC vs terminal-growth sensitivity table. |
| `Equity Research Note - BP.L.docx` | Equity research note on BP: business overview, financials, P/E comparison with Shell, risks, catalysts and a Hold recommendation. |
| `DCF for AAPL and Sensitivity Analysis.xlsx` | Dividend discount model for Apple, with a sensitivity table and a note on why a DDM undervalues a company that returns cash mainly through buybacks. |
| `Regulatory Compliance Case Study.docx` | Case study of Barclays' LIBOR manipulation: what happened, regulations breached and consequences. |

## Key results (portfolio notebook)

- Annualised return: 13.4% · annualised volatility: 16.6% · Sharpe ratio: 0.81 (risk-free rate assumed 0%)
- 1-day 95% Value at Risk: 1.7% of portfolio value
- BP DCF: implied value of about £9.24 per share vs a market price of about £5.42 (Sept 2026); around 74% of enterprise value comes from the terminal value

## Running the notebook

```
pip install -r requirements.txt
jupyter notebook "Portfolio 1.ipynb"
```

Then use **Kernel → Restart & Run All**. Price data is downloaded from Yahoo Finance via `yfinance`.

## Skills demonstrated

Python (pandas, NumPy, matplotlib, seaborn), SQL (SQLite), Excel financial modelling, DCF and dividend discount valuation, portfolio risk metrics, equity research writing.
