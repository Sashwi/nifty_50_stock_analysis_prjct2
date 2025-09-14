import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data

# CSV file p
df = pd.read_csv("full_stock_data.csv")

# 2. Preprocessing

# Calculate yearly return for each stock
df['Yearly Return %'] = ((df['close'] - df['open']) / df['open']) * 100

# Green = Positive return, Red = Negative return
df['Performance'] = df['Yearly Return %'].apply(lambda x: 'Green' if x > 0 else 'Red')


# 3. Streamlit structure
st.set_page_config(page_title="Nifty 50 Stock Dashboard", layout="wide")
st.title("📊 Nifty 50 Stock Analysis Dashboard")

# Market Summary Section

st.subheader("📌 Market Summary")

col1, col2, col3 = st.columns(3)

with col1:
    total_stocks = df['symbol'].nunique()
    st.metric("Total Stocks", total_stocks)

with col2:
    green_stocks = df[df['Performance'] == "Green"]['symbol'].nunique()
    red_stocks = df[df['Performance'] == "Red"]['symbol'].nunique()
    st.metric("Green vs Red", f"{green_stocks} Green / {red_stocks} Red")

with col3:
    avg_price = df['close'].mean().round(2)
    avg_volume = df['volume'].mean().round(2)
    st.metric("Avg Price / volume", f"{avg_price} / {avg_volume}")


# Top 10 Gainers
st.subheader("🏆 Top 10 Gainers")
top_gainers = df.sort_values(by="Yearly Return %", ascending=False).head(10)

fig, ax = plt.subplots(figsize=(5,3))
ax.bar(top_gainers['symbol'], top_gainers['Yearly Return %'], color='green')
ax.set_xlabel("Stock Symbol",fontsize=7)
ax.set_ylabel("Yearly Return %",fontsize=7)
ax.set_title("Top 10 Gainers",fontsize=9)

# Adjust x-axis labels (rotation + smaller font)
ax.set_xticks(range(len(top_gainers['symbol'])))
ax.set_xticklabels(top_gainers['symbol'], rotation=45, fontsize=6, ha="right")

st.pyplot(fig)


# Top 10 Losers
st.subheader("📉 Top 10 Losers")
top_losers = df.sort_values(by="Yearly Return %", ascending=True).head(10)

fig, ax = plt.subplots(figsize=(5,3))
ax.bar(top_losers['symbol'], top_losers['Yearly Return %'], color='red')
ax.set_xlabel("Stock Symbol",fontsize=7)
ax.set_ylabel("Yearly Return %",fontsize=7)
ax.set_title("Top 10 Losers",fontsize=9)

# Adjust x-axis labels (rotation + smaller font)
ax.set_xticks(range(len(top_losers['symbol'])))
ax.set_xticklabels(top_losers['symbol'], rotation=45, fontsize=6, ha="right")

st.pyplot(fig)
