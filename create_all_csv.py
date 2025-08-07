"""
This script loads stock data from TiDB, calculates yearly returns,
adds sector information, and exports these 3 CSV files:

1. full_stock_data.csv      -> complete stock table
2. yearly_returns.csv       -> symbol, start_price, end_price, yearly_return, sector
3. sector_performance.csv   -> sector-wise average yearly return
"""

import pandas as pd
from sqlalchemy import create_engine

# ========== 1) Connect to TiDB ==========
username = "3ZpzE69BSNXuvY2.root"
password = "MSiewQGRtx2F7qYu"
host = "gateway01.us-west-2.prod.aws.tidbcloud.com"
port = 4000
database = "stock_analysis"
ssl_certificate_path = "certs/ca-certificate.crt"

connection_url = (
    f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}"
    f"?ssl_ca={ssl_certificate_path}"
)
engine = create_engine(connection_url)

# ========== 2) Read raw data ==========
df = pd.read_sql("SELECT date, symbol, close, open, volume FROM stock_data", engine)
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d_%H-%M-%S')
df = df.sort_values(['symbol', 'date'])

# 2a) Export full table
df.to_csv("full_stock_data.csv", index=False)
print("full_stock_data.csv saved.")

# ========== 3) Compute yearly return ==========
returns = (
    df.groupby('symbol')
      .agg(start_price=('close', 'first'), end_price=('close', 'last'))
      .reset_index()
)
returns['yearly_return'] = ((returns['end_price'] - returns['start_price']) / returns['start_price']) * 100

# ========== 4) Mapping sectors ==========
sector_mapping = {
    "ADANIENT": "Conglomerate", "ADANIPORTS": "Transport", "ASIANPAINT": "Consumer",
    "APOLLOHOSP": "Healthcare", "AXISBANK": "Banking", "BAJAJ-AUTO": "Automobile",
    "BAJFINANCE": "Financials", "BAJAJFINSV": "Financials", "BPCL": "Energy",
    "BHARTIARTL": "Telecom", "BRITANNIA": "Consumer", "CIPLA": "Pharma",
    "COALINDIA": "Energy", "DIVISLAB": "Pharma", "DRREDDY": "Pharma",
    "EICHERMOT": "Automobile", "GRASIM": "Manufacturing", "HCLTECH": "IT",
    "HDFCBANK": "Banking", "HDFCLIFE": "Insurance", "HEROMOTOCO": "Automobile",
    "HINDALCO": "Metals", "HINDUNILVR": "Consumer", "ICICIBANK": "Banking",
    "INDUSINDBK": "Banking", "INFY": "IT", "ITC": "Consumer", "JSWSTEEL": "Metals",
    "KOTAKBANK": "Banking", "LT": "Infrastructure", "M&M": "Automobile",
    "MARUTI": "Automobile", "NESTLEIND": "Consumer", "NTPC": "Energy", "ONGC": "Energy",
    "PIDILITIND": "Consumer", "POWERGRID": "Energy", "RELIANCE": "Energy", "SBIN": "Banking",
    "SUNPHARMA": "Pharma", "TATACONSUM": "Consumer", "TATAMOTORS": "Automobile",
    "TATASTEEL": "Metals", "TCS": "IT", "TECHM": "IT", "TITAN": "Consumer",
    "ULTRACEMCO": "Cement", "UPL": "Agrochemical", "WIPRO": "IT"
}
returns['sector'] = returns['symbol'].map(sector_mapping)

# ========== 5) Export yearly_returns ==========
returns.to_csv("yearly_returns.csv", index=False)
print(" yearly_returns.csv saved.")


# ========== 6) Export sector-level average ==========
sector_perf = returns.groupby('sector')['yearly_return'].mean().reset_index()
sector_perf.to_csv("sector_performance.csv", index=False)
print(" sector_performance.csv saved.")

print("\n All CSV files created successfully!")
