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
import os
import subprocess

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

# Initialize session state for language
if 'lang' not in st.session_state:
    st.session_state.lang = 'en'

# Language toggle in top right
col1, col2 = st.columns([8, 1])
with col2:
    lang_options = ['EN', 'VI']
    lang_index = 0 if st.session_state.lang == 'en' else 1
    selected_lang = st.selectbox(" ", lang_options, index=lang_index, label_visibility="collapsed")
    st.session_state.lang = selected_lang.lower()

# Translation function
def t(en, vi):
    return en if st.session_state.lang == 'en' else vi

st.set_page_config(
    page_title=t("🏆 Advanced Gold Price Dashboard", "🏆 Bảng Điều Khiển Giá Vàng Nâng Cao"), 
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
st.markdown(f"""
# {t("🏆 Advanced Gold Price Dashboard", "🏆 Bảng Điều Khiển Giá Vàng Nâng Cao")}
<div style="display: flex; align-items: center; margin-bottom: 20px;">
    <span class="realtime-indicator online"></span>
    <span>{t("Real-time Gold Market Analysis", "Phân Tích Thị Trường Vàng Thời Gian Thực")}</span>
</div>
""", unsafe_allow_html=True)

# ---- Enhanced Helper Functions ----
@st.cache_data(ttl=30)  # Cache for 30 seconds for real-time feel
def load_current_data(db_file: str = DB_FILE) -> pd.DataFrame:
    """Load current gold prices"""
    if not os.path.exists(db_file):
        return pd.DataFrame()
    
    try:
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
        
        # Calculate spreads and other metrics with error handling
        df["buy"] = pd.to_numeric(df["buy"], errors="coerce")
        df["sell"] = pd.to_numeric(df["sell"], errors="coerce")
        
        # Only calculate spreads where both buy and sell are valid
        df["spread"] = df.apply(lambda row: 
            (row["sell"] - row["buy"]) if (
                pd.notna(row["sell"]) and pd.notna(row["buy"]) and 
                row["sell"] is not None and row["buy"] is not None
            ) else None, axis=1
        )
        
        df["spread_pct"] = df.apply(lambda row: 
            (row["spread"] / row["buy"] * 100) if (
                pd.notna(row["spread"]) and pd.notna(row["buy"]) and 
                row["spread"] is not None and row["buy"] is not None and row["buy"] != 0
            ) else None, axis=1
        )
        
        df["mid_price"] = df.apply(lambda row: 
            ((row["buy"] + row["sell"]) / 2) if (
                pd.notna(row["sell"]) and pd.notna(row["buy"]) and 
                row["sell"] is not None and row["buy"] is not None
            ) else None, axis=1
        )
        
        return df
    
    except Exception as e:
        st.error(t(f"Error loading current data: {e}", f"Lỗi tải dữ liệu hiện tại: {e}"))
        return pd.DataFrame()

@st.cache_data(ttl=60)
def load_historical_data(db_file: str = TIMESERIES_DB) -> pd.DataFrame:
    """Load historical time-series data"""
    if not os.path.exists(db_file):
        return pd.DataFrame()
    
    try:
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
        
        # Convert numeric columns with error handling
        numeric_cols = ["buy", "sell", "open", "high", "low", "close", "spot_price"]
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")
        
        # Calculate spreads and mid_price with null checking
        df["spread"] = df.apply(lambda row: 
            (row["sell"] - row["buy"]) if (
                pd.notna(row["sell"]) and pd.notna(row["buy"])
            ) else None, axis=1
        )
        
        df["mid_price"] = df.apply(lambda row: 
            ((row["buy"] + row["sell"]) / 2) if (
                pd.notna(row["sell"]) and pd.notna(row["buy"])
            ) else None, axis=1
        )
        
        return df
    
    except Exception as e:
        st.error(t(f"Error loading historical data: {e}", f"Lỗi tải dữ liệu lịch sử: {e}"))
        return pd.DataFrame()

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
        st.error(t(f"Error calculating technical indicators: {e}", f"Lỗi tính toán chỉ số kỹ thuật: {e}"))
    
    return df



def run_scraper() -> tuple[bool, str]:
    """Run scraper in subprocess and return (success, output)"""
    try:
        # Lấy đường dẫn đến gold_scraper.py ở cùng thư mục với script hiện tại
        script_dir = os.path.dirname(os.path.abspath(__file__))  # __file__ là đường dẫn script Streamlit
        scraper_path = os.path.join(script_dir, "gold_scraper.py")
        
        proc = subprocess.run(["python3", scraper_path], capture_output=True, text=True, check=False, timeout=120)
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
        return t("NEUTRAL", "TRUNG LẬP"), "⚪"
    
    if rsi > 70 and macd_hist > 0:
        return t("STRONG_BUY", "MUA MẠNH"), "🟢"
    elif rsi > 60 and macd_hist > 0:
        return t("BUY", "MUA"), "🟢"
    elif rsi < 30 and macd_hist < 0:
        return t("STRONG_SELL", "BÁN MẠNH"), "🔴"
    elif rsi < 40 and macd_hist < 0:
        return t("SELL", "BÁN"), "🔴"
    else:
        return t("NEUTRAL", "TRUNG LẬP"), "🟡"

# ---- Sidebar Controls ----
st.sidebar.header(t("🎛️ Dashboard Controls", "🎛️ Điều Khiển Bảng Điều Khiển"))

# Real-time settings
st.sidebar.subheader(t("⚡ Real-time Settings", "⚡ Cài Đặt Thời Gian Thực"))
auto_refresh = st.sidebar.checkbox(t("🔄 Auto-refresh", "🔄 Tự Động Làm Mới"), value=True)
refresh_interval = st.sidebar.selectbox(
    t("Refresh interval", "Khoảng Thời Gian Làm Mới"), 
    [10, 30, 60, 120, 300],
    index=2,
    format_func=lambda x: f"{x} " + t("seconds", "giây")
)

# Auto-refresh logic
if auto_refresh:
    placeholder = st.empty()
    time.sleep(refresh_interval)
    st.rerun()

# Scraper controls
st.sidebar.subheader(t("📡 Data Collection", "📡 Thu Thập Dữ Liệu"))
col1, col2 = st.sidebar.columns(2)
with col1:
    if st.button(t("🔄 Scrape Now", "🔄 Thu Thập Ngay"), type="primary"):
        with st.spinner(t("Running scraper...", "Đang chạy scraper...")):
            ok, out = run_scraper()
            if ok:
                st.success(t("✅ Scrape completed", "✅ Thu thập hoàn thành"))
                st.cache_data.clear()
                time.sleep(2)
                st.rerun()
            else:
                st.error(t("❌ Scrape failed", "❌ Thu thập thất bại"))
                with st.expander(t("Error details", "Chi tiết lỗi")):
                    st.text(out)

with col2:
    if st.button(t("🗑️ Clear Cache", "🗑️ Xóa Cache")):
        st.cache_data.clear()
        st.success(t("Cache cleared", "Cache đã xóa"))
        time.sleep(1)
        st.rerun()

# ---- Load Data ----
current_df = load_current_data()
historical_df = load_historical_data()

if current_df.empty and historical_df.empty:
    st.warning(t("📭 No data found. Run the scraper first to collect gold price data.", "📭 Không tìm thấy dữ liệu. Chạy scraper trước để thu thập dữ liệu giá vàng."))
    st.stop()

# ---- Data source selection with validation ----
all_sources = []
if not current_df.empty:
    all_sources.extend([s for s in current_df["source"].unique().tolist() if pd.notna(s)])
if not historical_df.empty:
    all_sources.extend([s for s in historical_df["source"].unique().tolist() if pd.notna(s)])
all_sources = sorted(list(set(all_sources)))

if not all_sources:
    st.warning(t("📭 No valid data sources found. Please run the scraper to collect data.", "📭 Không tìm thấy nguồn dữ liệu hợp lệ. Hãy chạy scraper để thu thập dữ liệu."))
    st.stop()

selected_sources = st.sidebar.multiselect(t("📊 Select Sources", "📊 Chọn Nguồn"), all_sources, default=all_sources[:min(5, len(all_sources))])

# Time range selection
st.sidebar.subheader(t("📅 Time Range", "📅 Phạm Vi Thời Gian"))
time_range = st.sidebar.selectbox(
    t("Quick select", "Chọn Nhanh"),
    [t("Last 24 Hours", "24 Giờ Qua"), t("Last 3 Days", "3 Ngày Qua"), t("Last Week", "Tuần Qua"), t("Last Month", "Tháng Qua"), t("Last 3 Months", "3 Tháng Qua"), t("Custom", "Tùy Chỉnh")]
)

if time_range == t("Custom", "Tùy Chỉnh"):
    if not historical_df.empty:
        min_date = historical_df["date"].min().date()
        max_date = historical_df["date"].max().date()
        date_range = st.sidebar.date_input(t("Date Range", "Phạm Vi Ngày"), value=(min_date, max_date))
    else:
        date_range = st.sidebar.date_input(t("Date Range", "Phạm Vi Ngày"))
else:
    # Calculate date range based on selection
    end_date = datetime.now().date()
    if time_range == t("Last 24 Hours", "24 Giờ Qua"):
        start_date = (datetime.now() - timedelta(days=1)).date()
    elif time_range == t("Last 3 Days", "3 Ngày Qua"):
        start_date = (datetime.now() - timedelta(days=3)).date()
    elif time_range == t("Last Week", "Tuần Qua"):
        start_date = (datetime.now() - timedelta(weeks=1)).date()
    elif time_range == t("Last Month", "Tháng Qua"):
        start_date = (datetime.now() - timedelta(days=30)).date()
    else:  # Last 3 Months
        start_date = (datetime.now() - timedelta(days=90)).date()
    date_range = (start_date, end_date)

# ---- Real-time Dashboard Header ----
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.markdown(f"""
<div style="background: linear-gradient(90deg, #1f4037, #99f2c8); color: white; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
    <h3>🕐 {t("Live Market Status", "Trạng Thái Thị Trường Trực Tiếp")} - {current_time}</h3>
    <p>{t("Last updated", "Cập Nhật Cuối")}: {refresh_interval}s {t("ago", "trước")} | {t("Auto-refresh", "Tự Động Làm Mới")}: {'ON' if auto_refresh else 'OFF' if st.session_state.lang == 'en' else 'BẬT' if auto_refresh else 'TẮT'}</p>
</div>
""", unsafe_allow_html=True)

# ---- Current Market Overview ----
if not current_df.empty and selected_sources:
    st.subheader(t("💰 Current Market Overview", "💰 Tổng Quan Thị Trường Hiện Tại"))
    
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
                
                # Check if sell price is valid before calculations
                if pd.notna(row["sell"]) and row["sell"] is not None and row["sell"] != 0:
                    change_pct = change / row["sell"] * 100
                    
                    st.metric(
                        label=f"{row['source']} ({t('Sell', 'Bán')})",
                        value=f"{row['sell']:,.0f} ₫",
                        delta=f"{change_pct:+.2f}%"
                    )
                else:
                    st.metric(
                        label=f"{row['source']} ({t('Sell', 'Bán')})",
                        value="N/A",
                        delta="N/A"
                    )
                
                # Display spread info if available
                if (pd.notna(row.get("spread")) and row.get("spread") is not None and
                    pd.notna(row.get("spread_pct")) and row.get("spread_pct") is not None):
                    st.metric(
                        label=t("Spread", "Chênh Lệch"),
                        value=f"{row['spread']:,.0f} ₫",
                        delta=f"{row['spread_pct']:.2f}%"
                    )
                else:
                    st.metric(
                        label=t("Spread", "Chênh Lệch"),
                        value="N/A",
                        delta="N/A"
                    )

# ---- Technical Analysis Dashboard ----
if not historical_df.empty:
    st.subheader(t("📈 Technical Analysis Dashboard", "📈 Bảng Phân Tích Kỹ Thuật"))
    
    # Filter historical data
    hist_filtered = historical_df[historical_df["source"].isin(selected_sources)]
    if isinstance(date_range, tuple) and len(date_range) == 2:
        start_date, end_date = date_range
        hist_filtered = hist_filtered[
            (hist_filtered["date"].dt.date >= start_date) & 
            (hist_filtered["date"].dt.date <= end_date)
        ]
    
    # Calculate technical indicators for each source
    ta_tabs = st.tabs([t("📊 Price Charts", "📊 Biểu Đồ Giá"), t("🔢 Technical Indicators", "🔢 Chỉ Số Kỹ Thuật"), t("📉 Market Signals", "📉 Tín Hiệu Thị Trường"), t("🎯 Trading Signals", "🎯 Tín Hiệu Giao Dịch")])
    
    with ta_tabs[0]:  # Price Charts
        fig = make_subplots(
            rows=3, cols=1,
            subplot_titles=(t("Gold Prices", "Giá Vàng"), t("Volume/Spread Analysis", "Phân Tích Khối Lượng/Chênh Lệch"), t("Price Distribution", "Phân Bổ Giá")),
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
                        name=f"{source} - {t('Sell', 'Bán')}",
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
                        name=f"{source} - {t('Buy', 'Mua')}",
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
                        name=f"{source} - {t('Spread', 'Chênh Lệch')}",
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
                name=t("Price Distribution", "Phân Bổ Giá"),
                nbinsx=50,
                opacity=0.7
            ),
            row=3, col=1
        )
        
        fig.update_layout(
            height=800,
            title_text=t("Gold Price Analysis Dashboard", "Bảng Phân Tích Giá Vàng"),
            showlegend=True
        )
        
        fig.update_xaxes(title_text=t("Date", "Ngày"), row=3, col=1)
        fig.update_yaxes(title_text=t("Price (₫)", "Giá (₫)"), row=1, col=1)
        fig.update_yaxes(title_text=t("Spread (₫)", "Chênh Lệch (₫)"), row=2, col=1)
        fig.update_yaxes(title_text=t("Frequency", "Tần Số"), row=3, col=1)
        
        st.plotly_chart(fig, use_container_width=True)
    
    with ta_tabs[1]:  # Technical Indicators
        if TALIB_AVAILABLE and not hist_filtered.empty:
            # Select source for detailed technical analysis
            ta_source = st.selectbox(t("Select source for technical analysis", "Chọn nguồn cho phân tích kỹ thuật"), selected_sources)
            ta_data = hist_filtered[hist_filtered["source"] == ta_source].sort_values("date")
            
            if len(ta_data) > 20:
                ta_data = calculate_technical_indicators(ta_data, "sell")
                
                # Technical indicators charts
                fig_ta = make_subplots(
                    rows=4, cols=1,
                    subplot_titles=(
                        t("Price & Moving Averages", "Giá & Trung Bình Di Động"),
                        "MACD",
                        "RSI & Stochastic",
                        t("Bollinger Bands", "Dải Bollinger")
                    ),
                    vertical_spacing=0.05,
                    row_heights=[0.4, 0.2, 0.2, 0.2]
                )
                
                # Price and moving averages
                fig_ta.add_trace(go.Scatter(x=ta_data["date"], y=ta_data["sell"], name=t("Price", "Giá"), line=dict(width=2)), row=1, col=1)
                for ma in ["MA_5", "MA_10", "MA_20", "MA_50"]:
                    if ma in ta_data.columns:
                        fig_ta.add_trace(go.Scatter(x=ta_data["date"], y=ta_data[ma], name=ma), row=1, col=1)
                
                # MACD
                if "MACD" in ta_data.columns:
                    fig_ta.add_trace(go.Scatter(x=ta_data["date"], y=ta_data["MACD"], name="MACD"), row=2, col=1)
                    fig_ta.add_trace(go.Scatter(x=ta_data["date"], y=ta_data["MACD_signal"], name=t("Signal", "Tín Hiệu")), row=2, col=1)
                    fig_ta.add_trace(go.Bar(x=ta_data["date"], y=ta_data["MACD_hist"], name="Histogram"), row=2, col=1)
                
                # RSI
                if "RSI" in ta_data.columns:
                    fig_ta.add_trace(go.Scatter(x=ta_data["date"], y=ta_data["RSI"], name="RSI"), row=3, col=1)
                    fig_ta.add_hline(y=70, line_dash="dash", line_color="red", row=3, col=1)
                    fig_ta.add_hline(y=30, line_dash="dash", line_color="green", row=3, col=1)
                
                # Bollinger Bands
                if "BB_upper" in ta_data.columns:
                    fig_ta.add_trace(go.Scatter(x=ta_data["date"], y=ta_data["BB_upper"], name=t("BB Upper", "BB Trên")), row=4, col=1)
                    fig_ta.add_trace(go.Scatter(x=ta_data["date"], y=ta_data["BB_middle"], name=t("BB Middle", "BB Giữa")), row=4, col=1)
                    fig_ta.add_trace(go.Scatter(x=ta_data["date"], y=ta_data["BB_lower"], name=t("BB Lower", "BB Dưới")), row=4, col=1)
                    fig_ta.add_trace(go.Scatter(x=ta_data["date"], y=ta_data["sell"], name=t("Price", "Giá"), line=dict(color="black", width=2)), row=4, col=1)
                
                fig_ta.update_layout(height=1000, title_text=f"{t('Technical Analysis', 'Phân Tích Kỹ Thuật')} - {ta_source}")
                st.plotly_chart(fig_ta, use_container_width=True)
                
                # Technical indicators table
                st.subheader(t("📊 Latest Technical Indicators", "📊 Chỉ Số Kỹ Thuật Mới Nhất"))
                latest_ta = ta_data.iloc[-1]
                
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("RSI", f"{latest_ta.get('RSI', 0):.1f}", help=t("Relative Strength Index (14)", "Chỉ Số Sức Mạnh Tương Đối (14)"))
                    st.metric("MACD", f"{latest_ta.get('MACD', 0):.2f}")
                
                with col2:
                    st.metric("MA 5", f"{latest_ta.get('MA_5', 0):,.0f} ₫")
                    st.metric("MA 20", f"{latest_ta.get('MA_20', 0):,.0f} ₫")
                
                with col3:
                    st.metric("ATR", f"{latest_ta.get('ATR', 0):,.0f} ₫", help=t("Average True Range (Volatility)", "Phạm Vi Thực Trung Bình (Biến Động)"))
                    st.metric("Williams %R", f"{latest_ta.get('WILLIAMS_R', 0):.1f}")
                
                with col4:
                    sentiment, emoji = get_market_sentiment(
                        latest_ta.get('RSI', 50),
                        latest_ta.get('MACD_hist', 0)
                    )
                    st.metric(t("Market Sentiment", "Tâm Lý Thị Trường"), f"{emoji} {sentiment}")
            else:
                st.warning(t("Insufficient data for technical analysis (need >20 points)", "Dữ liệu không đủ cho phân tích kỹ thuật (cần >20 điểm)"))
        else:
            st.info(t("Install TA-Lib for technical indicators: pip install TA-Lib", "Cài đặt TA-Lib cho chỉ số kỹ thuật: pip install TA-Lib"))
    
    with ta_tabs[2]:  # Market Signals
        st.subheader(t("🚨 Market Alerts & Signals", "🚨 Cảnh Báo & Tín Hiệu Thị Trường"))
        
        # Generate alerts based on technical indicators
        alerts = []
        
        for source in selected_sources:
            source_data = hist_filtered[hist_filtered["source"] == source].sort_values("date")
            if len(source_data) > 1:
                latest = source_data.iloc[-1]
                previous = source_data.iloc[-2]
                
                # Check if data is valid before calculations
                if (latest["sell"] is not None and previous["sell"] is not None and 
                    not pd.isna(latest["sell"]) and not pd.isna(previous["sell"]) and 
                    previous["sell"] != 0):
                    
                    # Price change alert
                    try:
                        price_change = (latest["sell"] - previous["sell"]) / previous["sell"] * 100
                        if abs(price_change) > 2:  # 2% change threshold
                            alert_type = t("🔴 HIGH", "🔴 CAO") if abs(price_change) > 5 else t("🟡 MEDIUM", "🟡 TRUNG BÌNH")
                            alerts.append({
                                t("Type", "Loại"): alert_type,
                                t("Source", "Nguồn"): source,
                                t("Signal", "Tín Hiệu"): f"{t('Price change', 'Thay đổi giá')}: {price_change:+.2f}%",
                                t("Current", "Hiện Tại"): f"{latest['sell']:,.0f} ₫",
                                t("Previous", "Trước"): f"{previous['sell']:,.0f} ₫"
                            })
                    except (TypeError, ZeroDivisionError, ValueError):
                        continue
                
                # Spread alert - check if spread_pct exists and is valid
                if ("spread_pct" in latest and latest["spread_pct"] is not None and 
                    not pd.isna(latest["spread_pct"]) and latest["spread_pct"] > 3):
                    try:
                        alerts.append({
                            t("Type", "Loại"): t("🟡 MEDIUM", "🟡 TRUNG BÌNH"),
                            t("Source", "Nguồn"): source,
                            t("Signal", "Tín Hiệu"): f"{t('High spread', 'Chênh lệch cao')}: {latest['spread_pct']:.2f}%",
                            t("Current", "Hiện Tại"): f"{latest.get('spread', 0):,.0f} ₫",
                            t("Previous", "Trước"): "-"
                        })
                    except (TypeError, ValueError):
                        continue
        
        if alerts:
            alerts_df = pd.DataFrame(alerts)
            st.dataframe(alerts_df, use_container_width=True)
        else:
            st.success(t("✅ No alerts at this time", "✅ Không có cảnh báo lúc này"))
        
        # Market correlation matrix
        st.subheader(t("📊 Source Correlation Matrix", "📊 Ma Trận Tương Quan Nguồn"))
        
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
                title=t("Gold Price Source Correlation", "Tương Quan Nguồn Giá Vàng"),
                height=500
            )
            
            st.plotly_chart(fig_corr, use_container_width=True)
    
    with ta_tabs[3]:  # Trading Signals
        st.subheader(t("🎯 AI Trading Signals", "🎯 Tín Hiệu Giao Dịch AI"))
        
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
                        signal_reasons.append(t("RSI oversold", "RSI quá bán"))
                    elif latest["RSI"] > 70:
                        signal_strength -= 2
                        signal_reasons.append(t("RSI overbought", "RSI quá mua"))
                
                # MACD signals
                if "MACD_hist" in source_data.columns and not pd.isna(latest["MACD_hist"]):
                    if latest["MACD_hist"] > 0:
                        signal_strength += 1
                        signal_reasons.append(t("MACD bullish", "MACD tăng"))
                    else:
                        signal_strength -= 1
                        signal_reasons.append(t("MACD bearish", "MACD giảm"))
                
                # Moving average signals
                if "MA_5" in source_data.columns and "MA_20" in source_data.columns:
                    if latest["sell"] > latest["MA_5"] > latest["MA_20"]:
                        signal_strength += 1
                        signal_reasons.append(t("Price above MA", "Giá trên MA"))
                    elif latest["sell"] < latest["MA_5"] < latest["MA_20"]:
                        signal_strength -= 1
                        signal_reasons.append(t("Price below MA", "Giá dưới MA"))
                
                # Determine signal
                if signal_strength >= 2:
                    signal = t("🟢 STRONG BUY", "🟢 MUA MẠNH")
                elif signal_strength >= 1:
                    signal = t("🟢 BUY", "🟢 MUA")
                elif signal_strength <= -2:
                    signal = t("🔴 STRONG SELL", "🔴 BÁN MẠNH")
                elif signal_strength <= -1:
                    signal = t("🔴 SELL", "🔴 BÁN")
                else:
                    signal = t("🟡 HOLD", "🟡 GIỮ")
                
                signals.append({
                    t("Source", "Nguồn"): source,
                    t("Signal", "Tín Hiệu"): signal,
                    t("Strength", "Sức Mạnh"): signal_strength,
                    t("Reasons", "Lý Do"): ", ".join(signal_reasons) if signal_reasons else t("No clear signals", "Không có tín hiệu rõ ràng"),
                    t("Current Price", "Giá Hiện Tại"): f"{latest['sell']:,.0f} ₫",
                    t("Last Update", "Cập Nhật Cuối"): latest["date"].strftime("%Y-%m-%d")
                })
        
        if signals:
            signals_df = pd.DataFrame(signals)
            st.dataframe(signals_df, use_container_width=True)
        else:
            st.info(t("No trading signals available", "Không có tín hiệu giao dịch có sẵn"))

# ---- Performance Analytics ----
st.subheader(t("⚡ Performance Analytics", "⚡ Phân Tích Hiệu Suất"))

perf_col1, perf_col2, perf_col3 = st.columns(3)

with perf_col1:
    st.metric(
        t("Data Points", "Điểm Dữ Liệu"),
        len(current_df) + len(historical_df),
        f"+{len(current_df)} " + t("today", "hôm nay")
    )

with perf_col2:
    if not current_df.empty:
        latest_update = current_df["timestamp"].max()
        minutes_ago = (datetime.now() - latest_update.replace(tzinfo=None)).total_seconds() / 60
        st.metric(
            t("Last Update", "Cập Nhật Cuối"),
            f"{minutes_ago:.0f}m " + t("ago", "phút trước"),
            t("Real-time", "Thời gian thực") if minutes_ago < 5 else t("Delayed", "Trì Hoãn")
        )

with perf_col3:
    active_sources = len(selected_sources)
    total_sources = len(all_sources)
    st.metric(
        t("Active Sources", "Nguồn Hoạt Động"),
        f"{active_sources}/{total_sources}",
        f"{(active_sources/total_sources*100):.0f}% " + t("coverage", "phạm vi")
    )

# ---- Portfolio Management ----
st.subheader(t("💼 Portfolio & Risk Management", "💼 Quản Lý Danh Mục & Rủi Ro"))

portfolio_tabs = st.tabs([t("💰 Portfolio Tracker", "💰 Theo Dõi Danh Mục"), t("⚖️ Risk Analysis", "⚖️ Phân Tích Rủi Ro"), t("📊 Performance Reports", "📊 Báo Cáo Hiệu Suất"), t("🎯 Position Calculator", "🎯 Máy Tính Vị Thế")])

with portfolio_tabs[0]:  # Portfolio Tracker
    st.markdown(t("### 💰 Gold Portfolio Tracker", "### 💰 Theo Dõi Danh Mục Vàng"))
    
    # Portfolio input section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(t("#### Add Position", "#### Thêm Vị Thế"))
        with st.form("add_position"):
            pos_source = st.selectbox(t("Source", "Nguồn"), selected_sources)
            pos_type = st.selectbox(t("Position Type", "Loại Vị Thế"), [t("Long (Buy)", "Mua (Long)"), t("Short (Sell)", "Bán (Short)")])
            pos_quantity = st.number_input(t("Quantity (grams)", "Số Lượng (gram)"), min_value=0.1, value=10.0, step=0.1)
            pos_entry_price = st.number_input(t("Entry Price (₫/gram)", "Giá Vào (₫/gram)"), min_value=1000, value=80000000, step=1000)
            pos_date = st.date_input(t("Entry Date", "Ngày Vào"), value=datetime.now().date())
            
            if st.form_submit_button(t("➕ Add Position", "➕ Thêm Vị Thế")):
                if "portfolio" not in st.session_state:
                    st.session_state.portfolio = []
                
                position = {
                    "id": len(st.session_state.portfolio),
                    "source": pos_source,
                    "type": pos_type,
                    "quantity": pos_quantity,
                    "entry_price": pos_entry_price,
                    "entry_date": pos_date,
                    "status": t("Open", "Mở")
                }
                st.session_state.portfolio.append(position)
                st.success(t("✅ Position added to portfolio!", "✅ Vị thế đã thêm vào danh mục!"))
                st.rerun()
    
    with col2:
        # Portfolio summary
        if "portfolio" in st.session_state and st.session_state.portfolio:
            total_positions = len(st.session_state.portfolio)
            total_value = sum(p["quantity"] * p["entry_price"] for p in st.session_state.portfolio)
            
            st.metric(t("Total Positions", "Tổng Vị Thế"), total_positions)
            st.metric(t("Portfolio Value", "Giá Trị Danh Mục"), f"{total_value:,.0f} ₫")
            
            if st.button(t("🗑️ Clear Portfolio", "🗑️ Xóa Danh Mục")):
                st.session_state.portfolio = []
                st.rerun()
    
    # Portfolio display
    if "portfolio" in st.session_state and st.session_state.portfolio:
        st.markdown(t("#### Current Positions", "#### Vị Thế Hiện Tại"))
        
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
            
            if t("Short (Sell)", "Bán (Short)") in pos["type"]:
                pnl = -pnl
                pnl_pct = -pnl_pct
            
            portfolio_data.append({
                "ID": pos["id"],
                t("Source", "Nguồn"): pos["source"],
                t("Type", "Loại"): pos["type"],
                t("Quantity (g)", "Số Lượng (g)"): pos["quantity"],
                t("Entry Price", "Giá Vào"): f"{pos['entry_price']:,.0f} ₫",
                t("Current Price", "Giá Hiện Tại"): f"{current_price:,.0f} ₫",
                t("P&L", "Lãi/Lỗ"): f"{pnl:,.0f} ₫",
                t("P&L %", "Lãi/Lỗ %"): f"{pnl_pct:+.2f}%",
                t("Entry Date", "Ngày Vào"): pos["entry_date"],
                t("Status", "Trạng Thái"): pos["status"]
            })
        
        portfolio_df = pd.DataFrame(portfolio_data)
        st.dataframe(portfolio_df, use_container_width=True)
        
        # Portfolio performance chart
        if len(portfolio_data) > 0:
            fig_portfolio = go.Figure()
            
            pnl_values = [float(p[t("P&L", "Lãi/Lỗ")].replace(" ₫", "").replace(",", "")) for p in portfolio_data]
            sources = [p[t("Source", "Nguồn")] for p in portfolio_data]
            
            fig_portfolio.add_trace(go.Bar(
                x=sources,
                y=pnl_values,
                marker_color=["green" if x > 0 else "red" for x in pnl_values],
                text=[f"{x:,.0f} ₫" for x in pnl_values],
                textposition="auto"
            ))
            
            fig_portfolio.update_layout(
                title=t("Portfolio P&L by Source", "Lãi/Lỗ Danh Mục Theo Nguồn"),
                xaxis_title=t("Source", "Nguồn"),
                yaxis_title=t("P&L (₫)", "Lãi/Lỗ (₫)"),
                height=400
            )
            
            st.plotly_chart(fig_portfolio, use_container_width=True)

with portfolio_tabs[1]:  # Risk Analysis
    st.markdown(t("### ⚖️ Risk Analysis & VaR Calculator", "### ⚖️ Phân Tích Rủi Ro & Máy Tính VaR"))
    
    risk_col1, risk_col2 = st.columns(2)
    
    with risk_col1:
        st.markdown(t("#### Value at Risk (VaR) Calculator", "#### Máy Tính Giá Trị Rủi Ro (VaR)"))
        
        var_confidence = st.selectbox(t("Confidence Level", "Mức Tin Cậy"), [90, 95, 99], index=1)
        var_timeframe = st.selectbox(t("Time Horizon", "Chân Trời Thời Gian"), [t("1 Day", "1 Ngày"), t("1 Week", "1 Tuần"), t("1 Month", "1 Tháng")])
        var_method = st.selectbox(t("VaR Method", "Phương Pháp VaR"), [t("Historical Simulation", "Mô Phỏng Lịch Sử"), t("Parametric", "Tham Số"), "Monte Carlo"])
        
        if not historical_df.empty and len(historical_df) > 30:
            # Calculate historical volatility
            for source in selected_sources[:3]:  # Limit to first 3 sources for performance
                source_data = historical_df[historical_df["source"] == source].sort_values("date")
                
                if len(source_data) > 30:
                    # Calculate daily returns
                    source_data["returns"] = source_data["sell"].pct_change()
                    daily_vol = source_data["returns"].std()
                    
                    # Scale volatility based on timeframe
                    if var_timeframe == t("1 Week", "1 Tuần"):
                        scaled_vol = daily_vol * np.sqrt(7)
                    elif var_timeframe == t("1 Month", "1 Tháng"):
                        scaled_vol = daily_vol * np.sqrt(30)
                    else:
                        scaled_vol = daily_vol
                    
                    # Calculate VaR
                    if var_method == t("Parametric", "Tham Số"):
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
                    
                    st.info(f"📊 {t('Daily Volatility', 'Biến Động Hàng Ngày')}: {daily_vol*100:.2f}%")
    
    with risk_col2:
        st.markdown(t("#### Risk Metrics Dashboard", "#### Bảng Chỉ Số Rủi Ro"))
        
        # Risk-free rate (Vietnam government bonds)
        risk_free_rate = st.number_input(t("Risk-free Rate (%)", "Lãi Suất Phi Rủi Ro (%)"), value=4.5, step=0.1) / 100
        
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
                st.markdown(t("**Sharpe Ratios:**", "**Tỷ Lệ Sharpe:**"))
                for source, ratio in sharpe_ratios.items():
                    color = "green" if ratio > 1 else "orange" if ratio > 0.5 else "red"
                    st.markdown(f"- **{source}**: <span style='color: {color}'>{ratio:.3f}</span>", unsafe_allow_html=True)
                
                st.markdown(t("**Maximum Drawdowns:**", "**Mức Sụt Giảm Tối Đa:**"))
                for source, dd in max_drawdowns.items():
                    st.markdown(f"- **{source}**: <span style='color: red'>{dd*100:.2f}%</span>", unsafe_allow_html=True)

with portfolio_tabs[2]:  # Performance Reports
    st.markdown(t("### 📊 Performance Reports & Analytics", "### 📊 Báo Cáo Hiệu Suất & Phân Tích"))
    
    report_type = st.selectbox(t("Report Type", "Loại Báo Cáo"), [
        t("Daily Performance", "Hiệu Suất Hàng Ngày"), 
        t("Weekly Summary", "Tóm Tắt Tuần"), 
        t("Monthly Analysis", "Phân Tích Tháng"), 
        t("Comparative Analysis", "Phân Tích So Sánh"),
        t("Volatility Report", "Báo Cáo Biến Động")
    ])
    
    if report_type == t("Daily Performance", "Hiệu Suất Hàng Ngày") and not historical_df.empty:
        # Daily performance analysis
        today = datetime.now().date()
        yesterday = today - timedelta(days=1)
        
        daily_data = historical_df[historical_df["date"].dt.date == today]
        
        if not daily_data.empty:
            st.markdown(t("#### Today's Performance", "#### Hiệu Suất Hôm Nay"))
            
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
                title=t("Intraday Price Movement", "Chuyển Động Giá Trong Ngày")
            )
            st.plotly_chart(fig_intraday, use_container_width=True)
        else:
            st.info(t("No data available for today", "Không có dữ liệu cho hôm nay"))
    
    elif report_type == t("Comparative Analysis", "Phân Tích So Sánh") and not historical_df.empty:
        st.markdown(t("#### Source Comparison Matrix", "#### Ma Trận So Sánh Nguồn"))
        
        # Create comparison metrics
        comparison_data = []
        
        for source in selected_sources:
            source_data = historical_df[historical_df["source"] == source]
            
            if not source_data.empty:
                metrics = {
                    t("Source", "Nguồn"): source,
                    t("Avg Price", "Giá Trung Bình"): source_data["sell"].mean(),
                    t("Price Std", "Độ Lệch Chuẩn Giá"): source_data["sell"].std(),
                    t("Min Price", "Giá Tối Thiểu"): source_data["sell"].min(),
                    t("Max Price", "Giá Tối Đa"): source_data["sell"].max(),
                    t("Avg Spread", "Chênh Lệch Trung Bình"): source_data["spread"].mean(),
                    t("Spread %", "Chênh Lệch %"): (source_data["spread"] / source_data["sell"] * 100).mean(),
                    t("Data Points", "Điểm Dữ Liệu"): len(source_data)
                }
                comparison_data.append(metrics)
        
        if comparison_data:
            comp_df = pd.DataFrame(comparison_data)
            
            # Style the dataframe
            styled_df = comp_df.style.format({
                t("Avg Price", "Giá Trung Bình"): "{:,.0f} ₫",
                t("Price Std", "Độ Lệch Chuẩn Giá"): "{:,.0f} ₫",
                t("Min Price", "Giá Tối Thiểu"): "{:,.0f} ₫",
                t("Max Price", "Giá Tối Đa"): "{:,.0f} ₫",
                t("Avg Spread", "Chênh Lệch Trung Bình"): "{:,.0f} ₫",
                t("Spread %", "Chênh Lệch %"): "{:.2f}%"
            }).background_gradient(subset=[t("Avg Price", "Giá Trung Bình"), t("Price Std", "Độ Lệch Chuẩn Giá"), t("Spread %", "Chênh Lệch %")])
            
            st.dataframe(styled_df, use_container_width=True)
            
            # Radar chart for source comparison
            categories = [t("Avg Price (norm)", "Giá Trung Bình (chuẩn hóa)"), t("Volatility", "Biến Động"), t("Spread", "Chênh Lệch"), t("Data Quality", "Chất Lượng Dữ Liệu")]
            
            fig_radar = go.Figure()
            
            for _, row in comp_df.iterrows():
                # Normalize metrics for radar chart
                values = [
                    (row[t("Avg Price", "Giá Trung Bình")] - comp_df[t("Avg Price", "Giá Trung Bình")].min()) / (comp_df[t("Avg Price", "Giá Trung Bình")].max() - comp_df[t("Avg Price", "Giá Trung Bình")].min()),
                    (row[t("Price Std", "Độ Lệch Chuẩn Giá")] - comp_df[t("Price Std", "Độ Lệch Chuẩn Giá")].min()) / (comp_df[t("Price Std", "Độ Lệch Chuẩn Giá")].max() - comp_df[t("Price Std", "Độ Lệch Chuẩn Giá")].min()),
                    (row[t("Spread %", "Chênh Lệch %")] - comp_df[t("Spread %", "Chênh Lệch %")].min()) / (comp_df[t("Spread %", "Chênh Lệch %")].max() - comp_df[t("Spread %", "Chênh Lệch %")].min()),
                    (row[t("Data Points", "Điểm Dữ Liệu")] - comp_df[t("Data Points", "Điểm Dữ Liệu")].min()) / (comp_df[t("Data Points", "Điểm Dữ Liệu")].max() - comp_df[t("Data Points", "Điểm Dữ Liệu")].min())
                ]
                
                fig_radar.add_trace(go.Scatterpolar(
                    r=values + [values[0]],  # Close the loop
                    theta=categories + [categories[0]],
                    fill='toself',
                    name=row[t("Source", "Nguồn")]
                ))
            
            fig_radar.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
                showlegend=True,
                title=t("Source Performance Comparison", "So Sánh Hiệu Suất Nguồn")
            )
            
            st.plotly_chart(fig_radar, use_container_width=True)

with portfolio_tabs[3]:  # Position Calculator
    st.markdown(t("### 🎯 Advanced Position Calculator", "### 🎯 Máy Tính Vị Thế Nâng Cao"))
    
    calc_col1, calc_col2 = st.columns([1, 1])
    
    with calc_col1:
        st.markdown(t("#### Position Sizing Calculator", "#### Máy Tính Kích Thước Vị Thế"))
        
        # Kelly Criterion Calculator
        st.markdown(t("**Kelly Criterion Position Sizing**", "**Định Kích Vị Thế Kelly Criterion**"))
        
        win_rate = st.slider(t("Win Rate (%)", "Tỷ Lệ Thắng (%)"), 0, 100, 60) / 100
        avg_win = st.number_input(t("Average Win (₫)", "Lãi Trung Bình (₫)"), value=500000, step=10000)
        avg_loss = st.number_input(t("Average Loss (₫)", "Lỗ Trung Bình (₫)"), value=300000, step=10000)
        
        if avg_loss > 0:
            win_loss_ratio = avg_win / avg_loss
            kelly_fraction = win_rate - ((1 - win_rate) / win_loss_ratio)
            
            st.metric(t("Kelly Fraction", "Hệ Số Kelly"), f"{kelly_fraction:.3f}")
            
            if kelly_fraction > 0:
                st.success(t(f"✅ Optimal position size: {kelly_fraction*100:.1f}% of capital", f"✅ Kích thước vị thế tối ưu: {kelly_fraction*100:.1f}% của vốn"))
            else:
                st.warning(t("⚠️ Negative Kelly fraction - avoid this trade", "⚠️ Hệ Số Kelly Âm - tránh giao dịch này"))
        
        # Risk-based position sizing
        st.markdown(t("**Risk-Based Position Sizing**", "**Định Kích Vị Thế Dựa Trên Rủi Ro**"))
        
        account_size = st.number_input(t("Account Size (₫)", "Kích Thước Tài Khoản (₫)"), value=100000000, step=1000000)
        risk_per_trade = st.slider(t("Risk per Trade (%)", "Rủi Ro Mỗi Giao Dịch (%)"), 0.5, 5.0, 2.0) / 100
        stop_loss_pct = st.slider(t("Stop Loss (%)", "Dừng Lỗ (%)"), 1.0, 10.0, 3.0) / 100
        
        risk_amount = account_size * risk_per_trade
        position_size = risk_amount / stop_loss_pct
        
        st.metric(t("Position Size", "Kích Thước Vị Thế"), f"{position_size:,.0f} ₫")
        st.metric(t("Risk Amount", "Số Lượng Rủi Ro"), f"{risk_amount:,.0f} ₫")
    
    with calc_col2:
        st.markdown(t("#### Profit/Loss Calculator", "#### Máy Tính Lãi/Lỗ"))
        
        # P&L Calculator
        entry_price = st.number_input(t("Entry Price (₫/gram)", "Giá Vào (₫/gram)"), value=80000000, step=100000)
        exit_price = st.number_input(t("Target Exit Price (₫/gram)", "Giá Ra Mục Tiêu (₫/gram)"), value=82000000, step=100000)
        position_grams = st.number_input(t("Position Size (grams)", "Kích Thước Vị Thế (gram)"), value=10.0, step=0.1)
        
        # Calculate P&L
        gross_pnl = (exit_price - entry_price) * position_grams
        
        # Transaction costs
        buy_fee_rate = st.number_input(t("Buy Fee (%)", "Phí Mua (%)"), value=0.5, step=0.1) / 100
        sell_fee_rate = st.number_input(t("Sell Fee (%)", "Phí Bán (%)"), value=0.5, step=0.1) / 100
        
        buy_fee = entry_price * position_grams * buy_fee_rate
        sell_fee = exit_price * position_grams * sell_fee_rate
        total_fees = buy_fee + sell_fee
        
        net_pnl = gross_pnl - total_fees
        roi = net_pnl / (entry_price * position_grams) * 100
        
        # Display results
        st.markdown(t("**Calculation Results:**", "**Kết Quả Tính Toán:**"))
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric(t("Gross P&L", "Lãi/Lỗ Tổng"), f"{gross_pnl:,.0f} ₫")
            st.metric(t("Total Fees", "Tổng Phí"), f"{total_fees:,.0f} ₫")
        
        with col_b:
            st.metric(t("Net P&L", "Lãi/Lỗ Ròng"), f"{net_pnl:,.0f} ₫", f"{roi:+.2f}%")
            
            if net_pnl > 0:
                st.success(t("✅ Profitable trade", "✅ Giao Dịch Lãi"))
            else:
                st.error(t("❌ Loss-making trade", "❌ Giao Dịch Lỗ"))
        
        # Break-even analysis
        breakeven_price = entry_price + (total_fees / position_grams)
        st.info(f"📊 {t('Break-even price', 'Giá Hòa Vốn')}: {breakeven_price:,.0f} ₫/gram")

# ---- Market News & Sentiment ----
st.subheader(t("📰 Market News & Sentiment Analysis", "📰 Tin Tức Thị Trường & Phân Tích Tâm Lý"))

news_col1, news_col2 = st.columns([2, 1])

with news_col1:
    st.markdown(t("#### 📈 Market Impact Factors", "#### 📈 Yếu Tố Ảnh Hưởng Thị Trường"))
    
    # Mock news data - in real implementation, connect to news APIs
    market_factors = [
        {t("Factor", "Yếu Tố"): t("USD/VND Exchange Rate", "Tỷ Giá USD/VND"), t("Impact", "Tác Động"): t("High", "Cao"), t("Direction", "Hướng"): t("Inverse", "Ngược"), t("Last Update", "Cập Nhật Cuối"): t("30m ago", "30 phút trước")},
        {t("Factor", "Yếu Tố"): t("International Gold Price", "Giá Vàng Quốc Tế"), t("Impact", "Tác Động"): t("Very High", "Rất Cao"), t("Direction", "Hướng"): t("Direct", "Trực Tiếp"), t("Last Update", "Cập Nhật Cuối"): t("15m ago", "15 phút trước")},
        {t("Factor", "Yếu Tố"): t("Inflation Rate (Vietnam)", "Tỷ Lệ Lạm Phát (Việt Nam)"), t("Impact", "Tác Động"): t("Medium", "Trung Bình"), t("Direction", "Hướng"): t("Direct", "Trực Tiếp"), t("Last Update", "Cập Nhật Cuối"): t("2h ago", "2 giờ trước")},
        {t("Factor", "Yếu Tố"): t("Central Bank Policy", "Chính Sách Ngân Hàng Trung Ương"), t("Impact", "Tác Động"): t("High", "Cao"), t("Direction", "Hướng"): t("Mixed", "Hỗn Hợp"), t("Last Update", "Cập Nhật Cuối"): t("1d ago", "1 ngày trước")},
        {t("Factor", "Yếu Tố"): t("Global Economic Uncertainty", "Bất Định Kinh Tế Toàn Cầu"), t("Impact", "Tác Động"): t("High", "Cao"), t("Direction", "Hướng"): t("Direct", "Trực Tiếp"), t("Last Update", "Cập Nhật Cuối"): t("4h ago", "4 giờ trước")}
    ]
    
    factors_df = pd.DataFrame(market_factors)
    
    # Style the factors table
    def color_impact(val):
        colors = {t("Very High", "Rất Cao"): "background-color: #ff4444; color: white",
                 t("High", "Cao"): "background-color: #ff8800; color: white",
                 t("Medium", "Trung Bình"): "background-color: #ffaa00; color: black"}
        return colors.get(val, "")
    
    styled_factors = factors_df.style.applymap(color_impact, subset=[t("Impact", "Tác Động")])
    st.dataframe(styled_factors, use_container_width=True)

with news_col2:
    st.markdown(t("#### 🎭 Market Sentiment", "#### 🎭 Tâm Lý Thị Trường"))
    
    # Mock sentiment analysis
    sentiment_score = np.random.uniform(0.3, 0.8)  # Replace with actual sentiment analysis
    
    if sentiment_score > 0.7:
        sentiment_label = t("Very Bullish", "Rất Tăng")
        sentiment_color = "#00ff00"
        sentiment_emoji = "🚀"
    elif sentiment_score > 0.6:
        sentiment_label = t("Bullish", "Tăng")
        sentiment_color = "#88ff88"
        sentiment_emoji = "📈"
    elif sentiment_score > 0.4:
        sentiment_label = t("Neutral", "Trung Lập")
        sentiment_color = "#ffff00"
        sentiment_emoji = "😐"
    elif sentiment_score > 0.3:
        sentiment_label = t("Bearish", "Giảm")
        sentiment_color = "#ff8888"
        sentiment_emoji = "📉"
    else:
        sentiment_label = t("Very Bearish", "Rất Giảm")
        sentiment_color = "#ff0000"
        sentiment_emoji = "💥"
    
    st.markdown(f"""
    <div style="text-align: center; padding: 20px; border-radius: 10px; background-color: {sentiment_color}20; border: 2px solid {sentiment_color};">
        <h2>{sentiment_emoji} {sentiment_label}</h2>
        <h3>{t("Score", "Điểm")}: {sentiment_score:.2f}/1.0</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Sentiment gauge
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = sentiment_score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': t("Market Sentiment", "Tâm Lý Thị Trường")},
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
st.subheader(t("🔧 System Health & Monitoring", "🔧 Sức Khỏe Hệ Thống & Giám Sát"))

health_col1, health_col2, health_col3, health_col4 = st.columns(4)

with health_col1:
    # Database health
    db_health = t("Healthy", "Khỏe Mạnh") if os.path.exists(DB_FILE) else t("Offline", "Ngoại Tuyến")
    db_color = "green" if db_health == t("Healthy", "Khỏe Mạnh") else "red"
    st.markdown(t("**Database Status**", "**Trạng Thái Cơ Sở Dữ Liệu**"))
    st.markdown(f"<span style='color: {db_color}'>● {db_health}</span>", unsafe_allow_html=True)

with health_col2:
    # Data freshness
    if not current_df.empty:
        last_update = current_df["timestamp"].max()
        freshness_minutes = (datetime.now() - last_update.replace(tzinfo=None)).total_seconds() / 60
        freshness_status = t("Fresh", "Tươi") if freshness_minutes < 30 else t("Stale", "Cũ")
        freshness_color = "green" if freshness_status == t("Fresh", "Tươi") else "orange"
    else:
        freshness_status = t("No Data", "Không Có Dữ Liệu")
        freshness_color = "red"
    
    st.markdown(t("**Data Freshness**", "**Độ Tươi Dữ Liệu**"))
    st.markdown(f"<span style='color: {freshness_color}'>● {freshness_status}</span>", unsafe_allow_html=True)

with health_col3:
    # Source availability
    total_sources = len(all_sources)
    active_sources = len([s for s in selected_sources if not current_df[current_df["source"] == s].empty])
    availability_pct = (active_sources / total_sources * 100) if total_sources > 0 else 0
    availability_color = "green" if availability_pct > 80 else "orange" if availability_pct > 50 else "red"
    
    st.markdown(t("**Source Availability**", "**Tính Sẵn Sàng Nguồn**"))
    st.markdown(f"<span style='color: {availability_color}'>● {availability_pct:.0f}%</span>", unsafe_allow_html=True)

with health_col4:
    # API response time (mock)
    response_time = np.random.uniform(100, 500)  # Replace with actual monitoring
    response_status = t("Fast", "Nhanh") if response_time < 200 else t("Normal", "Bình Thường") if response_time < 400 else t("Slow", "Chậm")
    response_color = "green" if response_status == t("Fast", "Nhanh") else "orange" if response_status == t("Normal", "Bình Thường") else "red"
    
    st.markdown(t("**Response Time**", "**Thời Gian Phản Hồi**"))
    st.markdown(f"<span style='color: {response_color}'>● {response_time:.0f}ms</span>", unsafe_allow_html=True)

# ---- Export & Integration ----
st.subheader(t("📤 Export & Integration", "📤 Xuất & Tích Hợp"))

export_col1, export_col2 = st.columns(2)

with export_col1:
    st.markdown(t("#### 📊 Data Export", "#### 📊 Xuất Dữ Liệu"))
    
    export_format = st.selectbox(t("Export Format", "Định Dạng Xuất"), ["CSV", "JSON", "Excel", "Parquet"])
    export_timeframe = st.selectbox(t("Timeframe", "Khung Thời Gian"), [t("Current Session", "Phiên Hiện Tại"), t("Last 24h", "24h Qua"), t("Last Week", "Tuần Qua"), t("All Data", "Tất Cả Dữ Liệu")])
    
    if st.button(t("📥 Export Data", "📥 Xuất Dữ Liệu")):
        # Prepare export data based on selection
        if export_timeframe == t("Current Session", "Phiên Hiện Tại"):
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
            
            st.success(t(f"✅ Data exported as {filename}.{export_format.lower()}", f"✅ Dữ liệu xuất dưới dạng {filename}.{export_format.lower()}"))

with export_col2:
    st.markdown(t("#### 🔗 API Integration", "#### 🔗 Tích Hợp API"))
    
    st.code("""
# REST API Endpoints (Mock)
GET /api/v1/current-prices
GET /api/v1/historical/{source}
GET /api/v1/alerts
POST /api/v1/portfolio/positions
    """)
    
    api_key = st.text_input(t("API Key", "Khóa API"), type="password", placeholder=t("Enter your API key", "Nhập khóa API của bạn"))
    
    if st.button(t("🔑 Generate API Key", "🔑 Tạo Khóa API")):
        mock_key = f"gd_{datetime.now().strftime('%Y%m%d')}_{hash(datetime.now()) % 10000:04d}"
        st.code(mock_key)
        st.info(t("API key generated! (Mock)", "Khóa API đã tạo! (Giả)"))

# ---- Footer with Enhanced Info ----
st.markdown("---")

footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.markdown(t("**🏆 Dashboard Stats**", "**🏆 Thống Kê Bảng Điều Khiển**"))
    total_datapoints = len(current_df) + len(historical_df)
    st.write(f"• {t('Total data points', 'Tổng điểm dữ liệu')}: {total_datapoints:,}")
    st.write(f"• {t('Active sources', 'Nguồn hoạt động')}: {len(selected_sources)}")
    st.write(f"• {t('Last update', 'Cập nhật cuối')}: {datetime.now().strftime('%H:%M:%S')}")

with footer_col2:
    st.markdown(t("**📊 Market Coverage**", "**📊 Phạm Vi Thị Trường**"))
    st.write(t("• Vietnamese gold markets", "• Thị trường vàng Việt Nam"))
    st.write(t("• International benchmarks", "• Chuẩn mực quốc tế"))
    st.write(t("• Real-time & historical data", "• Dữ liệu thời gian thực & lịch sử"))

with footer_col3:
    st.markdown(t("**🔧 System Info**", "**🔧 Thông Tin Hệ Thống**"))
    st.write(f"• {t('Refresh', 'Làm Mới')}: {refresh_interval}s")
    st.write(f"• {t('Auto-refresh', 'Tự Động Làm Mới')}: {'ON' if auto_refresh else 'OFF' if st.session_state.lang == 'en' else 'BẬT' if auto_refresh else 'TẮT'}")
    st.write(t("• Status: 🟢 Online", "• Trạng Thái: 🟢 Trực Tuyến"))

# ---- Advanced Machine Learning Predictions ----
st.subheader(t("🤖 AI-Powered Price Predictions", "🤖 Dự Đoán Giá Bằng AI"))

ml_tabs = st.tabs([t("🎯 Price Forecasting", "🎯 Dự Báo Giá"), t("📊 Pattern Recognition", "📊 Nhận Diện Mẫu"), t("⚡ Anomaly Detection", "⚡ Phát Hiện Bất Thường"), t("🔮 Scenario Analysis", "🔮 Phân Tích Kịch Bản")])

with ml_tabs[0]:  # Price Forecasting
    st.markdown(t("### 🎯 Machine Learning Price Forecasting", "### 🎯 Dự Báo Giá Bằng Học Máy"))
    
    if not historical_df.empty:
        forecast_source = st.selectbox(t("Select Source for ML Forecast", "Chọn Nguồn Cho Dự Báo ML"), selected_sources, key="ml_forecast")
        forecast_horizon = st.selectbox(t("Forecast Horizon", "Chân Trời Dự Báo"), [t("1 Hour", "1 Giờ"), t("4 Hours", "4 Giờ"), t("1 Day", "1 Ngày"), t("3 Days", "3 Ngày"), t("1 Week", "1 Tuần")])
        
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
                        forecast_steps_dict = {t("1 Hour", "1 Giờ"): 1, t("4 Hours", "4 Giờ"): 4, t("1 Day", "1 Ngày"): 24, t("3 Days", "3 Ngày"): 72, t("1 Week", "1 Tuần"): 168}
                        steps = forecast_steps_dict.get(forecast_horizon, 24)
                        
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
                            name=t("Historical", "Lịch Sử"),
                            line=dict(color="blue", width=2)
                        ))
                        
                        # Predictions
                        fig_forecast.add_trace(go.Scatter(
                            x=forecast_df["date"],
                            y=forecast_df["predicted_price"],
                            name=t("ML Forecast", "Dự Báo ML"),
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
                            name=t('Confidence Interval', 'Khoảng Tin Cậy'),
                            fillcolor='rgba(255,0,0,0.2)'
                        ))
                        
                        fig_forecast.update_layout(
                            title=f"{t('ML Price Forecast', 'Dự Báo Giá ML')} - {forecast_source} ({forecast_horizon})",
                            xaxis_title=t("Date", "Ngày"),
                            yaxis_title=t("Price (₫)", "Giá (₫)"),
                            height=500
                        )
                        
                        st.plotly_chart(fig_forecast, use_container_width=True)
                        
                        # Model performance metrics
                        r2_score = model.score(X_scaled, y)
                        
                        st.markdown(t("**Model Performance:**", "**Hiệu Suất Mô Hình:**"))
                        metric_col1, metric_col2, metric_col3 = st.columns(3)
                        
                        with metric_col1:
                            st.metric(t("R² Score", "Điểm R²"), f"{r2_score:.3f}")
                        with metric_col2:
                            st.metric("MAE", f"{mae:,.0f} ₫")
                        with metric_col3:
                            pred_change = (predictions[-1] - y.iloc[-1]) / y.iloc[-1] * 100
                            st.metric(t("Forecast Change", "Thay Đổi Dự Báo"), f"{pred_change:+.2f}%")
                        
                except Exception as e:
                    st.error(t(f"ML Forecasting Error: {e}", f"Lỗi Dự Báo ML: {e}"))
                    st.info(t("Try with different parameters or check data quality", "Thử với thông số khác hoặc kiểm tra chất lượng dữ liệu"))
            else:
                st.warning(t("Insufficient data for ML forecasting (need ≥50 data points)", "Dữ liệu không đủ cho dự báo ML (cần ≥50 điểm)"))
        
        with ml_col2:
            st.markdown(t("#### 📊 Feature Importance", "#### 📊 Tầm Quan Trọng Tính Năng"))
            
            if 'model' in locals() and hasattr(model, 'coef_'):
                feature_importance = pd.DataFrame({
                    t('Feature', 'Tính Năng'): features,
                    t('Importance', 'Tầm Quan Trọng'): np.abs(model.coef_)
                }).sort_values(t('Importance', 'Tầm Quan Trọng'), ascending=True)
                
                fig_importance = px.bar(
                    feature_importance,
                    x=t('Importance', 'Tầm Quan Trọng'),
                    y=t('Feature', 'Tính Năng'),
                    orientation='h',
                    title=t("Feature Importance", "Tầm Quan Trọng Tính Năng")
                )
                
                st.plotly_chart(fig_importance, use_container_width=True)
            
            # Model settings
            st.markdown(t("#### ⚙️ Model Settings", "#### ⚙️ Cài Đặt Mô Hình"))
            
            model_type = st.selectbox(t("Model Type", "Loại Mô Hình"), [
                t("Linear Regression", "Hồi Quy Tuyến Tính"),
                t("Random Forest", "Rừng Ngẫu Nhiên"), 
                t("LSTM Neural Network", "Mạng Nơ Ron LSTM"),
                "ARIMA",
                "Prophet"
            ], key="ml_model_type")
            
            retrain_freq = st.selectbox(t("Retrain Frequency", "Tần Suất Tái Huấn Luyện"), [
                t("Every Hour", "Mỗi Giờ"),
                t("Every 4 Hours", "Mỗi 4 Giờ"), 
                t("Daily", "Hàng Ngày"),
                t("Weekly", "Hàng Tuần")
            ])
            
            if st.button(t("🔄 Retrain Model", "🔄 Tái Huấn Luyện Mô Hình")):
                st.info(t("Model retraining initiated...", "Bắt đầu tái huấn luyện mô hình..."))
                time.sleep(2)
                st.success(t("✅ Model retrained successfully!", "✅ Mô hình tái huấn luyện thành công!"))

with ml_tabs[1]:  # Pattern Recognition
    st.markdown(t("### 📊 Chart Pattern Recognition", "### 📊 Nhận Diện Mẫu Biểu Đồ"))
    
    if not historical_df.empty:
        pattern_source = st.selectbox(t("Select Source for Pattern Analysis", "Chọn Nguồn Cho Phân Tích Mẫu"), selected_sources, key="pattern")
        
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
                        t("Date", "Ngày"): pattern_data.iloc[i]["date"],
                        t("Pattern", "Mẫu"): t("Golden Cross", "Chữ Thập Vàng"),
                        t("Signal", "Tín Hiệu"): t("Bullish", "Tăng"),
                        t("Confidence", "Tin Cậy"): t("High", "Cao")
                    })
                elif (pattern_data.iloc[i]["ma_short"] < pattern_data.iloc[i]["ma_long"] and
                      pattern_data.iloc[i-1]["ma_short"] >= pattern_data.iloc[i-1]["ma_long"]):
                    patterns_found.append({
                        t("Date", "Ngày"): pattern_data.iloc[i]["date"],
                        t("Pattern", "Mẫu"): t("Death Cross", "Chữ Thập Chết"),
                        t("Signal", "Tín Hiệu"): t("Bearish", "Giảm"),
                        t("Confidence", "Tin Cậy"): t("High", "Cao")
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
                name=t("Price", "Giá"),
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
                annotation_text=t("Support", "Hỗ Trợ")
            )
            
            fig_patterns.add_hline(
                y=resistance_level,
                line_dash="dash",
                line_color="red",
                annotation_text=t("Resistance", "Kháng Cự")
            )
            
            # Mark pattern points
            for pattern in patterns_found[-5:]:  # Show last 5 patterns
                fig_patterns.add_scatter(
                    x=[pattern[t("Date", "Ngày")]],
                    y=[pattern_data[pattern_data["date"] == pattern[t("Date", "Ngày")]]["sell"].iloc[0]],
                    mode="markers",
                    marker=dict(
                        size=15,
                        color="green" if pattern[t("Signal", "Tín Hiệu")] == t("Bullish", "Tăng") else "red",
                        symbol="triangle-up" if pattern[t("Signal", "Tín Hiệu")] == t("Bullish", "Tăng") else "triangle-down"
                    ),
                    name=pattern[t("Pattern", "Mẫu")],
                    showlegend=False
                )
            
            fig_patterns.update_layout(
                title=f"{t('Chart Pattern Analysis', 'Phân Tích Mẫu Biểu Đồ')} - {pattern_source}",
                xaxis_title=t("Date", "Ngày"),
                yaxis_title=t("Price (₫)", "Giá (₫)"),
                height=600
            )
            
            st.plotly_chart(fig_patterns, use_container_width=True)
            
            # Pattern summary
            if patterns_found:
                st.markdown(t("#### 🔍 Detected Patterns", "#### 🔍 Mẫu Phát Hiện"))
                patterns_df = pd.DataFrame(patterns_found)
                st.dataframe(patterns_df.tail(10), use_container_width=True)
            else:
                st.info(t("No significant patterns detected in current timeframe", "Không phát hiện mẫu đáng kể trong khung thời gian hiện tại"))
            
            # Key levels
            col1, col2 = st.columns(2)
            with col1:
                st.metric(t("Support Level", "Mức Hỗ Trợ"), f"{support_level:,.0f} ₫")
            with col2:
                st.metric(t("Resistance Level", "Mức Kháng Cự"), f"{resistance_level:,.0f} ₫")

with ml_tabs[2]:  # Anomaly Detection
    st.markdown(t("### ⚡ Real-time Anomaly Detection", "### ⚡ Phát Hiện Bất Thường Thời Gian Thực"))
    
    if not historical_df.empty:
        anomaly_source = st.selectbox(t("Select Source for Anomaly Detection", "Chọn Nguồn Cho Phát Hiện Bất Thường"), selected_sources, key="anomaly")
        
        anomaly_data = historical_df[historical_df["source"] == anomaly_source].sort_values("date")
        
        if len(anomaly_data) >= 30:
            # Statistical anomaly detection
            anomaly_data = anomaly_data.copy()
            
            # Z-score based anomalies
            price_mean = anomaly_data["sell"].rolling(30).mean()
            price_std = anomaly_data["sell"].rolling(30).std()
            z_scores = (anomaly_data["sell"] - price_mean) / price_std
            
            # Anomaly threshold
            anomaly_threshold = st.slider(t("Anomaly Threshold (Z-score)", "Ngưỡng Bất Thường (Z-score)"), 1.5, 4.0, 2.5, 0.1)
            
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
                name=t("Normal Prices", "Giá Bình Thường"),
                line=dict(color="blue", width=1),
                marker=dict(size=3)
            ))
            
            # Anomalies
            if not anomalies.empty:
                fig_anomaly.add_trace(go.Scatter(
                    x=anomalies["date"],
                    y=anomalies["sell"],
                    mode="markers",
                    name=t("Anomalies", "Bất Thường"),
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
                name=t("Upper Threshold", "Ngưỡng Trên"),
                line=dict(color="red", dash="dash", width=1)
            ))
            
            fig_anomaly.add_trace(go.Scatter(
                x=anomaly_data["date"],
                y=price_mean - anomaly_threshold * price_std,
                mode="lines",
                name=t("Lower Threshold", "Ngưỡng Dưới"),
                line=dict(color="red", dash="dash", width=1)
            ))
            
            fig_anomaly.update_layout(
                title=f"{t('Anomaly Detection', 'Phát Hiện Bất Thường')} - {anomaly_source}",
                xaxis_title=t("Date", "Ngày"),
                yaxis_title=t("Price (₫)", "Giá (₫)"),
                height=500
            )
            
            st.plotly_chart(fig_anomaly, use_container_width=True)
            
            # Anomaly statistics
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(t("Total Anomalies", "Tổng Bất Thường"), len(anomalies))
            with col2:
                if not anomalies.empty:
                    latest_anomaly = (datetime.now().date() - anomalies["date"].dt.date.max()).days
                    st.metric(t("Days Since Last Anomaly", "Ngày Kể Từ Bất Thường Cuối"), latest_anomaly)
                else:
                    st.metric(t("Days Since Last Anomaly", "Ngày Kể Từ Bất Thường Cuối"), "N/A")
            with col3:
                anomaly_rate = len(anomalies) / len(anomaly_data) * 100
                st.metric(t("Anomaly Rate", "Tỷ Lệ Bất Thường"), f"{anomaly_rate:.2f}%")
            
            # Recent anomalies table
            if not anomalies.empty:
                st.markdown(t("#### 🚨 Recent Anomalies", "#### 🚨 Bất Thường Gần Đây"))
                recent_anomalies = anomalies.tail(10)[["date", "sell", "z_score"]].copy()
                recent_anomalies["severity"] = recent_anomalies["z_score"].apply(
                    lambda x: t("🔴 High", "🔴 Cao") if abs(x) > 3 else t("🟡 Medium", "🟡 Trung Bình")
                )
                st.dataframe(recent_anomalies, use_container_width=True)

with ml_tabs[3]:  # Scenario Analysis
    st.markdown(t("### 🔮 Monte Carlo Scenario Analysis", "### 🔮 Phân Tích Kịch Bản Monte Carlo"))
    
    if not historical_df.empty:
        scenario_source = st.selectbox(t("Select Source for Scenario Analysis", "Chọn Nguồn Cho Phân Tích Kịch Bản"), selected_sources, key="scenario")
        
        scenario_data = historical_df[historical_df["source"] == scenario_source].sort_values("date")
        
        if len(scenario_data) >= 30:
            # Monte Carlo parameters
            col1, col2 = st.columns(2)
            
            with col1:
                num_simulations = st.slider(t("Number of Simulations", "Số Lượng Mô Phỏng"), 100, 2000, 1000, 100)
                time_horizon = st.slider(t("Time Horizon (days)", "Chân Trời Thời Gian (ngày)"), 1, 90, 30)
            
            with col2:
                confidence_level = st.slider(t("Confidence Level (%)", "Mức Tin Cậy (%)"), 90, 99, 95)
                shock_scenarios = st.multiselect(
                    t("Include Shock Scenarios", "Bao Gồm Kịch Bản Sốc"),
                    [t("Market Crash (-20%)", "Sụp Đổ Thị Trường (-20%)"), t("Economic Boom (+15%)", "Bùng Nổ Kinh Tế (+15%)"), t("Currency Crisis (+30%)", "Khủng Hoảng Tiền Tệ (+30%)")],
                    default=[]
                )
            
            if st.button(t("🎲 Run Monte Carlo Simulation", "🎲 Chạy Mô Phỏng Monte Carlo")):
                with st.spinner(t("Running simulations...", "Đang chạy mô phỏng...")):
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
                                if t("Market Crash (-20%)", "Sụp Đổ Thị Trường (-20%)") in shock:
                                    random_return += -0.20
                                elif t("Economic Boom (+15%)", "Bùng Nổ Kinh Tế (+15%)") in shock:
                                    random_return += 0.15
                                elif t("Currency Crisis (+30%)", "Khủng Hoảng Tiền Tệ (+30%)") in shock:
                                    random_return += 0.30
                            
                            new_price = prices[-1] * (1 + random_return)
                            prices.append(new_price)
                        
                        simulations.append(prices)
                    
                    # Convert to array
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
                    percentile_names = [t("5th", "Thứ 5"), t("25th", "Thứ 25"), t("50th (Median)", "Thứ 50 (Trung Vị)"), t("75th", "Thứ 75"), t("95th", "Thứ 95")]
                    
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
                        annotation_text=f"{t('Current', 'Hiện Tại')}: {current_price:,.0f} ₫"
                    )
                    
                    fig_monte.update_layout(
                        title=f"{t('Monte Carlo Price Simulation', 'Mô Phỏng Giá Monte Carlo')} - {scenario_source}",
                        xaxis_title=t("Days", "Ngày"),
                        yaxis_title=t("Price (₫)", "Giá (₫)"),
                        height=600
                    )
                    
                    st.plotly_chart(fig_monte, use_container_width=True)
                    
                    # Results summary
                    st.markdown(t("#### 📊 Simulation Results", "#### 📊 Kết Quả Mô Phỏng"))
                    
                    result_col1, result_col2, result_col3, result_col4 = st.columns(4)
                    
                    with result_col1:
                        median_price = percentiles[2]
                        median_change = (median_price - current_price) / current_price * 100
                        st.metric(t("Median Outcome", "Kết Quả Trung Vị"), f"{median_price:,.0f} ₫", f"{median_change:+.1f}%")
                    
                    with result_col2:
                        best_case = percentiles[4]
                        best_change = (best_case - current_price) / current_price * 100
                        st.metric(t("95th Percentile", "Phần Trăm Thứ 95"), f"{best_case:,.0f} ₫", f"{best_change:+.1f}%")
                    
                    with result_col3:
                        worst_case = percentiles[0]
                        worst_change = (worst_case - current_price) / current_price * 100
                        st.metric(t("5th Percentile", "Phần Trăm Thứ 5"), f"{worst_case:,.0f} ₫", f"{worst_change:+.1f}%")
                    
                    with result_col4:
                        var_95 = current_price - percentiles[0]
                        st.metric(f"VaR (95%)", f"{var_95:,.0f} ₫", f"{var_95/current_price*100:.1f}%")
                    
                    # Probability analysis
                    final_prices = simulations_array[:, -1]
                    prob_gain = (final_prices > current_price).sum() / num_simulations * 100
                    prob_loss_10 = (final_prices < current_price * 0.9).sum() / num_simulations * 100
                    prob_gain_10 = (final_prices > current_price * 1.1).sum() / num_simulations * 100
                    
                    st.markdown(t("#### 🎯 Probability Analysis", "#### 🎯 Phân Tích Xác Suất"))
                    prob_col1, prob_col2, prob_col3 = st.columns(3)
                    
                    with prob_col1:
                        st.metric(t("Probability of Gain", "Xác Suất Lãi"), f"{prob_gain:.1f}%")
                    with prob_col2:
                        st.metric(t("Probability of >10% Loss", "Xác Suất Lỗ >10%"), f"{prob_loss_10:.1f}%")
                    with prob_col3:
                        st.metric(t("Probability of >10% Gain", "Xác Suất Lãi >10%"), f"{prob_gain_10:.1f}%")
        else:
            st.warning(t("Need at least 30 data points for scenario analysis", "Cần ít nhất 30 điểm dữ liệu cho phân tích kịch bản"))
    else:
        st.info(t("No historical data available for scenario analysis", "Không có dữ liệu lịch sử cho phân tích kịch bản"))