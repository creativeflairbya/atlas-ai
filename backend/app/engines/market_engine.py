
# app/engines/market_engine.py

import ccxt

exchange = ccxt.binance()

async def get_market_data(data):

    symbol = data.get("symbol", "BTC/USDT")
    timeframe = data.get("timeframe", "15m")

    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=100)

    return {
        "symbol": symbol,
        "timeframe": timeframe,
        "ohlcv": ohlcv
    }
