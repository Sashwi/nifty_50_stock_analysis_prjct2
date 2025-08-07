import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load CSV files
try:
    returns = pd.read_csv("yearly_returns.csv")
    sector_avg = pd.read_csv("sector_performance.csv")
except FileNotFoundError:
    st.error("CSV files not found. Please check file paths and names.")
    st.stop()

#  2. Show column names for debugging
st.write("Columns in 'returns' DataFrame:", returns.columns.tolist())
st.write("First few rows of data:")
st.write(returns.head())

# 3. App Title
st.title("Stock Market Performance Dashboard")

#  4. Market Overview
st.subheader("Market Overview")
col1, col2 = st.columns(2)
if 'end_price' in returns.columns:
    col1.metric("Average Price", f"{returns['end_price'].mean():.2f}")
    col2.metric("Average Volume", f"{returns['end_price'].mean():,.0f}")
else:
    st.warning("Column 'end_price' not found in returns data.")

#  5. Top Gainers
st.subheader("Top 5 Gainers")
if 'symbol' in returns.columns and 'yearly_return' in returns.columns:
    top_gainers = returns.sort_values('yearly_return', ascending=False).head(5)
    st.bar_chart(top_gainers.set_index('symbol')['yearly_return'])
else:
    st.warning("Required columns missing in returns data.")

#  6. Top Losers
st.subheader("Top 5 Losers")
if 'symbol' in returns.columns and 'yearly_return' in returns.columns:
    top_losers = returns.sort_values('yearly_return').head(5)
    st.bar_chart(top_losers.set_index('symbol')['yearly_return'])
else:
    st.warning("Required columns missing in returns data.")

#  7. Sector-wise performance
st.subheader("Sector-wise Performance")
if 'sector' in sector_avg.columns and 'yearly_return' in sector_avg.columns:
    fig, ax = plt.subplots()
    sector_avg.set_index('sector')['yearly_return'].plot(kind='bar', color='teal', ax=ax)
    ax.set_ylabel('Avg Yearly Return (%)')
    ax.set_title("Sector-wise Avg Return")
    st.pyplot(fig)
else:
    st.warning("Sector performance data not found or incomplete.")




