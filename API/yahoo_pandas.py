import pandas_datareader as web
import datetime as dt

from static import StaticInfo as sti
from static import LejziTime as lTime

lt = lTime()
td = dt.datetime.utcnow().date()
yd = td - dt.timedelta(days=1)
tn = dt.datetime.now().time()


def multi_day_crypto(tickers, metric, start, end):
    df = web.DataReader(f'{tickers[0]}-{sti.currencies[0]}', "yahoo", start=start, end=end)
    combined = df[[metric]].copy()
    colnames = [tickers[0]]
    combined.columns = colnames
    for ticker in tickers[1:]:
        colnames.append(ticker)
        combined = combined.join(df[metric])
        combined.columns = colnames
    return combined


def multi_day_stocks(**kwargs):
    df = web.DataReader([ticker for ticker in kwargs['tickers'].values()],
                        "yahoo", start=kwargs['time_spectrum'][0], end=kwargs['time_spectrum'][1])

    # TODO get only metrics columns
    combined = df[kwargs['metric']].copy()
    colnames = [kwargs['tickers'].keys()]

    combined.columns = colnames
    for ticker in kwargs['tickers'][1:]:
        colnames.append(ticker)
        combined = combined.join(kwargs['metric'])
        combined.columns = colnames
    return combined


if __name__ == '__main__':

    week = lt.week_back(lt.today)
    m = multi_day_crypto(sti.crypto_tickers, 'Open', week[0], week[1])
    s = multi_day_stocks(tickers=sti.tickers, time_spectrum=lt.week_back(lt.today), metric='Open')



