from bs4 import BeautifulSoup
import requests
az = 'abc'.upper()
az = list(az)


class Tickers:
    def __init__(self, **kwargs):
        self.markets_url = 'https://eoddata.com/symbols.aspx'
        self.url = 'https://eoddata.com/stocklist/'
        self.ticker_list = []
        self.kwargs = kwargs

    def get_markets_list(self):
        if not self.kwargs:
            markets_list = []
            source = requests.get(self.markets_url).text
            soup = BeautifulSoup(source, 'lxml')
            select = soup.findAll('option')
            for i in select:
                attribute = i.attrs
                markets_list.append(attribute['value'])
            return markets_list
        # TODO user choice of markets
        else:
            markets_list = []
            source = requests.get(self.markets_url).text
            soup = BeautifulSoup(source, 'lxml')
            select = soup.findAll('option')
            for i in select:
                attribute = i.attrs
                markets_list.append(attribute['value'])
            return markets_list

    def scrape(self):
        markets_list = self.get_markets_list()
        for market in markets_list[:1]:
            for letter in az:
                url = self.url + market
                url = url + '/' + letter + '.htm'
                source = requests.get(url).text
                soup = BeautifulSoup(source, 'lxml')
                soup = soup.find('table', {"class": "quotes"})
                children = soup.findChildren("tr")

                for child in children[:5]:
                    # TODO **BOMB POINT**
                    if len(child) > 8:
                        name = child.td.findNext('td')
                        try:
                            name = name.text
                            a_tag = child.a.text
                            self.ticker_list.append([name, a_tag])
                        except:
                            pass

        return self.ticker_list


def scrape_tickers(**kwargs):
    """
        Returns dict of tickers ::  {'company name': 'ticker'
                                            ...
                                            ...
                                            ...
                                    'company name': 'ticker'}
    """
    return Tickers(**kwargs).scrape()



