from dataclasses import dataclass
import itertools
import datetime as dt
import urllib.request
import requests


@dataclass
class StaticInfo:
    google_trends_kw = ['Dogs', 'Cats']
    currencies = ['USD']
    keywords = ['Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']
    crypto_tickers = ['BTC', 'ETH']
    tickers = {"INTEL":'INTC',"UBER": 'UBER',"TESLA": 'TSLA','ADOBE': 'ADBE'}
    intervals = ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']
    periods = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']


class LejziTime:
    def __init__(self):
        self.today = dt.datetime.now()
        self.today_UTC = dt.datetime.utcnow()
        self.yesterday = self.today - dt.timedelta(days=1)
        self.time_now = dt.datetime.now().time()

    @staticmethod
    def around_x_day(x_day):
        x_yd = x_day - dt.timedelta(days=1)
        x_nd = x_day + dt.timedelta(days=1)
        return x_yd, x_nd

    @staticmethod
    def week_back(x_day):
        week_ago = x_day - dt.timedelta(days=7)
        return week_ago, x_day


    def x_days_ago_till_now(self, x_days):
        x_days_ago = self.today - dt.timedelta(days=x_days)

        return x_days_ago, self.today

    def x_days_ago(self, x_days):
        x_days_ago = self.today - dt.timedelta(days=x_days)
        delta = x_days_ago.replace(hour=23, minute=59, second=59, microsecond=0)
        x_days_ago = x_days_ago.replace(hour=0, minute=0, second=0, microsecond=0)
        return x_days_ago, delta


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + dt.timedelta(n)