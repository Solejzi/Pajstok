import yfinance as yf
import datetime as dt
from static import LejziTime as lTime
from static import StaticInfo as sti
lt = lTime()
td = dt.datetime.utcnow().date()
yd = td - dt.timedelta(days=1)
tn = dt.datetime.now().time()



class YahooF:
    """
        USE yahoo_pandas instead - yfinance just as a support


        When I look in the yfinance .py files, I find lines of code like:

                r = _requests.get(url=url, proxies=proxy).json()

        You may need to modify the lines to include the 'verify=False' statement to look something like this:

                request.get(url=url, proxies=proxy, verify=False).json()

        I'm not entirely sure if 'verify=False' is allowed when you use proxies. You could try adding it to the
         request lines in the .py file and see if that does the trick.

        from:
            https://stackoverflow.com/questions/62061609/error-in-downloading-stock-price-data-from-yahoo-finance-using-yfinance-in-pytho
        also:
            https://github.com/ranaroussi/yfinance/issues/359
    """
    def __init__(self, **kwargs):
        self.kwargs = kwargs


    def multi_day_data(self):
        companies_data = yf.download(tickers=self.kwargs['tickers'], start=self.kwargs['time_spectrum'][0],
                                     end=self.kwargs['time_spectrum'][1], interval=self.kwargs['interval'],
                                     group_by=self.kwargs['group_by'], rounding=True)

        companies_data = companies_data[self.kwargs['labels']]
        return companies_data

    def yesterdays_data(self, period='1d', interval='1m', start=yd, group_by='ticker'):
        companies_data = yf.download(tickers=self.kwargs['tickers'], start=start, period=period, interval=interval,
                                     group_by=group_by, rounding=True)
        companies_data = companies_data[self.kwargs['labels']]
        return companies_data

    def historical_data(self):
        company = yf.Ticker(self.kwargs['ticker'])
        historical = company.history(start=self.kwargs['start'], end=self.kwargs['end'], interval=self.kwargs['interval'])
        return historical

    def company_info(self):
        company = yf.Ticker(self.kwargs['ticker'])
        return company.info


if __name__ == '__main__':

    y =  yf.download(tickers=sti.tickers['INTEL'], start=yd, period='1d', interval='1m')
    print(y)
    print(type(y))

