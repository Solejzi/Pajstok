import pandas as pd
from yf_API import company_info, multi_day_data, multi_day_crypto, yesterdays_data, multi_day_stocks
from static import StaticInfo as sti
import matplotlib.pyplot as plt
from pprint import pprint
import datetime as dt
from dateutil.relativedelta import relativedelta


td = dt.datetime.utcnow().date()
yd = td - dt.timedelta(days=1)
tn = dt.datetime.now().time()


class DataMaker:
    def __init__(self, API):

        self.today = dt.datetime.utcnow().date()
        self.yesterd = self.today - dt.timedelta(days=1)
        self.time_now = dt.datetime.now().time()
        self.API = API

    def year(self, metric):
        if self.API == 'yh2':
            df = multi_day_stocks(sti.tickers[0], metric, td-dt.timedelta(days=365), td )
            return df

    def yesterday(self, metric):
        if self.API == 'yh':
            df = yesterdays_data(sti.tickers)
            keys = df.keys()
            final_df = df[keys]
            return final_df
        if self.API == 'yh2':

            df = multi_day_crypto(sti.crypto_tickers, metric, td-dt.timedelta(days=365), td )
            df = multi_day_stocks(sti.tickers, metric, td-dt.timedelta(days=365), td )
            return df

    def last_week(self):
        if self.API == 'yh':
            df = multi_day_data(sti.tickers, sti.intervals[5], self.today-dt.timedelta(days=7), self.today)
            keys = df.keys()
            final_df = df[keys]
            return final_df

    def last_30_days(self):
        if self.API == 'yh':
            df = multi_day_data(sti.tickers[0], sti.intervals[8], self.today-dt.timedelta(days=30), self.today)
            keys = [key[1] for key in df.keys()]
            final_df = df[keys]
            return final_df

    def last_x_years(self, years, labels=('Open', 'Close', 'High', 'Low')):

        if self.API == 'yh':
            df = multi_day_data(sti.tickers[0], sti.intervals[8], self.today - relativedelta(years=years), self.today)
            print(df)
            columnsData = df.loc[:, [key for key in df.keys()]]
            print(columnsData)
            final_df = df.iloc[labels]


            return final_df


    def final_df(self, df):
        return df

