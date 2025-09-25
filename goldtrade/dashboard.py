#!/usr/bin/env python3
# coding: utf-8
"""
dashboard.py - Streamlit dashboard for gold prices
Run:
    python3 -m streamlit run dashboard.py
or
    python3 -m streamlit run dashboard.py
"""

import streamlit as st
import pandas as pd
import sqlite3
import subprocess
import os
import time
import matplotlib.pyplot as plt
from datetime import datetime
from typing import Optional
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
    # parse raw JSON column if needed
    try:
        df["raw_parsed"] = df["raw"].apply(lambda x: json.loads(x) if isinstance(x, str) else x)
    except Exception:
        df["raw_parsed"] = None
    return df.sort_values("timestamp")

def run_scraper() -> (bool, str):
    """Run scraper in subprocess and return (success, output)"""
    try:
        # run scraper and capture output (non-blocking allowed)
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
        # clear cache so load_data reloads from DB
        st.cache_data.clear()
    else:
        st.sidebar.error("❌ Scrape failed.")
        st.sidebar.text(out)

auto_refresh = st.sidebar.checkbox("Auto-refresh every N seconds", value=False)
refresh_seconds = st.sidebar.number_input("Refresh interval (seconds)", min_value=10, max_value=3600, value=300, step=10)

if auto_refresh:
    # Inject small JS to reload page after refresh_seconds
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
date_range = st.sidebar.date_input("Date range", value=(min_ts.date(), max_ts.date()))

start_date, end_date = date_range
mask = (df["timestamp"].dt.date >= start_date) & (df["timestamp"].dt.date <= end_date) & df["source"].isin(selected_sources)
df_filtered = df[mask]

# Main layout
st.subheader("Latest entries")
st.dataframe(df_filtered.sort_values("timestamp", ascending=False).head(50))

col1, col2 = st.columns(2)

with col1:
    st.subheader("Price trend (sell)")
    fig, ax = plt.subplots(figsize=(10,4))
    for src, g in df_filtered.groupby("source"):
        ax.plot(g["timestamp"], g["sell"], label=src)
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("Sell (VND)")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

with col2:
    st.subheader("Spread (sell - buy)")
    df_filtered = df_filtered.copy()
    df_filtered["spread"] = df_filtered["sell"] - df_filtered["buy"]
    fig2, ax2 = plt.subplots(figsize=(10,4))
    for src, g in df_filtered.groupby("source"):
        ax2.plot(g["timestamp"], g["spread"], label=src)
    ax2.set_xlabel("Timestamp")
    ax2.set_ylabel("Spread (VND)")
    ax2.grid(True)
    ax2.legend()
    st.pyplot(fig2)

# Forecast quick
st.subheader("Quick forecast (ARIMA)")
src_forecast = st.selectbox("Choose source for forecast", sources_all)
steps = st.slider("Forecast steps (points)", 1, 60, 7)

if st.button("Run Forecast"):
    df_src = df[df["source"] == src_forecast].sort_values("timestamp")
    series = df_src["sell"].dropna().reset_index(drop=True)
    if len(series) < 15:
        st.warning("Không đủ dữ liệu (cần >=15 điểm) để chạy ARIMA.")
    else:
        with st.spinner("Training ARIMA..."):
            try:
                from statsmodels.tsa.arima.model import ARIMA
                model = ARIMA(series, order=(1,1,1))
                fit = model.fit()
                fc = fit.forecast(steps=steps)
                st.write("Forecast result:")
                st.line_chart(pd.concat([series, pd.Series([None]*0)]))  # show history minimally
                # Show forecast as dataframe
                df_fc = pd.DataFrame({"step": list(range(1, len(fc)+1)), "forecast": fc.values})
                st.dataframe(df_fc)
            except Exception as e:
                st.error(f"Forecast error: {e}")

# Small stats
st.subheader("Summary statistics")
st.write(df_filtered.groupby("source").agg({
    "buy": ["min", "mean", "max"],
    "sell": ["min", "mean", "max"],
    "spread": ["mean", "std"]
}))

st.caption(f"Data range in DB: {min_ts} — {max_ts}")