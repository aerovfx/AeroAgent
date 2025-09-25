#!/usr/bin/env python3
# coding: utf-8
"""
data_learning.py
- Load data from gold_data.db
- Preprocess, compute stats, visualize (matplotlib)
- Forecast (ARIMA). Optionally support Prophet (commented)
Usage:
    python3 data_learning.py
"""

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from datetime import datetime
import numpy as np

DB_FILE = "gold_data.db"

def load_data(db_file: str = DB_FILE) -> pd.DataFrame:
    conn = sqlite3.connect(db_file)
    df = pd.read_sql("SELECT * FROM gold_prices", conn, parse_dates=["timestamp"])
    conn.close()
    if df.empty:
        print("No data in DB.")
        return df
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    # Normalize/cleanup
    df = df.sort_values("timestamp")
    return df

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["spread"] = df["sell"] - df["buy"]
    df["date"] = df["timestamp"].dt.date
    df["hour"] = df["timestamp"].dt.hour
    return df

def basic_stats(df: pd.DataFrame):
    print("=== Basic statistics ===")
    print(df[["buy", "sell", "spread"]].describe())
    print("\nBy source mean sell:")
    print(df.groupby("source")["sell"].mean().sort_values(ascending=False))

def plot_trend(df: pd.DataFrame, out_png: str = "trend.png"):
    plt.figure(figsize=(10,6))
    for src, g in df.groupby("source"):
        plt.plot(g["timestamp"], g["sell"], label=src)
    plt.title("Gold sell price trend")
    plt.xlabel("time")
    plt.ylabel("VND")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(out_png)
    print(f"Saved plot to {out_png}")

def forecast_arima(df: pd.DataFrame, source: str, steps: int = 7):
    series = df[df["source"] == source].sort_values("timestamp")["sell"].dropna()
    if len(series) < 15:
        print(f"Not enough data to forecast for {source} (need >=15 points).")
        return None
    # make index continuous 0..N-1 for ARIMA
    series = series.reset_index(drop=True)
    try:
        model = ARIMA(series, order=(1,1,1))
        model_fit = model.fit()
        fc = model_fit.forecast(steps=steps)
        print(f"Forecast for {source} next {steps} steps:")
        print(fc)
        return fc
    except Exception as e:
        print("ARIMA error:", e)
        return None

if __name__ == "__main__":
    df = load_data()
    if df.empty:
        exit(0)
    df = preprocess(df)
    basic_stats(df)
    plot_trend(df, out_png="trend.png")
    # Example forecast for the first source
    first_src = df["source"].unique()[0]
    forecast = forecast_arima(df, first_src, steps=7)