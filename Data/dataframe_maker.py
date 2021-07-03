import datetime as dt
from dateutil.relativedelta import relativedelta
import inspect
import pandas as pd
from API import weather, APIfb, yahoof, yahoo_pandas
from API.web_scrap import scrapp


from static import StaticInfo as sti
from static import LejziTime as lTime

lt = lTime()


class DataGetter:
    # TODO different dates on same lt.week_back-time_spectrum  - > weather - crypto - football etc
    """
        API's ::    'WH' -> weather api (meteostat, geocoder), 'YF' -> YAHOO FINANCE api (yfinance),
                    'YP' -> YAHOO FINANCE api using pandas (pandas_datareader), mode=[STOCKS, CRYPTO]
                    'GT' -> trends api (pytrends), 'TT' -> Twitter api (tweepy),
                    'AFB' -> APIFootball, mode=['Football, 'Basketball', 'Hockey', 'NBA', 'F1'],
                    'SCRAP' -> scraping (bs4), mode=[Tickers]

    """
    def __init__(self, api, **kwargs):
        self.API = api
        self.kwargs = kwargs
        self.df = pd.DataFrame()

    def get_data(self, *func, **data_kwargs):

        if self.API == 'YP':
            if self.kwargs['mode'] == 'STOCKS':
                data = yahoo_pandas.multi_day_stocks(**data_kwargs)
                return data
            if self.kwargs['mode'] == 'CRYPTO':
                data = yahoo_pandas.multi_day_crypto(**data_kwargs)
                return data

        if self.API == 'WH':
            cities_wh = weather.get_weather_data(**data_kwargs)
            return cities_wh

        if self.API == 'AFB':

            if data_kwargs.get('list_funcs') is not None:
                if self.kwargs['sport'] == 'Football':
                    sport = APIfb.FootApi(**data_kwargs)
                    methods = APIfb.fba_sport_methods(sport)
                    return methods
                elif self.kwargs['sport'] == 'Basketball':
                    sport = APIfb.BasketApi(**data_kwargs)
                    methods = APIfb.fba_sport_methods(sport)
                    return methods
                elif self.kwargs['sport'] == 'Hockey':
                    sport = APIfb.FootApi(**data_kwargs)
                    methods = APIfb.fba_sport_methods(sport)
                    return methods
                elif self.kwargs['sport'] == 'NBA':
                    sport = APIfb.FootApi(**data_kwargs)
                    methods = APIfb.fba_sport_methods(sport)
                    return methods
                elif self.kwargs['sport'] == 'F1':
                    sport = APIfb.FootApi(**data_kwargs)
                    methods = APIfb.fba_sport_methods(sport)
                    return methods
            else:

                if self.kwargs['mode'] == 'Football':
                    sport = APIfb.FootApi(**data_kwargs)
                    return APIfb.fba_sports(sport, *func)
                elif self.kwargs['mode'] == 'Basketball':
                    sport = APIfb.BasketApi(**data_kwargs)
                    return APIfb.fba_sports(sport, *func)
                elif self.kwargs['mode'] == 'Hockey':
                    sport = APIfb.FootApi(**data_kwargs)
                    return APIfb.fba_sports(sport, *func)
                elif self.kwargs['mode'] == 'NBA':
                    sport = APIfb.FootApi(**data_kwargs)
                    return APIfb.fba_sports(sport, *func)
                elif self.kwargs['mode'] == 'F1':
                    sport = APIfb.F1Api(**data_kwargs)
                    return APIfb.fba_sports(sport, *func)

        if self.API == 'YF':
            yf = yahoof.YahooF(**data_kwargs)


        # TODO - save rows into df
        if self.API == 'SCRAP':
            if self.kwargs['mode'] == 'Tickers':
                # tickers dict
                d = {'Name': [], 'Ticker': []}
                data = scrapp.scrape_tickers()
                for row in data:
                    print(row)

        elif self.API == 'GT':
            pass
        elif self.API == 'TT':
            pass


class DataShaper:
    def __init__(self, api, **kwargs):

        """
            Reshapes data from api calls to either:
                {'Table name': pandas.core.frame.DataFrame}
            or
                {'Table name': {repons dict}}
        """
        self.API = api
        self.DG = DataGetter(self.API, **kwargs)
        self.table_name = kwargs['mode']

    def to_df(self, *args, **kwargs):
        if self.API == 'WH':
            data = self.DG.get_data(*args, **kwargs)
            return data
        if self.API == 'AFB':
            data = self.DG.get_data(*args, **kwargs)
            data = {self.table_name: data['response']}

            return data
        if self.API == 'WH':
            data = self.DG.get_data(*args, **kwargs)
            return data
        if self.API == 'WH':
            data = self.DG.get_data(*args, **kwargs)
            return data


if __name__ == '__main__':
    pass
    # APIFootball call => DataMaker param :: sport = 'Sport', get_data params :: *args - method, **kwargs - filters
    # returns respond as python dict

    # fb = DataGetter('AFB', mode='Football').get_data('leagues', type='cup')
    # print(fb)

    # bb = DataGetter('AFB', mode='Basketball').get_data('leagues', type='cup')
    # print(fb)

    f1 = DataShaper('AFB', mode='F1').to_df('drivers', search='lewi')
    print(f1)

    # Get sport methods :: get data kwarg[list_func] other than None

    # DataGetter('AFB', sport='Football').get_data(list_funcs=1)
    # DataGetter('AFB', sport='Basketball').get_data(list_funcs=1)
    # DataGetter('AFB', sport='Hockey').get_data(list_funcs=1)
    # DataGetter('AFB', sport='F1').get_data(list_funcs=1)

    # weather API call => get_data params :: cities, time_spectrum, period
    # DataGetter('WH').get_data(cities=['Gdynia', 'Sopot'], time_spectrum=lt.week_back(lt.today_UTC), period='Hourly')




