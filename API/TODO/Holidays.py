import requests
import http.client
from Keys import api_keys
import inspect
import json
ApiKeys = api_keys.ApiKeys


class Holidays(object):

    """
        country (required)	String	The country's two letter ISO 3166-1 alpha-2 code.
        year (required on free plans)	String	The year to get the holiday(s) from. Note that this is optional on paid plans, and if left blank it will default to the current year.
        month (required on free plans)	String	The month to get the holiday(s) from, in the format of 1-12 (e.g., 1 is January, 2 is February, etc). Note that this is optional on paid plans, and if left blank it will default to the current month.
        day (required on free plans)	String	The day to get the holiday(s) from, in the format of 1-31. Note that this is optional on paid plans, and if left blank it will default to the current day.
    """

    def __init__(self, **kwargs):
        self.api_link = 'http://holidays.abstractapi.com/v1/?api_key=' + ApiKeys.holidays
        print(self.api_link)
        self.api_link = self.api_link + self.endpoint(**kwargs)
        print(self.api_link)
        self.headers = {}
        self.conn = http.client.HTTPSConnection(self.api_link)
    @staticmethod
    def endpoint(**kwargs):
        if kwargs:
            end_point = '&'
            for k, v in kwargs.items():
                kv_str = f'{k}={v}&'
                end_point = end_point + kv_str
            end_point = end_point[:-1]  # get rid of last &
            return end_point
        else:
            return ''

    def seasons(self):
        return self.conn.request("GET", f"{self.api_link}", headers=self.headers)

    def get_data(self):
        self.seasons()

        self.conn.request("GET", self.api_link)
        res = self.conn.getresponse()

        data = res.read()
        data = data.decode("UTF-8")
        data = json.loads(data)

        return data


h = Holidays(country='PL', year=2000, month=1, day=1).get_data()
print(h)
