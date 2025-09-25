#!/usr/bin/env python3
# coding: utf-8
"""
dashboard.py - Streamlit dashboard for gold prices with composite index
Run:
    streamlit run dashboard.py
"""

import streamlit as st
import pandas as pd
import sqlite3
import subprocess
import os
import matplotlib.pyplot as plt
from datetime import datetime
import json

DB_FILE = "gold_data.db"
SCRAPER_CMD = ["python3", "gold_scraper.py"]

st.set_page_config(page_title="Gold Price Dashboard", layout="wide")
st.title("📊 Gold Price Dashboard (Vietnam)")

# ---- helpers ----
@st.cache_data(ttl=60)
def load_data(db_file: str = DB_FILE) -> pd.DataFrame:
    if not os.path.exists(db_file):
        return pd.DataFrame()
    conn = sqlite3.connect(db_file)
    df = pd.read_sql("SELECT * FROM gold_prices", conn, parse_dates=["timestamp"])
    conn.close()
    if df.empty:
        return df
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    try:
        df["raw_parsed"] = df["raw"].apply(lambda x: json.loads(x) if isinstance(x, str) else x)
    except Exception:
        df["raw_parsed"] = None
    return df.sort_values("timestamp")

def run_scraper() -> (bool, str):
    """Run scraper in subprocess and return (success, output)"""
    try:
        proc = subprocess.run(SCRAPER_CMD, capture_output=True, text=True, check=False)
        out = proc.stdout + "\n" + proc.stderr
        ok = proc.returncode == 0
        return ok, out
    except Exception as e:
        return False, str(e)

# ---- Sidebar controls ----
st.sidebar.header("Controls")
if st.sidebar.button("🔄 Scrape Now"):
    st.sidebar.info("Running scraper...")
    ok, out = run_scraper()
    if ok:
        st.sidebar.success("✅ Scrape finished successfully.")
        st.cache_data.clear()
    else:
        st.sidebar.error("❌ Scrape failed.")
        st.sidebar.text(out)

auto_refresh = st.sidebar.checkbox("Auto-refresh every N seconds", value=False)
refresh_seconds = st.sidebar.number_input("Refresh interval (seconds)", min_value=10, max_value=3600, value=300, step=10)

if auto_refresh:
    ms = int(refresh_seconds * 1000)
    js = f"<script>setTimeout(()=>location.reload(true), {ms});</script>"
    st.components.v1.html(js, height=0)

# ---- Load data ----
df = load_data()
if df.empty:
    st.warning("Database empty or not found. Hãy chạy `gold_scraper.py` trước để thu thập dữ liệu.")
    st.stop()

# Sidebar filters
sources_all = df["source"].unique().tolist()
selected_sources = st.sidebar.multiselect("Select sources", sources_all, default=sources_all)

min_ts = df["timestamp"].min()
max_ts = df["timestamp"].max()

# ✅ Fix lỗi date_input
date_range = st.sidebar.date_input("Date range", value=(min_ts.date(), max_ts.date()))
if isinstance(date_range, tuple):
    if len(date_range) == 2:
        start_date, end_date = date_range
    elif len(date_range) == 1:
        start_date = end_date = date_range[0]
    else:
        start_date = min_ts.date()
        end_date = max_ts.date()
else:
    start_date = end_date = date_range

mask = (
    (df["timestamp"].dt.date >= start_date)
    & (df["timestamp"].dt.date <= end_date)
    & df["source"].isin(selected_sources)
)
df_filtered = df[mask]

# ---- Main layout ----
st.subheader("Latest entries")
st.dataframe(df_filtered.sort_values("timestamp", ascending=False).head(50))

col1, col2 = st.columns(2)

# --- Chart: Price trend ---
with col1:
    st.subheader("Price trend (sell)")
    fig, ax = plt.subplots(figsize=(10, 4))
    for src, g in df_filtered.groupby("source"):
        ax.plot(g["timestamp"], g["sell"], label=src)
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("Sell (VND)")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

# --- Chart: Spread ---
with col2:
    st.subheader("Spread (sell - buy)")
    df_filtered = df_filtered.copy()
    df_filtered["spread"] = df_filtered["sell"] - df_filtered["buy"]
    fig2, ax2 = plt.subplots(figsize=(10, 4))
    for src, g in df_filtered.groupby("source"):
        ax2.plot(g["timestamp"], g["spread"], label=src)
    ax2.set_xlabel("Timestamp")
    ax2.set_ylabel("Spread (VND)")
    ax2.grid(True)
    ax2.legend()
    st.pyplot(fig2)

# --- Composite Gold Index ---
st.subheader("📊 Composite Gold Price Index & Volatility")

df_index = (
    df_filtered.groupby("timestamp")["sell"]
    .agg(["mean", "std"])
    .reset_index()
    .rename(columns={"mean": "composite_sell", "std": "volatility"})
)

fig3, ax3 = plt.subplots(figsize=(12, 5))
ax3.plot(df_index["timestamp"], df_index["composite_sell"], color="red", linewidth=2, label="Composite Index (mean)")
ax3.fill_between(
    df_index["timestamp"],
    df_index["composite_sell"] - df_index["volatility"],
    df_index["composite_sell"] + df_index["volatility"],
    color="orange", alpha=0.3, label="Volatility band"
)
ax3.set_xlabel("Timestamp")
ax3.set_ylabel("Composite Sell (VND)")
ax3.grid(True)
ax3.legend()
st.pyplot(fig3)

# ---- Forecast quick ----
st.subheader("Quick forecast (ARIMA)")
src_forecast = st.selectbox("Choose source for forecast", sources_all + ["Composite Index"])
steps = st.slider("Forecast steps (points)", 1, 60, 7)

if st.button("Run Forecast"):
    if src_forecast == "Composite Index":
        df_src = df_index.rename(columns={"composite_sell": "sell"}).sort_values("timestamp")
    else:
        df_src = df[df["source"] == src_forecast].sort_values("timestamp")
    series = df_src["sell"].dropna().reset_index(drop=True)
    if len(series) < 15:
        st.warning("Không đủ dữ liệu (cần >=15 điểm) để chạy ARIMA.")
    else:
        with st.spinner("Training ARIMA..."):
            try:
                from statsmodels.tsa.arima.model import ARIMA
                model = ARIMA(series, order=(1, 1, 1))
                fit = model.fit()
                fc = fit.forecast(steps=steps)
                st.write("Forecast result:")
                df_fc = pd.DataFrame({"step": range(1, len(fc) + 1), "forecast": fc.values})
                st.line_chart(df_fc.set_index("step"))
                st.dataframe(df_fc)
            except Exception as e:
                st.error(f"Forecast error: {e}")

# ---- Summary stats ----
st.subheader("Summary statistics")
st.write(
    df_filtered.groupby("source").agg(
        {
            "buy": ["min", "mean", "max"],
            "sell": ["min", "mean", "max"],
            "spread": ["mean", "std"],
        }
    )
)

# Composite stats
st.write("**Composite Index stats:**")
st.write(df_index[["composite_sell", "volatility"]].describe())

st.caption(f"Data range in DB: {min_ts} — {max_ts}")