import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("full_stock_data.csv")

# Preprocessing
df['Yearly Return %'] = ((df['close'] - df['open']) / df['open']) * 100
df['Performance'] = df['Yearly Return %'].apply(lambda x: 'Green' if x > 0 else 'Red')

# Streamlit structure
st.set_page_config(page_title="Nifty 50 Stock Dashboard", layout="wide")
st.title("📊 Nifty 50 Stock Analysis Dashboard")

# Market Summary Section
st.subheader("📌 Market Summary")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Stocks", df['symbol'].nunique())

with col2:
    green_stocks = df[df['Performance'] == "Green"]['symbol'].nunique()
    red_stocks = df[df['Performance'] == "Red"]['symbol'].nunique()
    st.metric("Green vs Red", f"{green_stocks} Green / {red_stocks} Red")

with col3:
    avg_price = df['close'].mean().round(2)
    avg_volume = df['volume'].mean().round(2)
    st.metric("Avg Price / Volume", f"{avg_price} / {avg_volume}")

# Two charts side by side (compact view)
col1, col2 = st.columns(2)

# Top 10 Gainers
with col1:
    st.subheader("🏆 Top 10 Gainers")
    top_gainers = df.sort_values(by="Yearly Return %", ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(4,2.5))   # Smaller figure
    ax.bar(top_gainers['symbol'], top_gainers['Yearly Return %'], color='green')
    ax.set_xlabel("Symbol", fontsize=6)
    ax.set_ylabel("Return %", fontsize=6)
    ax.set_title("Top 10 Gainers", fontsize=8)

    ax.set_xticks(range(len(top_gainers['symbol'])))
    ax.set_xticklabels(top_gainers['symbol'], rotation=45, fontsize=5, ha="right")

    st.pyplot(fig, bbox_inches="tight")

# Top 10 Losers
with col2:
    st.subheader("📉 Top 10 Losers")
    top_losers = df.sort_values(by="Yearly Return %", ascending=True).head(10)

    fig, ax = plt.subplots(figsize=(4,2.5))   # Smaller figure
    ax.bar(top_losers['symbol'], top_losers['Yearly Return %'], color='red')
    ax.set_xlabel("Symbol", fontsize=6)
    ax.set_ylabel("Return %", fontsize=6)
    ax.set_title("Top 10 Losers", fontsize=8)

    ax.set_xticks(range(len(top_losers['symbol'])))
    ax.set_xticklabels(top_losers['symbol'], rotation=45, fontsize=5, ha="right")

    st.pyplot(fig, bbox_inches="tight")
