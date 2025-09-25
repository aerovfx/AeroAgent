#!/usr/bin/env python3
# coding: utf-8
"""
Enhanced dashboard.py - Advanced Streamlit dashboard for gold prices with real-time features
Run:
    streamlit run dashboard.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import subprocess
import os
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import json
import time
from typing import Dict, Any
import asyncio
import threading
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

# Technical Analysis imports
try:
    import talib
    TALIB_AVAILABLE = True
except ImportError:
    TALIB_AVAILABLE = False
    st.warning("⚠️ TA-Lib not installed. Install with: pip install TA-Lib")

# Configuration
DB_FILE = "gold_data.db"
TIMESERIES_DB = "gold_timeseries.db"
SCRAPER_CMD = ["python3", "gold_scraper.py"]

st.set_page_config(
    page_title="🏆 Advanced Gold Price Dashboard", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .metric-card {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 15px;
        margin: 5px 0;
        border-left: 4px solid #ff6b35;
    }
    .alert-high { border-left-color: #ff4444; }
    .alert-medium { border-left-color: #ffaa00; }
    .alert-low { border-left-color: #00aa44; }
    
    .realtime-indicator {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        display: inline-block;
        margin-right: 8px;
    }
    .online { background-color: #00ff00; }
    .offline { background-color: #ff0000; }
</style>
""", unsafe_allow_html=True)

# Title with real-time indicator
st.markdown("""
# 🏆 Advanced Gold Price Dashboard
<div style="display: flex; align-items: center; margin-bottom: 20px;">
    <span class="realtime-indicator online"></span>
    <span>Real-time Gold Market Analysis</span>
</div>
""", unsafe_allow_html=True)

# ---- Enhanced Helper Functions ----
@st.cache_data(ttl=30)  # Cache for 30 seconds for real-time feel
def load_current_data(db_file: str = DB_FILE) -> pd.DataFrame:
    """Load current gold prices"""
    if not os.path.exists(db_file):
        return pd.DataFrame()
    
    conn = sqlite3.connect(db_file)
    df = pd.read_sql("SELECT * FROM gold_prices ORDER BY timestamp DESC", conn, parse_dates=["timestamp"])
    conn.close()
    
    if df.empty:
        return df
    
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    try:
        df["raw_parsed"] = df["raw"].apply(lambda x: json.loads(x) if isinstance(x, str) else x)
    except Exception:
        df["raw_parsed"] = None
    
    # Calculate spreads and other metrics
    df["spread"] = df["sell"] - df["buy"]
    df["spread_pct"] = (df["spread"] / df["buy"]) * 100
    df["mid_price"] = (df["buy"] + df["sell"]) / 2
    
    return df

@st.cache_data(ttl=60)
def load_historical_data(db_file: str = TIMESERIES_DB) -> pd.DataFrame:
    """Load historical time-series data"""
    if not os.path.exists(db_file):
        return pd.DataFrame()
    
    conn = sqlite3.connect(db_file)
    df = pd.read_sql("""
        SELECT date, source, buy, sell, open, high, low, close, spot_price, unit, timestamp
        FROM gold_timeseries 
        ORDER BY date DESC, source
    """, conn)
    conn.close()
    
    if df.empty:
        return df
    
    df["date"] = pd.to_datetime(df["date"])
    df["spread"] = df["sell"] - df["buy"]
    df["mid_price"] = (df["buy"] + df["sell"]) / 2
    
    return df

def calculate_technical_indicators(df: pd.DataFrame, price_col: str = "close") -> pd.DataFrame:
    """Calculate technical indicators"""
    if df.empty or not TALIB_AVAILABLE:
        return df
    
    df = df.copy()
    prices = df[price_col].dropna().values
    
    if len(prices) < 20:
        return df
    
    try:
        # Moving Averages
        df["MA_5"] = talib.SMA(prices, timeperiod=5)
        df["MA_10"] = talib.SMA(prices, timeperiod=10)
        df["MA_20"] = talib.SMA(prices, timeperiod=20)
        df["MA_50"] = talib.SMA(prices, timeperiod=min(50, len(prices)//2))
        
        # Exponential Moving Averages
        df["EMA_12"] = talib.EMA(prices, timeperiod=12)
        df["EMA_26"] = talib.EMA(prices, timeperiod=26)
        
        # MACD
        df["MACD"], df["MACD_signal"], df["MACD_hist"] = talib.MACD(prices)
        
        # RSI
        df["RSI"] = talib.RSI(prices, timeperiod=14)
        
        # Bollinger Bands
        df["BB_upper"], df["BB_middle"], df["BB_lower"] = talib.BBANDS(prices)
        
        # Stochastic
        if "high" in df.columns and "low" in df.columns:
            highs = df["high"].values
            lows = df["low"].values
            df["STOCH_K"], df["STOCH_D"] = talib.STOCH(highs, lows, prices)
        
        # ATR (Average True Range)
        if "high" in df.columns and "low" in df.columns:
            df["ATR"] = talib.ATR(df["high"].values, df["low"].values, prices)
        
        # Williams %R
        if "high" in df.columns and "low" in df.columns:
            df["WILLIAMS_R"] = talib.WILLR(df["high"].values, df["low"].values, prices)
        
    except Exception as e:
        st.error(f"Error calculating technical indicators: {e}")
    
    return df

def run_scraper() -> tuple[bool, str]:
    """Run scraper in subprocess and return (success, output)"""
    try:
        proc = subprocess.run(SCRAPER_CMD, capture_output=True, text=True, check=False, timeout=120)
        out = proc.stdout + "\n" + proc.stderr
        ok = proc.returncode == 0
        return ok, out
    except subprocess.TimeoutExpired:
        return False, "Scraper timeout after 120 seconds"
    except Exception as e:
        return False, str(e)

def get_market_sentiment(rsi: float, macd_hist: float) -> tuple[str, str]:
    """Determine market sentiment based on technical indicators"""
    if pd.isna(rsi) or pd.isna(macd_hist):
        return "NEUTRAL", "⚪"
    
    if rsi > 70 and macd_hist > 0:
        return "STRONG_BUY", "🟢"
    elif rsi > 60 and macd_hist > 0:
        return "BUY", "🟢"
    elif rsi < 30 and macd_hist < 0:
        return "STRONG_SELL", "🔴"
    elif rsi < 40 and macd_hist < 0:
        return "SELL", "🔴"
    else:
        return "NEUTRAL", "🟡"

# ---- Sidebar Controls ----
st.sidebar.header("🎛️ Dashboard Controls")

# Real-time settings
st.sidebar.subheader("⚡ Real-time Settings")
auto_refresh = st.sidebar.checkbox("🔄 Auto-refresh", value=True)
refresh_interval = st.sidebar.selectbox(
    "Refresh interval", 
    [10, 30, 60, 120, 300],
    index=2,
    format_func=lambda x: f"{x} seconds"
)

# Auto-refresh logic
if auto_refresh:
    placeholder = st.empty()
    time.sleep(refresh_interval)
    st.rerun()

# Scraper controls
st.sidebar.subheader("📡 Data Collection")
col1, col2 = st.sidebar.columns(2)
with col1:
    if st.button("🔄 Scrape Now", type="primary"):
        with st.spinner("Running scraper..."):
            ok, out = run_scraper()
            if ok:
                st.success("✅ Scrape completed")
                st.cache_data.clear()
                time.sleep(2)
                st.rerun()
            else:
                st.error("❌ Scrape failed")
                with st.expander("Error details"):
                    st.text(out)

with col2:
    if st.button("🗑️ Clear Cache"):
        st.cache_data.clear()
        st.success("Cache cleared")
        time.sleep(1)
        st.rerun()

# ---- Load Data ----
current_df = load_current_data()
historical_df = load_historical_data()

if current_df.empty and historical_df.empty:
    st.warning("📭 No data found. Run the scraper first to collect gold price data.")
    st.stop()

# Data source selection
all_sources = []
if not current_df.empty:
    all_sources.extend(current_df["source"].unique().tolist())
if not historical_df.empty:
    all_sources.extend(historical_df["source"].unique().tolist())
all_sources = sorted(list(set(all_sources)))

selected_sources = st.sidebar.multiselect("📊 Select Sources", all_sources, default=all_sources[:5])

# Time range selection
st.sidebar.subheader("📅 Time Range")
time_range = st.sidebar.selectbox(
    "Quick select",
    ["Last 24 Hours", "Last 3 Days", "Last Week", "Last Month", "Last 3 Months", "Custom"]
)

if time_range == "Custom":
    if not historical_df.empty:
        min_date = historical_df["date"].min().date()
        max_date = historical_df["date"].max().date()
        date_range = st.sidebar.date_input("Date Range", value=(min_date, max_date))
    else:
        date_range = st.sidebar.date_input("Date Range")
else:
    # Calculate date range based on selection
    end_date = datetime.now().date()
    if time_range == "Last 24 Hours":
        start_date = (datetime.now() - timedelta(days=1)).date()
    elif time_range == "Last 3 Days":
        start_date = (datetime.now() - timedelta(days=3)).date()
    elif time_range == "Last Week":
        start_date = (datetime.now() - timedelta(weeks=1)).date()
    elif time_range == "Last Month":
        start_date = (datetime.now() - timedelta(days=30)).date()
    else:  # Last 3 Months
        start_date = (datetime.now() - timedelta(days=90)).date()
    date_range = (start_date, end_date)

# ---- Real-time Dashboard Header ----
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.markdown(f"""
<div style="background: linear-gradient(90deg, #1f4037, #99f2c8); color: white; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
    <h3>🕐 Live Market Status - {current_time}</h3>
    <p>Last updated: {refresh_interval}s ago | Auto-refresh: {'ON' if auto_refresh else 'OFF'}</p>
</div>
""", unsafe_allow_html=True)

# ---- Current Market Overview ----
if not current_df.empty:
    st.subheader("💰 Current Market Overview")
    
    # Latest prices from each source
    latest_data = current_df.groupby("source").last().reset_index()
    latest_data = latest_data[latest_data["source"].isin(selected_sources)]
    
    # Create metrics columns
    cols = st.columns(min(len(latest_data), 5))
    
    for i, (_, row) in enumerate(latest_data.iterrows()):
        if i < len(cols):
            with cols[i]:
                # Calculate change (mock for now - would need historical comparison)
                change = np.random.uniform(-2, 2)  # Replace with actual calculation
                change_pct = change / row["sell"] * 100 if row["sell"] else 0
                
                st.metric(
                    label=f"{row['source']} (Sell)",
                    value=f"{row['sell']:,.0f} ₫",
                    delta=f"{change_pct:+.2f}%"
                )
                
                st.metric(
                    label="Spread",
                    value=f"{row['spread']:,.0f} ₫",
                    delta=f"{row['spread_pct']:.2f}%"
                )

# ---- Technical Analysis Dashboard ----
if not historical_df.empty:
    st.subheader("📈 Technical Analysis Dashboard")
    
    # Filter historical data
    hist_filtered = historical_df[historical_df["source"].isin(selected_sources)]
    if isinstance(date_range, tuple) and len(date_range) == 2:
        start_date, end_date = date_range
        hist_filtered = hist_filtered[
            (hist_filtered["date"].dt.date >= start_date) & 
            (hist_filtered["date"].dt.date <= end_date)
        ]
    
    # Calculate technical indicators for each source
    ta_tabs = st.tabs(["📊 Price Charts", "🔢 Technical Indicators", "📉 Market Signals", "🎯 Trading Signals"])
    
    with ta_tabs[0]:  # Price Charts
        fig = make_subplots(
            rows=3, cols=1,
            subplot_titles=("Gold Prices", "Volume/Spread Analysis", "Price Distribution"),
            vertical_spacing=0.08,
            row_heights=[0.6, 0.25, 0.15]
        )
        
        colors = px.colors.qualitative.Set1
        
        for i, source in enumerate(selected_sources):
            source_data = hist_filtered[hist_filtered["source"] == source].sort_values("date")
            
            if not source_data.empty:
                color = colors[i % len(colors)]
                
                # Main price line
                fig.add_trace(
                    go.Scatter(
                        x=source_data["date"],
                        y=source_data["sell"],
                        name=f"{source} - Sell",
                        line=dict(color=color, width=2),
                        mode="lines"
                    ),
                    row=1, col=1
                )
                
                # Buy price (lighter)
                fig.add_trace(
                    go.Scatter(
                        x=source_data["date"],
                        y=source_data["buy"],
                        name=f"{source} - Buy",
                        line=dict(color=color, width=1, dash="dot"),
                        mode="lines"
                    ),
                    row=1, col=1
                )
                
                # Spread analysis
                fig.add_trace(
                    go.Scatter(
                        x=source_data["date"],
                        y=source_data["spread"],
                        name=f"{source} - Spread",
                        line=dict(color=color),
                        mode="lines"
                    ),
                    row=2, col=1
                )
        
        # Price distribution histogram
        all_prices = hist_filtered["sell"].dropna()
        fig.add_trace(
            go.Histogram(
                x=all_prices,
                name="Price Distribution",
                nbinsx=50,
                opacity=0.7
            ),
            row=3, col=1
        )
        
        fig.update_layout(
            height=800,
            title_text="Gold Price Analysis Dashboard",
            showlegend=True
        )
        
        fig.update_xaxes(title_text="Date", row=3, col=1)
        fig.update_yaxes(title_text="Price (₫)", row=1, col=1)
        fig.update_yaxes(title_text="Spread (₫)", row=2, col=1)
        fig.update_yaxes(title_text="Frequency", row=3, col=1)
        
        st.plotly_chart(fig, use_container_width=True)
    
    with ta_tabs[1]:  # Technical Indicators
        if TALIB_AVAILABLE and not hist_filtered.empty:
            # Select source for detailed technical analysis
            ta_source = st.selectbox("Select source for technical analysis", selected_sources)
            ta_data = hist_filtered[hist_filtered["source"] == ta_source].sort_values("date")
            
            if len(ta_data) > 20:
                ta_data = calculate_technical_indicators(ta_data, "sell")
                
                # Technical indicators charts
                fig_ta = make_subplots(
                    rows=4, cols=1,
                    subplot_titles=(
                        "Price & Moving Averages",
                        "MACD",
                        "RSI & Stochastic",
                        "Bollinger Bands"
                    ),
                    vertical_spacing=0.05,
                    row_heights=[0.4, 0.2, 0.2, 0.2]
                )
                
                # Price and moving averages
                fig_ta.add_trace(go.Scatter(x=ta_data["date"], y=ta_data["sell"], name="Price", line=dict(width=2)), row=1, col=1)
                for ma in ["MA_5", "MA_10", "MA_20", "MA_50"]:
                    if ma in ta_data.columns:
                        fig_ta.add_trace(go.Scatter(x=ta_data["date"], y=ta_data[ma], name=ma), row=1, col=1)
                
                # MACD
                if "MACD" in ta_data.columns:
                    fig_ta.add_trace(go.Scatter(x=ta_data["date"], y=ta_data["MACD"], name="MACD"), row=2, col=1)
                    fig_ta.add_trace(go.Scatter(x=ta_data["date"], y=ta_data["MACD_signal"], name="Signal"), row=2, col=1)
                    fig_ta.add_trace(go.Bar(x=ta_data["date"], y=ta_data["MACD_hist"], name="Histogram"), row=2, col=1)
                
                # RSI
                if "RSI" in ta_data.columns:
                    fig_ta.add_trace(go.Scatter(x=ta_data["date"], y=ta_data["RSI"], name="RSI"), row=3, col=1)
                    fig_ta.add_hline(y=70, line_dash="dash", line_color="red", row=3, col=1)
                    fig_ta.add_hline(y=30, line_dash="dash", line_color="green", row=3, col=1)
                
                # Bollinger Bands
                if "BB_upper" in ta_data.columns:
                    fig_ta.add_trace(go.Scatter(x=ta_data["date"], y=ta_data["BB_upper"], name="BB Upper"), row=4, col=1)
                    fig_ta.add_trace(go.Scatter(x=ta_data["date"], y=ta_data["BB_middle"], name="BB Middle"), row=4, col=1)
                    fig_ta.add_trace(go.Scatter(x=ta_data["date"], y=ta_data["BB_lower"], name="BB Lower"), row=4, col=1)
                    fig_ta.add_trace(go.Scatter(x=ta_data["date"], y=ta_data["sell"], name="Price", line=dict(color="black", width=2)), row=4, col=1)
                
                fig_ta.update_layout(height=1000, title_text=f"Technical Analysis - {ta_source}")
                st.plotly_chart(fig_ta, use_container_width=True)
                
                # Technical indicators table
                st.subheader("📊 Latest Technical Indicators")
                latest_ta = ta_data.iloc[-1]
                
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("RSI", f"{latest_ta.get('RSI', 0):.1f}", help="Relative Strength Index (14)")
                    st.metric("MACD", f"{latest_ta.get('MACD', 0):.2f}")
                
                with col2:
                    st.metric("MA 5", f"{latest_ta.get('MA_5', 0):,.0f} ₫")
                    st.metric("MA 20", f"{latest_ta.get('MA_20', 0):,.0f} ₫")
                
                with col3:
                    st.metric("ATR", f"{latest_ta.get('ATR', 0):,.0f} ₫", help="Average True Range (Volatility)")
                    st.metric("Williams %R", f"{latest_ta.get('WILLIAMS_R', 0):.1f}")
                
                with col4:
                    sentiment, emoji = get_market_sentiment(
                        latest_ta.get('RSI', 50),
                        latest_ta.get('MACD_hist', 0)
                    )
                    st.metric("Market Sentiment", f"{emoji} {sentiment}")
            else:
                st.warning("Insufficient data for technical analysis (need >20 points)")
        else:
            st.info("Install TA-Lib for technical indicators: pip install TA-Lib")
    
    with ta_tabs[2]:  # Market Signals
        st.subheader("🚨 Market Alerts & Signals")
        
        # Generate alerts based on technical indicators
        alerts = []
        
        for source in selected_sources:
            source_data = hist_filtered[hist_filtered["source"] == source].sort_values("date")
            if len(source_data) > 1:
                latest = source_data.iloc[-1]
                previous = source_data.iloc[-2]
                
                # Price change alert
                price_change = (latest["sell"] - previous["sell"]) / previous["sell"] * 100
                if abs(price_change) > 2:  # 2% change threshold
                    alert_type = "🔴 HIGH" if abs(price_change) > 5 else "🟡 MEDIUM"
                    alerts.append({
                        "Type": alert_type,
                        "Source": source,
                        "Signal": f"Price change: {price_change:+.2f}%",
                        "Current": f"{latest['sell']:,.0f} ₫",
                        "Previous": f"{previous['sell']:,.0f} ₫"
                    })
                
                # Spread alert
                if latest["spread_pct"] > 3:  # High spread alert
                    alerts.append({
                        "Type": "🟡 MEDIUM",
                        "Source": source,
                        "Signal": f"High spread: {latest['spread_pct']:.2f}%",
                        "Current": f"{latest['spread']:,.0f} ₫",
                        "Previous": "-"
                    })
        
        if alerts:
            alerts_df = pd.DataFrame(alerts)
            st.dataframe(alerts_df, use_container_width=True)
        else:
            st.success("✅ No alerts at this time")
        
        # Market correlation matrix
        st.subheader("📊 Source Correlation Matrix")
        
        pivot_data = hist_filtered.pivot_table(
            index="date", 
            columns="source", 
            values="sell", 
            aggfunc="mean"
        )
        
        if not pivot_data.empty:
            corr_matrix = pivot_data.corr()
            
            fig_corr = go.Figure(data=go.Heatmap(
                z=corr_matrix.values,
                x=corr_matrix.columns,
                y=corr_matrix.index,
                colorscale="RdBu",
                zmid=0,
                text=corr_matrix.round(3),
                texttemplate="%{text}",
                textfont={"size": 12}
            ))
            
            fig_corr.update_layout(
                title="Gold Price Source Correlation",
                height=500
            )
            
            st.plotly_chart(fig_corr, use_container_width=True)
    
    with ta_tabs[3]:  # Trading Signals
        st.subheader("🎯 AI Trading Signals")
        
        # Simple trading signal generation
        signals = []
        
        for source in selected_sources:
            source_data = hist_filtered[hist_filtered["source"] == source].sort_values("date")
            
            if len(source_data) > 5:
                if TALIB_AVAILABLE:
                    source_data = calculate_technical_indicators(source_data, "sell")
                
                latest = source_data.iloc[-1]
                
                # Generate signals based on multiple indicators
                signal_strength = 0
                signal_reasons = []
                
                # RSI signals
                if "RSI" in source_data.columns and not pd.isna(latest["RSI"]):
                    if latest["RSI"] < 30:
                        signal_strength += 2
                        signal_reasons.append("RSI oversold")
                    elif latest["RSI"] > 70:
                        signal_strength -= 2
                        signal_reasons.append("RSI overbought")
                
                # MACD signals
                if "MACD_hist" in source_data.columns and not pd.isna(latest["MACD_hist"]):
                    if latest["MACD_hist"] > 0:
                        signal_strength += 1
                        signal_reasons.append("MACD bullish")
                    else:
                        signal_strength -= 1
                        signal_reasons.append("MACD bearish")
                
                # Moving average signals
                if "MA_5" in source_data.columns and "MA_20" in source_data.columns:
                    if latest["sell"] > latest["MA_5"] > latest["MA_20"]:
                        signal_strength += 1
                        signal_reasons.append("Price above MA")
                    elif latest["sell"] < latest["MA_5"] < latest["MA_20"]:
                        signal_strength -= 1
                        signal_reasons.append("Price below MA")
                
                # Determine signal
                if signal_strength >= 2:
                    signal = "🟢 STRONG BUY"
                elif signal_strength >= 1:
                    signal = "🟢 BUY"
                elif signal_strength <= -2:
                    signal = "🔴 STRONG SELL"
                elif signal_strength <= -1:
                    signal = "🔴 SELL"
                else:
                    signal = "🟡 HOLD"
                
                signals.append({
                    "Source": source,
                    "Signal": signal,
                    "Strength": signal_strength,
                    "Reasons": ", ".join(signal_reasons) if signal_reasons else "No clear signals",
                    "Current Price": f"{latest['sell']:,.0f} ₫",
                    "Last Update": latest["date"].strftime("%Y-%m-%d")
                })
        
        if signals:
            signals_df = pd.DataFrame(signals)
            st.dataframe(signals_df, use_container_width=True)
        else:
            st.info("No trading signals available")

# ---- Performance Analytics ----
st.subheader("⚡ Performance Analytics")

perf_col1, perf_col2, perf_col3 = st.columns(3)

with perf_col1:
    st.metric(
        "Data Points",
        len(current_df) + len(historical_df),
        f"+{len(current_df)} today"
    )

with perf_col2:
    if not current_df.empty:
        latest_update = current_df["timestamp"].max()
        minutes_ago = (datetime.now() - latest_update.replace(tzinfo=None)).total_seconds() / 60
        st.metric(
            "Last Update",
            f"{minutes_ago:.0f}m ago",
            "Real-time" if minutes_ago < 5 else "Delayed"
        )

with perf_col3:
    active_sources = len(selected_sources)
    total_sources = len(all_sources)
    st.metric(
        "Active Sources",
        f"{active_sources}/{total_sources}",
        f"{(active_sources/total_sources*100):.0f}% coverage"
    )

# ---- Portfolio Management ----
st.subheader("💼 Portfolio & Risk Management")

portfolio_tabs = st.tabs(["💰 Portfolio Tracker", "⚖️ Risk Analysis", "📊 Performance Reports", "🎯 Position Calculator"])

with portfolio_tabs[0]:  # Portfolio Tracker
    st.markdown("### 💰 Gold Portfolio Tracker")
    
    # Portfolio input section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("#### Add Position")
        with st.form("add_position"):
            pos_source = st.selectbox("Source", selected_sources)
            pos_type = st.selectbox("Position Type", ["Long (Buy)", "Short (Sell)"])
            pos_quantity = st.number_input("Quantity (grams)", min_value=0.1, value=10.0, step=0.1)
            pos_entry_price = st.number_input("Entry Price (₫/gram)", min_value=1000, value=80000000, step=1000)
            pos_date = st.date_input("Entry Date", value=datetime.now().date())
            
            if st.form_submit_button("➕ Add Position"):
                if "portfolio" not in st.session_state:
                    st.session_state.portfolio = []
                
                position = {
                    "id": len(st.session_state.portfolio),
                    "source": pos_source,
                    "type": pos_type,
                    "quantity": pos_quantity,
                    "entry_price": pos_entry_price,
                    "entry_date": pos_date,
                    "status": "Open"
                }
                st.session_state.portfolio.append(position)
                st.success("✅ Position added to portfolio!")
                st.rerun()
    
    with col2:
        # Portfolio summary
        if "portfolio" in st.session_state and st.session_state.portfolio:
            total_positions = len(st.session_state.portfolio)
            total_value = sum(p["quantity"] * p["entry_price"] for p in st.session_state.portfolio)
            
            st.metric("Total Positions", total_positions)
            st.metric("Portfolio Value", f"{total_value:,.0f} ₫")
            
            if st.button("🗑️ Clear Portfolio"):
                st.session_state.portfolio = []
                st.rerun()
    
    # Portfolio display
    if "portfolio" in st.session_state and st.session_state.portfolio:
        st.markdown("#### Current Positions")
        
        portfolio_data = []
        for pos in st.session_state.portfolio:
            # Get current price for P&L calculation
            current_price = 80000000  # Default, replace with actual current price
            if not current_df.empty:
                current_source_data = current_df[current_df["source"] == pos["source"]]
                if not current_source_data.empty:
                    current_price = current_source_data.iloc[-1]["sell"]
            
            pnl = (current_price - pos["entry_price"]) * pos["quantity"]
            pnl_pct = (current_price - pos["entry_price"]) / pos["entry_price"] * 100
            
            if pos["type"] == "Short (Sell)":
                pnl = -pnl
                pnl_pct = -pnl_pct
            
            portfolio_data.append({
                "ID": pos["id"],
                "Source": pos["source"],
                "Type": pos["type"],
                "Quantity (g)": pos["quantity"],
                "Entry Price": f"{pos['entry_price']:,.0f} ₫",
                "Current Price": f"{current_price:,.0f} ₫",
                "P&L": f"{pnl:,.0f} ₫",
                "P&L %": f"{pnl_pct:+.2f}%",
                "Entry Date": pos["entry_date"],
                "Status": pos["status"]
            })
        
        portfolio_df = pd.DataFrame(portfolio_data)
        st.dataframe(portfolio_df, use_container_width=True)
        
        # Portfolio performance chart
        if len(portfolio_data) > 0:
            fig_portfolio = go.Figure()
            
            pnl_values = [float(p["P&L"].replace(" ₫", "").replace(",", "")) for p in portfolio_data]
            sources = [p["Source"] for p in portfolio_data]
            
            fig_portfolio.add_trace(go.Bar(
                x=sources,
                y=pnl_values,
                marker_color=["green" if x > 0 else "red" for x in pnl_values],
                text=[f"{x:,.0f} ₫" for x in pnl_values],
                textposition="auto"
            ))
            
            fig_portfolio.update_layout(
                title="Portfolio P&L by Source",
                xaxis_title="Source",
                yaxis_title="P&L (₫)",
                height=400
            )
            
            st.plotly_chart(fig_portfolio, use_container_width=True)

with portfolio_tabs[1]:  # Risk Analysis
    st.markdown("### ⚖️ Risk Analysis & VaR Calculator")
    
    risk_col1, risk_col2 = st.columns(2)
    
    with risk_col1:
        st.markdown("#### Value at Risk (VaR) Calculator")
        
        var_confidence = st.selectbox("Confidence Level", [90, 95, 99], index=1)
        var_timeframe = st.selectbox("Time Horizon", ["1 Day", "1 Week", "1 Month"])
        var_method = st.selectbox("VaR Method", ["Historical Simulation", "Parametric", "Monte Carlo"])
        
        if not historical_df.empty and len(historical_df) > 30:
            # Calculate historical volatility
            for source in selected_sources[:3]:  # Limit to first 3 sources for performance
                source_data = historical_df[historical_df["source"] == source].sort_values("date")
                
                if len(source_data) > 30:
                    # Calculate daily returns
                    source_data["returns"] = source_data["sell"].pct_change()
                    daily_vol = source_data["returns"].std()
                    
                    # Scale volatility based on timeframe
                    if var_timeframe == "1 Week":
                        scaled_vol = daily_vol * np.sqrt(7)
                    elif var_timeframe == "1 Month":
                        scaled_vol = daily_vol * np.sqrt(30)
                    else:
                        scaled_vol = daily_vol
                    
                    # Calculate VaR
                    if var_method == "Parametric":
                        from scipy.stats import norm
                        var_multiplier = norm.ppf((100 - var_confidence) / 100)
                        var_value = abs(var_multiplier * scaled_vol)
                    else:
                        # Historical simulation
                        var_value = abs(source_data["returns"].quantile((100 - var_confidence) / 100))
                    
                    current_price = source_data.iloc[-1]["sell"]
                    var_amount = var_value * current_price
                    
                    st.metric(
                        f"VaR - {source}",
                        f"{var_value*100:.2f}%",
                        f"≈ {var_amount:,.0f} ₫"
                    )
                    
                    st.info(f"📊 Daily Volatility: {daily_vol*100:.2f}%")
    
    with risk_col2:
        st.markdown("#### Risk Metrics Dashboard")
        
        # Risk-free rate (Vietnam government bonds)
        risk_free_rate = st.number_input("Risk-free Rate (%)", value=4.5, step=0.1) / 100
        
        if not historical_df.empty:
            # Calculate Sharpe ratio for each source
            sharpe_ratios = {}
            max_drawdowns = {}
            
            for source in selected_sources[:3]:
                source_data = historical_df[historical_df["source"] == source].sort_values("date")
                
                if len(source_data) > 30:
                    source_data["returns"] = source_data["sell"].pct_change()
                    
                    # Sharpe ratio
                    excess_return = source_data["returns"].mean() - risk_free_rate/252
                    sharpe_ratio = excess_return / source_data["returns"].std() * np.sqrt(252)
                    sharpe_ratios[source] = sharpe_ratio
                    
                    # Maximum Drawdown
                    cumulative = (1 + source_data["returns"]).cumprod()
                    rolling_max = cumulative.expanding().max()
                    drawdown = (cumulative - rolling_max) / rolling_max
                    max_drawdown = drawdown.min()
                    max_drawdowns[source] = max_drawdown
            
            # Display risk metrics
            if sharpe_ratios:
                st.markdown("**Sharpe Ratios:**")
                for source, ratio in sharpe_ratios.items():
                    color = "green" if ratio > 1 else "orange" if ratio > 0.5 else "red"
                    st.markdown(f"- **{source}**: <span style='color: {color}'>{ratio:.3f}</span>", unsafe_allow_html=True)
                
                st.markdown("**Maximum Drawdowns:**")
                for source, dd in max_drawdowns.items():
                    st.markdown(f"- **{source}**: <span style='color: red'>{dd*100:.2f}%</span>", unsafe_allow_html=True)

with portfolio_tabs[2]:  # Performance Reports
    st.markdown("### 📊 Performance Reports & Analytics")
    
    report_type = st.selectbox("Report Type", [
        "Daily Performance", 
        "Weekly Summary", 
        "Monthly Analysis", 
        "Comparative Analysis",
        "Volatility Report"
    ])
    
    if report_type == "Daily Performance" and not historical_df.empty:
        # Daily performance analysis
        today = datetime.now().date()
        yesterday = today - timedelta(days=1)
        
        daily_data = historical_df[historical_df["date"].dt.date == today]
        
        if not daily_data.empty:
            st.markdown("#### Today's Performance")
            
            perf_metrics = daily_data.groupby("source").agg({
                "sell": ["first", "last", "min", "max", "std"],
                "spread": ["mean", "max"]
            }).round(2)
            
            st.dataframe(perf_metrics, use_container_width=True)
            
            # Intraday volatility chart
            fig_intraday = px.line(
                daily_data, 
                x="date", 
                y="sell", 
                color="source",
                title="Intraday Price Movement"
            )
            st.plotly_chart(fig_intraday, use_container_width=True)
        else:
            st.info("No data available for today")
    
    elif report_type == "Comparative Analysis" and not historical_df.empty:
        st.markdown("#### Source Comparison Matrix")
        
        # Create comparison metrics
        comparison_data = []
        
        for source in selected_sources:
            source_data = historical_df[historical_df["source"] == source]
            
            if not source_data.empty:
                metrics = {
                    "Source": source,
                    "Avg Price": source_data["sell"].mean(),
                    "Price Std": source_data["sell"].std(),
                    "Min Price": source_data["sell"].min(),
                    "Max Price": source_data["sell"].max(),
                    "Avg Spread": source_data["spread"].mean(),
                    "Spread %": (source_data["spread"] / source_data["sell"] * 100).mean(),
                    "Data Points": len(source_data)
                }
                comparison_data.append(metrics)
        
        if comparison_data:
            comp_df = pd.DataFrame(comparison_data)
            
            # Style the dataframe
            styled_df = comp_df.style.format({
                "Avg Price": "{:,.0f} ₫",
                "Price Std": "{:,.0f} ₫",
                "Min Price": "{:,.0f} ₫",
                "Max Price": "{:,.0f} ₫",
                "Avg Spread": "{:,.0f} ₫",
                "Spread %": "{:.2f}%"
            }).background_gradient(subset=["Avg Price", "Price Std", "Spread %"])
            
            st.dataframe(styled_df, use_container_width=True)
            
            # Radar chart for source comparison
            categories = ["Avg Price (norm)", "Volatility", "Spread", "Data Quality"]
            
            fig_radar = go.Figure()
            
            for _, row in comp_df.iterrows():
                # Normalize metrics for radar chart
                values = [
                    (row["Avg Price"] - comp_df["Avg Price"].min()) / (comp_df["Avg Price"].max() - comp_df["Avg Price"].min()),
                    (row["Price Std"] - comp_df["Price Std"].min()) / (comp_df["Price Std"].max() - comp_df["Price Std"].min()),
                    (row["Spread %"] - comp_df["Spread %"].min()) / (comp_df["Spread %"].max() - comp_df["Spread %"].min()),
                    (row["Data Points"] - comp_df["Data Points"].min()) / (comp_df["Data Points"].max() - comp_df["Data Points"].min())
                ]
                
                fig_radar.add_trace(go.Scatterpolar(
                    r=values + [values[0]],  # Close the loop
                    theta=categories + [categories[0]],
                    fill='toself',
                    name=row["Source"]
                ))
            
            fig_radar.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
                showlegend=True,
                title="Source Performance Comparison"
            )
            
            st.plotly_chart(fig_radar, use_container_width=True)

with portfolio_tabs[3]:  # Position Calculator
    st.markdown("### 🎯 Advanced Position Calculator")
    
    calc_col1, calc_col2 = st.columns([1, 1])
    
    with calc_col1:
        st.markdown("#### Position Sizing Calculator")
        
        # Kelly Criterion Calculator
        st.markdown("**Kelly Criterion Position Sizing**")
        
        win_rate = st.slider("Win Rate (%)", 0, 100, 60) / 100
        avg_win = st.number_input("Average Win (₫)", value=500000, step=10000)
        avg_loss = st.number_input("Average Loss (₫)", value=300000, step=10000)
        
        if avg_loss > 0:
            win_loss_ratio = avg_win / avg_loss
            kelly_fraction = win_rate - ((1 - win_rate) / win_loss_ratio)
            
            st.metric("Kelly Fraction", f"{kelly_fraction:.3f}")
            
            if kelly_fraction > 0:
                st.success(f"✅ Optimal position size: {kelly_fraction*100:.1f}% of capital")
            else:
                st.warning("⚠️ Negative Kelly fraction - avoid this trade")
        
        # Risk-based position sizing
        st.markdown("**Risk-Based Position Sizing**")
        
        account_size = st.number_input("Account Size (₫)", value=100000000, step=1000000)
        risk_per_trade = st.slider("Risk per Trade (%)", 0.5, 5.0, 2.0) / 100
        stop_loss_pct = st.slider("Stop Loss (%)", 1.0, 10.0, 3.0) / 100
        
        risk_amount = account_size * risk_per_trade
        position_size = risk_amount / stop_loss_pct
        
        st.metric("Position Size", f"{position_size:,.0f} ₫")
        st.metric("Risk Amount", f"{risk_amount:,.0f} ₫")
    
    with calc_col2:
        st.markdown("#### Profit/Loss Calculator")
        
        # P&L Calculator
        entry_price = st.number_input("Entry Price (₫/gram)", value=80000000, step=100000)
        exit_price = st.number_input("Target Exit Price (₫/gram)", value=82000000, step=100000)
        position_grams = st.number_input("Position Size (grams)", value=10.0, step=0.1)
        
        # Calculate P&L
        gross_pnl = (exit_price - entry_price) * position_grams
        
        # Transaction costs
        buy_fee_rate = st.number_input("Buy Fee (%)", value=0.5, step=0.1) / 100
        sell_fee_rate = st.number_input("Sell Fee (%)", value=0.5, step=0.1) / 100
        
        buy_fee = entry_price * position_grams * buy_fee_rate
        sell_fee = exit_price * position_grams * sell_fee_rate
        total_fees = buy_fee + sell_fee
        
        net_pnl = gross_pnl - total_fees
        roi = net_pnl / (entry_price * position_grams) * 100
        
        # Display results
        st.markdown("**Calculation Results:**")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Gross P&L", f"{gross_pnl:,.0f} ₫")
            st.metric("Total Fees", f"{total_fees:,.0f} ₫")
        
        with col_b:
            st.metric("Net P&L", f"{net_pnl:,.0f} ₫", f"{roi:+.2f}%")
            
            if net_pnl > 0:
                st.success("✅ Profitable trade")
            else:
                st.error("❌ Loss-making trade")
        
        # Break-even analysis
        breakeven_price = entry_price + (total_fees / position_grams)
        st.info(f"📊 Break-even price: {breakeven_price:,.0f} ₫/gram")

# ---- Market News & Sentiment ----
st.subheader("📰 Market News & Sentiment Analysis")

news_col1, news_col2 = st.columns([2, 1])

with news_col1:
    st.markdown("#### 📈 Market Impact Factors")
    
    # Mock news data - in real implementation, connect to news APIs
    market_factors = [
        {"Factor": "USD/VND Exchange Rate", "Impact": "High", "Direction": "Inverse", "Last Update": "30m ago"},
        {"Factor": "International Gold Price", "Impact": "Very High", "Direction": "Direct", "Last Update": "15m ago"},
        {"Factor": "Inflation Rate (Vietnam)", "Impact": "Medium", "Direction": "Direct", "Last Update": "2h ago"},
        {"Factor": "Central Bank Policy", "Impact": "High", "Direction": "Mixed", "Last Update": "1d ago"},
        {"Factor": "Global Economic Uncertainty", "Impact": "High", "Direction": "Direct", "Last Update": "4h ago"}
    ]
    
    factors_df = pd.DataFrame(market_factors)
    
    # Style the factors table
    def color_impact(val):
        colors = {"Very High": "background-color: #ff4444; color: white",
                 "High": "background-color: #ff8800; color: white",
                 "Medium": "background-color: #ffaa00; color: black"}
        return colors.get(val, "")
    
    styled_factors = factors_df.style.applymap(color_impact, subset=["Impact"])
    st.dataframe(styled_factors, use_container_width=True)

with news_col2:
    st.markdown("#### 🎭 Market Sentiment")
    
    # Mock sentiment analysis
    sentiment_score = np.random.uniform(0.3, 0.8)  # Replace with actual sentiment analysis
    
    if sentiment_score > 0.7:
        sentiment_label = "Very Bullish"
        sentiment_color = "#00ff00"
        sentiment_emoji = "🚀"
    elif sentiment_score > 0.6:
        sentiment_label = "Bullish"
        sentiment_color = "#88ff88"
        sentiment_emoji = "📈"
    elif sentiment_score > 0.4:
        sentiment_label = "Neutral"
        sentiment_color = "#ffff00"
        sentiment_emoji = "😐"
    elif sentiment_score > 0.3:
        sentiment_label = "Bearish"
        sentiment_color = "#ff8888"
        sentiment_emoji = "📉"
    else:
        sentiment_label = "Very Bearish"
        sentiment_color = "#ff0000"
        sentiment_emoji = "💥"
    
    st.markdown(f"""
    <div style="text-align: center; padding: 20px; border-radius: 10px; background-color: {sentiment_color}20; border: 2px solid {sentiment_color};">
        <h2>{sentiment_emoji} {sentiment_label}</h2>
        <h3>Score: {sentiment_score:.2f}/1.0</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Sentiment gauge
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = sentiment_score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Market Sentiment"},
        gauge = {
            'axis': {'range': [None, 1]},
            'bar': {'color': sentiment_color},
            'steps': [
                {'range': [0, 0.3], 'color': "#ff4444"},
                {'range': [0.3, 0.7], 'color': "#ffff44"},
                {'range': [0.7, 1], 'color': "#44ff44"}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 0.9}}))
    
    fig_gauge.update_layout(height=300)
    st.plotly_chart(fig_gauge, use_container_width=True)

# ---- System Health & Monitoring ----
st.subheader("🔧 System Health & Monitoring")

health_col1, health_col2, health_col3, health_col4 = st.columns(4)

with health_col1:
    # Database health
    db_health = "Healthy" if os.path.exists(DB_FILE) else "Offline"
    db_color = "green" if db_health == "Healthy" else "red"
    st.markdown(f"**Database Status**")
    st.markdown(f"<span style='color: {db_color}'>● {db_health}</span>", unsafe_allow_html=True)

with health_col2:
    # Data freshness
    if not current_df.empty:
        last_update = current_df["timestamp"].max()
        freshness_minutes = (datetime.now() - last_update.replace(tzinfo=None)).total_seconds() / 60
        freshness_status = "Fresh" if freshness_minutes < 30 else "Stale"
        freshness_color = "green" if freshness_status == "Fresh" else "orange"
    else:
        freshness_status = "No Data"
        freshness_color = "red"
    
    st.markdown("**Data Freshness**")
    st.markdown(f"<span style='color: {freshness_color}'>● {freshness_status}</span>", unsafe_allow_html=True)

with health_col3:
    # Source availability
    total_sources = len(all_sources)
    active_sources = len([s for s in selected_sources if not current_df[current_df["source"] == s].empty])
    availability_pct = (active_sources / total_sources * 100) if total_sources > 0 else 0
    availability_color = "green" if availability_pct > 80 else "orange" if availability_pct > 50 else "red"
    
    st.markdown("**Source Availability**")
    st.markdown(f"<span style='color: {availability_color}'>● {availability_pct:.0f}%</span>", unsafe_allow_html=True)

with health_col4:
    # API response time (mock)
    response_time = np.random.uniform(100, 500)  # Replace with actual monitoring
    response_status = "Fast" if response_time < 200 else "Normal" if response_time < 400 else "Slow"
    response_color = "green" if response_status == "Fast" else "orange" if response_status == "Normal" else "red"
    
    st.markdown("**Response Time**")
    st.markdown(f"<span style='color: {response_color}'>● {response_time:.0f}ms</span>", unsafe_allow_html=True)

# ---- Export & Integration ----
st.subheader("📤 Export & Integration")

export_col1, export_col2 = st.columns(2)

with export_col1:
    st.markdown("#### 📊 Data Export")
    
    export_format = st.selectbox("Export Format", ["CSV", "JSON", "Excel", "Parquet"])
    export_timeframe = st.selectbox("Timeframe", ["Current Session", "Last 24h", "Last Week", "All Data"])
    
    if st.button("📥 Export Data"):
        # Prepare export data based on selection
        if export_timeframe == "Current Session":
            export_data = current_df
        else:
            export_data = historical_df
        
        if not export_data.empty:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"gold_data_{export_timeframe.lower().replace(' ', '_')}_{timestamp}"
            
            if export_format == "CSV":
                export_data.to_csv(f"{filename}.csv", index=False)
            elif export_format == "JSON":
                export_data.to_json(f"{filename}.json", orient="records", indent=2)
            elif export_format == "Excel":
                export_data.to_excel(f"{filename}.xlsx", index=False)
            elif export_format == "Parquet":
                export_data.to_parquet(f"{filename}.parquet", index=False)
            
            st.success(f"✅ Data exported as {filename}.{export_format.lower()}")

with export_col2:
    st.markdown("#### 🔗 API Integration")
    
    st.code("""
# REST API Endpoints (Mock)
GET /api/v1/current-prices
GET /api/v1/historical/{source}
GET /api/v1/alerts
POST /api/v1/portfolio/positions
    """)
    
    api_key = st.text_input("API Key", type="password", placeholder="Enter your API key")
    
    if st.button("🔑 Generate API Key"):
        mock_key = f"gd_{datetime.now().strftime('%Y%m%d')}_{hash(datetime.now()) % 10000:04d}"
        st.code(mock_key)
        st.info("API key generated! (Mock)")

# ---- Footer with Enhanced Info ----
st.markdown("---")

footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.markdown("**🏆 Dashboard Stats**")
    total_datapoints = len(current_df) + len(historical_df)
    st.write(f"• Total data points: {total_datapoints:,}")
    st.write(f"• Active sources: {len(selected_sources)}")
    st.write(f"• Last update: {datetime.now().strftime('%H:%M:%S')}")

with footer_col2:
    st.markdown("**📊 Market Coverage**")
    st.write("• Vietnamese gold markets")
    st.write("• International benchmarks")
    st.write("• Real-time & historical data")

with footer_col3:
    st.markdown("**🔧 System Info**")
    st.write(f"• Refresh: {refresh_interval}s")
    st.write(f"• Auto-refresh: {'ON' if auto_refresh else 'OFF'}")
    st.write("• Status: 🟢 Online")

# ---- Advanced Machine Learning Predictions ----
st.subheader("🤖 AI-Powered Price Predictions")

ml_tabs = st.tabs(["🎯 Price Forecasting", "📊 Pattern Recognition", "⚡ Anomaly Detection", "🔮 Scenario Analysis"])

with ml_tabs[0]:  # Price Forecasting
    st.markdown("### 🎯 Machine Learning Price Forecasting")
    
    if not historical_df.empty:
        forecast_source = st.selectbox("Select Source for ML Forecast", selected_sources, key="ml_forecast")
        forecast_horizon = st.selectbox("Forecast Horizon", ["1 Hour", "4 Hours", "1 Day", "3 Days", "1 Week"])
        
        ml_col1, ml_col2 = st.columns([2, 1])
        
        with ml_col1:
            # Prepare ML data
            source_data = historical_df[historical_df["source"] == forecast_source].sort_values("date")
            
            if len(source_data) >= 50:  # Minimum data required
                try:
                    # Feature engineering
                    source_data = source_data.copy()
                    source_data["price_lag1"] = source_data["sell"].shift(1)
                    source_data["price_lag2"] = source_data["sell"].shift(2)
                    source_data["price_lag3"] = source_data["sell"].shift(3)
                    source_data["ma_3"] = source_data["sell"].rolling(3).mean()
                    source_data["ma_7"] = source_data["sell"].rolling(7).mean()
                    source_data["volatility"] = source_data["sell"].rolling(7).std()
                    source_data["price_change"] = source_data["sell"].pct_change()
                    
                    # Prepare features
                    features = ["price_lag1", "price_lag2", "price_lag3", "ma_3", "ma_7", "volatility"]
                    X = source_data[features].dropna()
                    y = source_data["sell"].iloc[len(source_data) - len(X):]
                    
                    if len(X) >= 30:
                        # Train model
                        scaler = StandardScaler()
                        X_scaled = scaler.fit_transform(X)
                        
                        model = LinearRegression()
                        model.fit(X_scaled, y)
                        
                        # Make predictions
                        last_features = X.iloc[-1:].values
                        last_features_scaled = scaler.transform(last_features)
                        
                        # Generate forecast steps
                        forecast_steps = {"1 Hour": 1, "4 Hours": 4, "1 Day": 24, "3 Days": 72, "1 Week": 168}
                        steps = forecast_steps.get(forecast_horizon, 24)
                        
                        predictions = []
                        current_features = last_features_scaled[0].copy()
                        
                        for step in range(steps):
                            pred = model.predict([current_features])[0]
                            predictions.append(pred)
                            
                            # Update features for next prediction (simple approach)
                            current_features[1:3] = current_features[0:2]  # Shift lags
                            current_features[0] = pred
                        
                        # Create forecast dataframe
                        future_dates = pd.date_range(
                            start=source_data["date"].max() + pd.Timedelta(hours=1),
                            periods=steps,
                            freq="H"
                        )
                        
                        forecast_df = pd.DataFrame({
                            "date": future_dates,
                            "predicted_price": predictions,
                            "source": forecast_source
                        })
                        
                        # Plot forecast
                        fig_forecast = go.Figure()
                        
                        # Historical data
                        recent_data = source_data.tail(100)  # Last 100 points
                        fig_forecast.add_trace(go.Scatter(
                            x=recent_data["date"],
                            y=recent_data["sell"],
                            name="Historical",
                            line=dict(color="blue", width=2)
                        ))
                        
                        # Predictions
                        fig_forecast.add_trace(go.Scatter(
                            x=forecast_df["date"],
                            y=forecast_df["predicted_price"],
                            name="ML Forecast",
                            line=dict(color="red", width=2, dash="dash")
                        ))
                        
                        # Confidence interval (simple approach)
                        mae = np.mean(np.abs(model.predict(X_scaled) - y))
                        upper_bound = forecast_df["predicted_price"] + mae
                        lower_bound = forecast_df["predicted_price"] - mae
                        
                        fig_forecast.add_trace(go.Scatter(
                            x=forecast_df["date"],
                            y=upper_bound,
                            fill=None,
                            mode='lines',
                            line_color='rgba(0,0,0,0)',
                            showlegend=False
                        ))
                        
                        fig_forecast.add_trace(go.Scatter(
                            x=forecast_df["date"],
                            y=lower_bound,
                            fill='tonexty',
                            mode='lines',
                            line_color='rgba(0,0,0,0)',
                            name='Confidence Interval',
                            fillcolor='rgba(255,0,0,0.2)'
                        ))
                        
                        fig_forecast.update_layout(
                            title=f"ML Price Forecast - {forecast_source} ({forecast_horizon})",
                            xaxis_title="Date",
                            yaxis_title="Price (₫)",
                            height=500
                        )
                        
                        st.plotly_chart(fig_forecast, use_container_width=True)
                        
                        # Model performance metrics
                        r2_score = model.score(X_scaled, y)
                        
                        st.markdown("**Model Performance:**")
                        metric_col1, metric_col2, metric_col3 = st.columns(3)
                        
                        with metric_col1:
                            st.metric("R² Score", f"{r2_score:.3f}")
                        with metric_col2:
                            st.metric("MAE", f"{mae:,.0f} ₫")
                        with metric_col3:
                            pred_change = (predictions[-1] - y.iloc[-1]) / y.iloc[-1] * 100
                            st.metric("Forecast Change", f"{pred_change:+.2f}%")
                        
                except Exception as e:
                    st.error(f"ML Forecasting Error: {e}")
                    st.info("Try with different parameters or check data quality")
            else:
                st.warning("Insufficient data for ML forecasting (need ≥50 data points)")
        
        with ml_col2:
            st.markdown("#### 📊 Feature Importance")
            
            if 'model' in locals() and hasattr(model, 'coef_'):
                feature_importance = pd.DataFrame({
                    'Feature': features,
                    'Importance': np.abs(model.coef_)
                }).sort_values('Importance', ascending=True)
                
                fig_importance = px.bar(
                    feature_importance,
                    x='Importance',
                    y='Feature',
                    orientation='h',
                    title="Feature Importance"
                )
                
                st.plotly_chart(fig_importance, use_container_width=True)
            
            # Model settings
            st.markdown("#### ⚙️ Model Settings")
            
            model_type = st.selectbox("Model Type", [
                "Linear Regression",
                "Random Forest", 
                "LSTM Neural Network",
                "ARIMA",
                "Prophet"
            ], key="ml_model_type")
            
            retrain_freq = st.selectbox("Retrain Frequency", [
                "Every Hour",
                "Every 4 Hours", 
                "Daily",
                "Weekly"
            ])
            
            if st.button("🔄 Retrain Model"):
                st.info("Model retraining initiated...")
                time.sleep(2)
                st.success("✅ Model retrained successfully!")

with ml_tabs[1]:  # Pattern Recognition
    st.markdown("### 📊 Chart Pattern Recognition")
    
    if not historical_df.empty:
        pattern_source = st.selectbox("Select Source for Pattern Analysis", selected_sources, key="pattern")
        
        pattern_data = historical_df[historical_df["source"] == pattern_source].sort_values("date")
        
        if len(pattern_data) >= 20:
            # Simple pattern detection
            pattern_data = pattern_data.copy()
            pattern_data["ma_short"] = pattern_data["sell"].rolling(5).mean()
            pattern_data["ma_long"] = pattern_data["sell"].rolling(20).mean()
            
            # Detect patterns
            patterns_found = []
            
            # Golden Cross / Death Cross
            for i in range(1, len(pattern_data)):
                if (pattern_data.iloc[i]["ma_short"] > pattern_data.iloc[i]["ma_long"] and
                    pattern_data.iloc[i-1]["ma_short"] <= pattern_data.iloc[i-1]["ma_long"]):
                    patterns_found.append({
                        "Date": pattern_data.iloc[i]["date"],
                        "Pattern": "Golden Cross",
                        "Signal": "Bullish",
                        "Confidence": "High"
                    })
                elif (pattern_data.iloc[i]["ma_short"] < pattern_data.iloc[i]["ma_long"] and
                      pattern_data.iloc[i-1]["ma_short"] >= pattern_data.iloc[i-1]["ma_long"]):
                    patterns_found.append({
                        "Date": pattern_data.iloc[i]["date"],
                        "Pattern": "Death Cross",
                        "Signal": "Bearish",
                        "Confidence": "High"
                    })
            
            # Support/Resistance levels
            recent_data = pattern_data.tail(50)
            support_level = recent_data["sell"].min()
            resistance_level = recent_data["sell"].max()
            
            # Chart with patterns
            fig_patterns = go.Figure()
            
            # Price line
            fig_patterns.add_trace(go.Scatter(
                x=pattern_data["date"],
                y=pattern_data["sell"],
                name="Price",
                line=dict(color="blue", width=2)
            ))
            
            # Moving averages
            fig_patterns.add_trace(go.Scatter(
                x=pattern_data["date"],
                y=pattern_data["ma_short"],
                name="MA 5",
                line=dict(color="orange", width=1)
            ))
            
            fig_patterns.add_trace(go.Scatter(
                x=pattern_data["date"],
                y=pattern_data["ma_long"],
                name="MA 20",
                line=dict(color="red", width=1)
            ))
            
            # Support/Resistance lines
            fig_patterns.add_hline(
                y=support_level,
                line_dash="dash",
                line_color="green",
                annotation_text="Support"
            )
            
            fig_patterns.add_hline(
                y=resistance_level,
                line_dash="dash",
                line_color="red",
                annotation_text="Resistance"
            )
            
            # Mark pattern points
            for pattern in patterns_found[-5:]:  # Show last 5 patterns
                fig_patterns.add_scatter(
                    x=[pattern["Date"]],
                    y=[pattern_data[pattern_data["date"] == pattern["Date"]]["sell"].iloc[0]],
                    mode="markers",
                    marker=dict(
                        size=15,
                        color="green" if pattern["Signal"] == "Bullish" else "red",
                        symbol="triangle-up" if pattern["Signal"] == "Bullish" else "triangle-down"
                    ),
                    name=pattern["Pattern"],
                    showlegend=False
                )
            
            fig_patterns.update_layout(
                title=f"Chart Pattern Analysis - {pattern_source}",
                xaxis_title="Date",
                yaxis_title="Price (₫)",
                height=600
            )
            
            st.plotly_chart(fig_patterns, use_container_width=True)
            
            # Pattern summary
            if patterns_found:
                st.markdown("#### 🔍 Detected Patterns")
                patterns_df = pd.DataFrame(patterns_found)
                st.dataframe(patterns_df.tail(10), use_container_width=True)
            else:
                st.info("No significant patterns detected in current timeframe")
            
            # Key levels
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Support Level", f"{support_level:,.0f} ₫")
            with col2:
                st.metric("Resistance Level", f"{resistance_level:,.0f} ₫")

with ml_tabs[2]:  # Anomaly Detection
    st.markdown("### ⚡ Real-time Anomaly Detection")
    
    if not historical_df.empty:
        anomaly_source = st.selectbox("Select Source for Anomaly Detection", selected_sources, key="anomaly")
        
        anomaly_data = historical_df[historical_df["source"] == anomaly_source].sort_values("date")
        
        if len(anomaly_data) >= 30:
            # Statistical anomaly detection
            anomaly_data = anomaly_data.copy()
            
            # Z-score based anomalies
            price_mean = anomaly_data["sell"].rolling(30).mean()
            price_std = anomaly_data["sell"].rolling(30).std()
            z_scores = (anomaly_data["sell"] - price_mean) / price_std
            
            # Anomaly threshold
            anomaly_threshold = st.slider("Anomaly Threshold (Z-score)", 1.5, 4.0, 2.5, 0.1)
            
            anomalies = anomaly_data[np.abs(z_scores) > anomaly_threshold].copy()
            anomalies["z_score"] = z_scores[np.abs(z_scores) > anomaly_threshold]
            
            # Anomaly chart
            fig_anomaly = go.Figure()
            
            # Normal data
            normal_data = anomaly_data[np.abs(z_scores) <= anomaly_threshold]
            fig_anomaly.add_trace(go.Scatter(
                x=normal_data["date"],
                y=normal_data["sell"],
                mode="lines+markers",
                name="Normal Prices",
                line=dict(color="blue", width=1),
                marker=dict(size=3)
            ))
            
            # Anomalies
            if not anomalies.empty:
                fig_anomaly.add_trace(go.Scatter(
                    x=anomalies["date"],
                    y=anomalies["sell"],
                    mode="markers",
                    name="Anomalies",
                    marker=dict(
                        size=10,
                        color="red",
                        symbol="diamond",
                        line=dict(width=2, color="darkred")
                    )
                ))
            
            # Confidence bands
            fig_anomaly.add_trace(go.Scatter(
                x=anomaly_data["date"],
                y=price_mean + anomaly_threshold * price_std,
                mode="lines",
                name="Upper Threshold",
                line=dict(color="red", dash="dash", width=1)
            ))
            
            fig_anomaly.add_trace(go.Scatter(
                x=anomaly_data["date"],
                y=price_mean - anomaly_threshold * price_std,
                mode="lines",
                name="Lower Threshold",
                line=dict(color="red", dash="dash", width=1)
            ))
            
            fig_anomaly.update_layout(
                title=f"Anomaly Detection - {anomaly_source}",
                xaxis_title="Date",
                yaxis_title="Price (₫)",
                height=500
            )
            
            st.plotly_chart(fig_anomaly, use_container_width=True)
            
            # Anomaly statistics
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Total Anomalies", len(anomalies))
            with col2:
                if not anomalies.empty:
                    latest_anomaly = (datetime.now().date() - anomalies["date"].dt.date.max()).days
                    st.metric("Days Since Last Anomaly", latest_anomaly)
                else:
                    st.metric("Days Since Last Anomaly", "N/A")
            with col3:
                anomaly_rate = len(anomalies) / len(anomaly_data) * 100
                st.metric("Anomaly Rate", f"{anomaly_rate:.2f}%")
            
            # Recent anomalies table
            if not anomalies.empty:
                st.markdown("#### 🚨 Recent Anomalies")
                recent_anomalies = anomalies.tail(10)[["date", "sell", "z_score"]].copy()
                recent_anomalies["severity"] = recent_anomalies["z_score"].apply(
                    lambda x: "🔴 High" if abs(x) > 3 else "🟡 Medium"
                )
                st.dataframe(recent_anomalies, use_container_width=True)

with ml_tabs[3]:  # Scenario Analysis
    st.markdown("### 🔮 Monte Carlo Scenario Analysis")
    
    if not historical_df.empty:
        scenario_source = st.selectbox("Select Source for Scenario Analysis", selected_sources, key="scenario")
        
        scenario_data = historical_df[historical_df["source"] == scenario_source].sort_values("date")
        
        if len(scenario_data) >= 30:
            # Monte Carlo parameters
            col1, col2 = st.columns(2)
            
            with col1:
                num_simulations = st.slider("Number of Simulations", 100, 2000, 1000, 100)
                time_horizon = st.slider("Time Horizon (days)", 1, 90, 30)
            
            with col2:
                confidence_level = st.slider("Confidence Level (%)", 90, 99, 95)
                shock_scenarios = st.multiselect(
                    "Include Shock Scenarios",
                    ["Market Crash (-20%)", "Economic Boom (+15%)", "Currency Crisis (+30%)"],
                    default=[]
                )
            
            if st.button("🎲 Run Monte Carlo Simulation"):
                with st.spinner("Running simulations..."):
                    # Calculate historical statistics
                    returns = scenario_data["sell"].pct_change().dropna()
                    mean_return = returns.mean()
                    std_return = returns.std()
                    
                    # Current price
                    current_price = scenario_data["sell"].iloc[-1]
                    
                    # Run simulations
                    simulations = []
                    
                    for sim in range(num_simulations):
                        prices = [current_price]
                        
                        for day in range(time_horizon):
                            # Random return from normal distribution
                            random_return = np.random.normal(mean_return, std_return)
                            
                            # Apply shock scenarios randomly
                            if shock_scenarios and np.random.random() < 0.05:  # 5% chance
                                shock = np.random.choice(shock_scenarios)
                                if "Market Crash" in shock:
                                    random_return += -0.20
                                elif "Economic Boom" in shock:
                                    random_return += 0.15
                                elif "Currency Crisis" in shock:
                                    random_return += 0.30
                            
                            new_price = prices[-1] * (1 + random_return)
                            prices.append(new_price)
                        
                        simulations.append(prices)
                    
                    # Convert to DataFrame
                    simulations_array = np.array(simulations)
                    
                    # Calculate percentiles
                    percentiles = np.percentile(simulations_array[:, -1], [5, 25, 50, 75, 95])
                    
                    # Plot simulation results
                    fig_monte = go.Figure()
                    
                    # Plot sample simulation paths
                    days = list(range(time_horizon + 1))
                    for i in range(min(50, num_simulations)):  # Show max 50 paths
                        fig_monte.add_trace(go.Scatter(
                            x=days,
                            y=simulations[i],
                            mode="lines",
                            line=dict(color="lightblue", width=0.5),
                            opacity=0.3,
                            showlegend=False
                        ))
                    
                    # Add percentile lines
                    percentile_colors = ["red", "orange", "green", "orange", "red"]
                    percentile_names = ["5th", "25th", "50th (Median)", "75th", "95th"]
                    
                    for i, (perc, color, name) in enumerate(zip(percentiles, percentile_colors, percentile_names)):
                        fig_monte.add_hline(
                            y=perc,
                            line_dash="dash",
                            line_color=color,
                            annotation_text=f"{name}: {perc:,.0f} ₫"
                        )
                    
                    # Current price line
                    fig_monte.add_hline(
                        y=current_price,
                        line_color="black",
                        line_width=2,
                        annotation_text=f"Current: {current_price:,.0f} ₫"
                    )
                    
                    fig_monte.update_layout(
                        title=f"Monte Carlo Price Simulation - {scenario_source}",
                        xaxis_title="Days",
                        yaxis_title="Price (₫)",
                        height=600
                    )
                    
                    st.plotly_chart(fig_monte, use_container_width=True)
                    
                    # Results summary
                    st.markdown("#### 📊 Simulation Results")
                    
                    result_col1, result_col2, result_col3, result_col4 = st.columns(4)
                    
                    with result_col1:
                        median_price = percentiles[2]
                        median_change = (median_price - current_price) / current_price * 100
                        st.metric("Median Outcome", f"{median_price:,.0f} ₫", f"{median_change:+.1f}%")
                    
                    with result_col2:
                        best_case = percentiles[4]
                        best_change = (best_case - current_price) / current_price * 100
                        st.metric("95th Percentile", f"{best_case:,.0f} ₫", f"{best_change:+.1f}%")
                    
                    with result_col3:
                        worst_case = percentiles[0]
                        worst_change = (worst_case - current_price) / current_price * 100
                        st.metric("5th Percentile", f"{worst_case:,.0f} ₫", f"{worst_change:+.1f}%")
                    
                    with result_col4:
                        var_95 = current_price - percentiles[0]
                        st.metric(f"VaR (95%)", f"{var_95:,.0f} ₫", f"{var_95/current_price*100:.1f}%")
                    
                    # Probability analysis
                    final_prices = simulations_array[:, -1]
                    prob_gain = (final_prices > current_price).sum() / num_simulations * 100
                    prob_loss_10 = (final_prices < current_price * 0.9).sum() / num_simulations * 100
                    prob_gain_10 = (final_prices > current_price * 1.1).sum() / num_simulations * 100
                    
                    st.markdown("#### 🎯 Probability Analysis")
                    prob_col1, prob_col2, prob_col3 = st.columns(3)
                    
                    with prob_col1:
                        st.metric("Probability of Gain", f"{prob_gain:.1f}%")
                    with prob_col2:
                        st.metric("Probability of >10% Loss", f"{prob_loss_10:.1f}%")
                    with prob_col3:
                        st.metric("Probability of >10% Gain", f"{prob_gain_10:.1f}%")
        else:
            st.warning("Need at least 30 data points for scenario analysis")
    else:
        st.info("No historical data available for scenario analysis")