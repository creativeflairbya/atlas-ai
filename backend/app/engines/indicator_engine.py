
# app/engines/indicator_engine.py

import pandas as pd
import ta

def calculate_indicators(market):

    df = pd.DataFrame(market["ohlcv"], columns=[
        "time", "open", "high", "low", "close", "volume"
    ])

    df["ema20"] = ta.trend.ema_indicator(df["close"], window=20)
    df["ema50"] = ta.trend.ema_indicator(df["close"], window=50)
    df["rsi"] = ta.momentum.rsi(df["close"], window=14)

    return {
        "ema20": df["ema20"].iloc[-1],
        "ema50": df["ema50"].iloc[-1],
        "rsi": df["rsi"].iloc[-1],
    }
