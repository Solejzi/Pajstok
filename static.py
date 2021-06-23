from dataclasses import dataclass
import itertools

#TODO DOWNLOAD ALL THE TICKERS DIRECTLY FROM WWW


@dataclass
class StaticInfo:
    currencies = ['USD']
    keywords = ['Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']
    crypto_tickers = ['BTC', 'ETH']
    tickers = ['INTC', 'UBER', 'TSLA', 'ADBE']
    intervals = ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']
    periods = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']

