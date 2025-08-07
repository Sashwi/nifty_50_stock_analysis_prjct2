#  Data-Driven Stock Analysis – Nifty 50 Dashboard

This project focuses on collecting, cleaning, analyzing, and visualizing stock market data from the **Nifty-50 index**, using modern data-analytics tools.  
The final outcome includes **interactive dashboards** built with **Streamlit** and **Power BI** to help investors and analysts make better decisions.

---
##  Project Objectives
- Extract daily Nifty-50 stock data from YAML files.
- Convert raw data into clean, structured CSV files.
- Store data in a SQL database (TiDB Cloud).
- Perform core financial data analysis using Python.
- Visualize:
  - Yearly top gainers and losers
  - Volatility of stocks
  - Sector-wise performance
  - Cumulative returns
  - Monthly gainers/losers
- Create dashboards using Power BI and Streamlit.
---
##  Technologies Used

 Python (Pandas)       -    Data Cleaning & Analysis         
 YAML                  -    Raw Data Storage Format         
 TiDB Cloud            -    SQL Data Storage                
 SQLAlchemy            -    Database Connection in Python   
 Matplotlib / Seaborn  -    Visualizations in Python   
 Power BI              -    Interactive Dashboard           
 Streamlit             -    Web-based Python Dashboard      
---
##  Project Pipeline

YAML files → Python (Clean & Convert to CSV) → MySQL (TiDB) → Python Analysis →
Sector Mapping → Create CSV Reports → Power BI & Streamlit Dashboards

## 🛠️ How to Run (Python)

# Create 3 main CSVs
python create_all_csv.py

# Run Streamlit dashboard
streamlit run stock_dashboard.py

## Power BI Dashboard

Open Stock_analysis.pbix using Power BI Desktop to view and interact with pre-built visuals:

Top Gainers and Losers
Sector Performance
Time-Series Exploration
