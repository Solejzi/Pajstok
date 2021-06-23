import yfinance as yf
import datetime as dt
import pandas_datareader as web
import pandas as pd
from  static import StaticInfo as sti

td = dt.datetime.utcnow().date()
yd = td - dt.timedelta(days=1)
tn = dt.datetime.now().time()


def multi_day_crypto(tickers, metric, start, end):
    df = web.DataReader(f'{tickers[0]}-{sti.currencies[0]}', "yahoo", start=start, end=end)
    combined = df[[metric]].copy()
    colnames = []
    colnames.append(tickers[0])
    combined.columns = colnames
    for ticker in tickers[1:]:
        df = web.DataReader(f'{ticker}-{sti.currencies[0]}', "yahoo", (td - dt.timedelta(days=30)), td)
        colnames.append(ticker)
        combined = combined.join(df[metric])
        combined.columns = colnames
    return combined


def multi_day_stocks(tickers, metric, start, end):
    df = web.DataReader(tickers, "yahoo", start=start, end=end)
    combined = df[[metric]].copy()
    colnames = []
    colnames.append(tickers)
    print(tickers)
    combined.columns = colnames
    '''for ticker in tickers[1:]:
        df = web.DataReader(ticker, "yahoo",  start=start, end=end)
        colnames.append(ticker)
        combined = combined.join(df[metric])
        combined.columns = colnames
    '''
    return combined


def multi_day_data(tickers, interval, start, end, group_by='ticker', *labels):
    companies_data = yf.download(tickers=tickers, start=start, end=end, interval=interval, group_by=group_by,
                                 rounding=True)
    companies_data = companies_data[labels]
    return companies_data


def yesterdays_data(tickers, period='1d', interval='1m', start=yd, group_by='ticker', *labels):
    companies_data = yf.download(tickers=tickers, start=start, period=period, interval=interval, group_by=group_by, rounding=True)
    companies_data = companies_data[labels]
    return companies_data


def history_data(ticker, start, end, interval):
    company = yf.Ticker(ticker)
    historical = company.history(start=start, end=end, interval=interval)
    return historical


def company_info(ticker):
    company = yf.Ticker(ticker)
    return company.info






