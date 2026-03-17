# portfolio_performance_log.py

import yfinance as yf
import pandas as pd
from datetime import datetime

# -------------------------------
# USER SETTINGS
# -------------------------------

portfolio = {
    "AAPL": {"units": 25.44, "target_allocation": 0.25},
    "BP.L": {"units": 10.22, "target_allocation": 0.15},
    "JPM": {"units": 16.0, "target_allocation": 0.20},
    "ULVR.L": {"units": 0.84, "target_allocation": 0.15},
    "CSP1.L": {"units": 0.06, "target_allocation": 0.15},
    "VGOV.L": {"units": 92.86, "target_allocation": 0.10}
}

main_drivers = {
    "2026-02-02": "International equities outperformed, energy and defensive sectors rose; mixed but generally positive markets.",
    "2026-02-09": "Divergent market action with tech weakness and banking/cyclical sector pressure.",
    "2026-02-16": "Bank of England held rates; mixed UK and US data kept sentiment cautious.",
    "2026-02-23": "Geopolitical risk and rising oil prices drove market volatility and risk-off sentiment.",
    "2026-03-02": "S&P 500 fell on weak jobs data and geopolitical uncertainty; oil surged and volatility rose.",
    "2026-03-09": "Inflation fears and geopolitical tensions dominated; equities rebounded after earlier losses."
}

last_update = "2026-01-27"
today = datetime.today().strftime("%Y-%m-%d")

# -------------------------------
# HELPER FUNCTIONS
# -------------------------------

def fetch_weekly_prices(ticker, start, end):
    data = yf.download(ticker, start=start, end=end, interval="1wk")
    data = data['Close'].reset_index()
    data.rename(columns={'Close': ticker}, inplace=True)
    return data

# -------------------------------
# MAIN SCRIPT
# -------------------------------

all_data = None
for ticker in portfolio:
    df = fetch_weekly_prices(ticker, last_update, today)
    if all_data is None:
        all_data = df
    else:
        all_data = pd.merge(all_data, df, on='Date', how='outer')

all_data.sort_values('Date', inplace=True)
all_data.ffill(inplace=True)
all_data.reset_index(drop=True, inplace=True)

# Initialize performance log
log = pd.DataFrame(columns=[
    "Date", "Portfolio Value (£)", "Weekly P&L (£)", "Weekly P&L (%)",
    "Best Performer", "Worst Performer", "Main Driver"
])

prev_portfolio_value = None

for idx, row in all_data.iterrows():
    date_str = row['Date'].strftime("%Y-%m-%d")
    portfolio_value = 0
    weekly_perf = {}

    for ticker, info in portfolio.items():
        price = row[ticker]
        value = price * info['units']
        portfolio_value += value
        if idx > 0:
            prev_price = all_data.loc[idx-1, ticker]
            weekly_perf[ticker] = ((price - prev_price) / prev_price) * 100

    if prev_portfolio_value is not None:
        weekly_pnl = portfolio_value - prev_portfolio_value
        weekly_pct = (weekly_pnl / prev_portfolio_value) * 100
        best_perf = max(weekly_perf, key=weekly_perf.get)
        worst_perf = min(weekly_perf, key=weekly_perf.get)
    else:
        weekly_pnl = 0
        weekly_pct = 0
        best_perf = ""
        worst_perf = ""

    main_driver = main_drivers.get(date_str, "No major news")

    log = pd.concat([log, pd.DataFrame([{
        "Date": date_str,
        "Portfolio Value (£)": round(portfolio_value, 2),
        "Weekly P&L (£)": round(weekly_pnl, 2),
        "Weekly P&L (%)": round(weekly_pct, 2),
        "Best Performer": best_perf,
        "Worst Performer": worst_perf,
        "Main Driver": main_driver
    }])], ignore_index=True)

    prev_portfolio_value = portfolio_value

log.to_csv("portfolio_performance_log.csv", index=False)
print("Performance log saved to 'portfolio_performance_log.csv'")
