import http.client
from Keys import api_keys
import inspect
import json
ApiKeys = api_keys.ApiKeys


class Carbon(object):

    """
        country (required)	String	The country's two letter ISO 3166-1 alpha-2 code.
        year (required on free plans)	String	The year to get the holiday(s) from. Note that this is optional on paid plans, and if left blank it will default to the current year.
        month (required on free plans)	String	The month to get the holiday(s) from, in the format of 1-12 (e.g., 1 is January, 2 is February, etc). Note that this is optional on paid plans, and if left blank it will default to the current month.
        day (required on free plans)	String	The day to get the holiday(s) from, in the format of 1-31. Note that this is optional on paid plans, and if left blank it will default to the current day.
    """

    def __init__(self, **kwargs):
        self.api_link = 'www.carboninterface.com/api/v1'
        self.conn = http.client.HTTPSConnection(self.api_link)
        self.headers = {'Authorization': self.api_link}
        self.kwargs = kwargs
        self.types = ['estimates', ]

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

    def electricity(self):

        """type 	string 	electricity
            electricity_unit optional 	string 	Can be either megawatt hours mwh or kilowatt hours kwh. If a unit is not provided, mwh is the default.
            electricity_value 	decimal 	Value of the unit of electricity consumption or generation noted above.
            country 	string 	Set to the country you need emissions data on for electricity consumption. Currently, Carbon Interface supports North American and European countries and sub-regions. Visit our geographic coverage page to see what countries and regions are supported. The country must be passed through using the country’s ISO 3166 country code found here.
            state optional 	string 	Proving the state will allow the API to generate a more accurate eletrcitiy emissions estimate. Emissions data from electricity generation from all Canadian provinces and US states is supported. The state param needs to be the two letter ISO state code."""

        return self.conn.request("GET", f"{self.endpoint(**self.kwargs)}", headers=self.headers)

    def get_data(self):
        conn = http.client.HTTPSConnection(self.api_link)
        conn.request("GET", self.api_link)
        res = conn.getresponse()

        data = res.read()
        data = data.decode("UTF-8")
        data = json.loads(data)

        return data
