import http.client
import json
from Keys import api_keys
import json
import inspect
ApiKeys = api_keys.ApiKeys


class AFB:
    """
        response ::
         {'get': 'teams\\/seasons', 'parameters': {'team': '2'}, 'errors': [],
         'results': 10, 'paging': {'current': 1, 'total': 1},
          'response': [2008, 2010, 2012, 2014, 2016, 2017, 2018, 2019, 2020, 2021]}
    """
    def __init__(self, api_link, api_key, **kwargs):
        self.conn = http.client.HTTPSConnection(api_link)
        self.headers = {'x-rapidapi-host': api_link, 'x-rapidapi-key': api_key}
        self.kwargs = kwargs


    @staticmethod
    def endpoint(**kwargs):
        if kwargs:
            end_point = '?'
            for k, v in kwargs.items():
                kv_str = f'{k}={v}&'
                end_point = end_point + kv_str
            end_point = end_point[:-1]  # get rid of last &
            return end_point
        else:
            return ''

    def get_data(self, request):
        sports_methods = inspect.getmembers(self, predicate=inspect.ismethod)
        # TODO works only because there is __init__ and no other dunders in Apifb.AFB object
        sports_methods = dict(sports_methods[1:])
        sports_methods[request]()
        res = self.conn.getresponse()
        data = res.read()
        data = data.decode("UTF-8")
        data = json.loads(data)

        return data


class FootApi(AFB):
    def __init__(self, **kwargs):
        super().__init__("v3.football.api-sports.io", ApiKeys.AFB_keys['football'], **kwargs)

    def seasons(self):
        return self.conn.request("GET", "/leagues/seasons", headers=self.headers)

    def list_countries(self):
        """
        name	stringThe name of the country
        code string 2 characters FR, GB, IT ...The Alpha2 code of the country
        search	string 3 characters The name of the country

        """
        return self.conn.request("GET", f"/countries{self.endpoint(**self.kwargs)}", headers=self.headers)

    def timezone(self):
        return self.conn.request("GET", "/timezone", headers=self.headers)

    def leagues(self):
        """**kwargs ::
            id	integerThe id of the league
            name	stringThe name of the league
            country	stringThe country name of the league
            code	string 2 characters FR, GB, IT…The Alpha2 code of the country
            season	integer 4 characters YYYYThe season of the league
            team	integerThe id of the team
            type	string Enum: "league" "cup"The type of the league
            current	stringEnum: "true" "false"The state of the league
            search	string >= 3 charactersThe name or the country of the league
            last	integer <= 2 charactersThe X last leagues/cups added in the API"""
        return self.conn.request("GET", f"/leagues{self.endpoint(**self.kwargs)}", headers=self.headers)

    def team_by_id(self):
        """ **kwargs ::
            id integer :: The id of the team
            name string The name of the team
            league integer  The id of the league
            season integer 4 characters YYYY The season of the league
            country	string The country name of the team
            search	string >= 3 characters The name or the country name of the team"""
        return self.conn.request("GET", f"/teams{self.endpoint(**self.kwargs)}", headers=self.headers)

    def venues(self):
        """ NOT IMPLEMENTED FOR BSKTBLL"""
        return self.conn.request("GET", f"/venues{self.endpoint(**self.kwargs)}", headers=self.headers)

    def team_statistics(self):
        """ **kwargs ::
        league required integer The id of the league
        season required integer 4 characters YYYYThe season of the league
        team required integerThe id of the team
        date string YYYY-MM-DDThe limit date"""
        return self.conn.request("GET", f"/teams/statistics{self.endpoint(**self.kwargs)}", headers=self.headers)

    def team_seasons(self):
        """ **kwargs :: team required integer The id of the team"""
        return self.conn.request("GET", f"/teams/seasons{self.endpoint(**self.kwargs)}", headers=self.headers)

    def standings(self):
        """ **kwargs ::
        league integer The id of the league
        season required integer 4 characters YYYY The season of the league
        team	integer The id of the team"""

        return self.conn.request("GET", f"/standings{self.endpoint(**self.kwargs)}", headers=self.headers)

    def rounds(self):
        """leaguerequiredintegerThe id of the league
            seasonrequiredinteger 4 characters YYYYThe season of the league
            current	boolean Enum: "true" "false" The current round only"""
        return self.conn.request("GET", f"/fixtures/rounds{self.endpoint(**self.kwargs)}", headers=self.headers)

    def fixtures(self):
        """**kwargs::
            id	integerThe id of the fixture
            live stringEnum: "all" "id-id"
            date	stringYYYY-MM-DDA valid date
            leagueintegerThe id of the league
            season	integer 4 characters YYYYThe season of the league
            team	integerThe id of the team
            last	integer <= 2 charactersFor the X last fixtures
            next	integer <= 2 charactersFor the X next fixtures
            from	stringYYYY-MM-DDA valid date
            to	stringYYYY-MM-DDA valid date
            roundstringThe round of the fixture
            statusstringThe status short of the fixture
            timezonestringA valid timezone from the endpoint Timezone"""

        return self.conn.request("GET", f"/fixtures{self.endpoint(**self.kwargs)}", headers=self.headers)

    def head_to_head(self):
        """ h2hrequiredstringID-IDThe ids of the teams
            datestringYYYY-MM-DD
            leagueintegerThe id of the league
            season	integer 4 characters YYYYThe season of the league
            last	integerFor the X last fixtures
            next	integerFor the X next fixtures
            fromstringYYYY-MM-DD
            to	stringYYYY-MM-DD
            statusstringThe status short of the fixture
            timezonestringA valid timezone from the endpoint Timezone"""

        return self.conn.request("GET", f"/fixtures/headtohead{self.endpoint(**self.kwargs)}", headers=self.headers)

    def statistics(self):
        """fixturerequiredintegerThe id of the fixture
            team	int`egerThe id of the team
            type	str`ingThe type of statistics"""

        return self.conn.request("GET", f"/fixtures/statistics{self.endpoint(**self.kwargs)}", headers=self.headers)

    def events(self):
        """ fixturerequiredintegerThe id of the fixture
            team	integerThe id of the team
            playerintegerThe id of the player
            typestringThe type"""

        return self.conn.request("GET", f"/fixtures/events{self.endpoint(**self.kwargs)}", headers=self.headers)

    def lineup(self):
        """fixturerequiredintegerThe id of the fixture
            team	integerThe id of the team
            player	integerThe id of the player
            type	stringThe type"""

        return self.conn.request("GET", f"/fixtures/lineups{self.endpoint(**self.kwargs)}", headers=self.headers)

    def player_stats(self):
        """fixturerequiredintegerThe id of the fixture
            team	integerThe id of the team"""

        return self.conn.request("GET", f"/fixtures/players{self.endpoint(**self.kwargs)}", headers=self.headers)

    def players_out(self):
        """league	integerThe id of the league
            season	integer 4 characters YYYYThe season of the league, required with league, team and player parameters
            fixtureintegerThe id of the fixture
            team	integerThe id of the team
            playerintegerThe id of the player
            date	stringYYYY-MM-DDA valid date
            timezonestringA valid timezone from the endpoint Timezone"""

        return self.conn.request("GET", f"/injuries{self.endpoint(**self.kwargs)}", headers=self.headers)

    def predictions(self):
        """fixturerequiredintegerThe id of the fixture"""
        return self.conn.request("GET", f"/predictions{self.endpoint(**self.kwargs)}", headers=self.headers)

    def coach(self):
        """id	integerThe id of the coach
            team	integerThe id of the team
            search	string >= 3 charactersThe name of the coach"""

        return self.conn.request("GET", f"/coachs{self.endpoint(**self.kwargs)}", headers=self.headers)

    def player(self):
        """idintegerThe id of the player
            team	integerThe id of the team
            leagueintegerThe id of the league
            season	integer 4 characters YYYY | Requires the fields Id, League or Team...The season of the league
            search	string >= 4 characters Requires the fields League or TeamThe name of the player
            page	integerDefault: 1Use for the pagination"""

        return self.conn.request("GET", f"/players{self.endpoint(**self.kwargs)}", headers=self.headers)

    def player_season(self):
        """player	integerThe id of the player"""

        return self.conn.request("GET", f"/players/seasons{self.endpoint(**self.kwargs)}", headers=self.headers)

    def top_score(self):
        """league required integerThe id of the league
            season required integer 4 characters YYYYThe season of the league"""

        return self.conn.request("GET", f"/players/topscorers{self.endpoint(**self.kwargs)}", headers=self.headers)

    def top_assists(self):

        """league required integerThe id of the league
                    season required integer 4 characters YYYYThe season of the league"""

        return self.conn.request("GET", f"/players/topassists{self.endpoint(**self.kwargs)}", headers=self.headers)

    def top_yellow(self):
        """league required integerThe id of the league
                    season required integer 4 characters YYYYThe season of the league"""
        return self.conn.request("GET", f"/players/topyellowcards{self.endpoint(**self.kwargs)}", headers=self.headers)

    def top_red(self):
        """league required integerThe id of the league
                    season required integer 4 characters YYYYThe season of the league"""

        return self.conn.request("GET", f"/players/topredcards{self.endpoint(**self.kwargs)}", headers=self.headers)

    def transfers(self):
        """player	integer The id of the player
            team	integerThe id of the team"""

        return self.conn.request("GET", f"/transfers{self.endpoint(**self.kwargs)}", headers=self.headers)

    def trophies(self):
        """player	integerThe id of the player
            coach	integerThe id of the coach"""

        return self.conn.request("GET", f"/trophies{self.endpoint(**self.kwargs)}", headers=self.headers)

    def sidelines(self):
        """player	integerThe id of the player
            coach	integerThe id of the coach"""
        return self.conn.request("GET", f"/sidelined{self.endpoint(**self.kwargs)}", headers=self.headers)


class Hockey(AFB):
    def __init__(self, **kwargs):
        super().__init__("/v1.hockey.api-sports.io", ApiKeys.AFB_keys['hockey'], **kwargs)
    # TODO TBL


class BasketApi(AFB):

    # TODO implement ODDS responds

    def __init__(self, **kwargs):
        super().__init__("v1.basketball.api-sports.io", ApiKeys.AFB_keys['football'], **kwargs)
    def timezone(self):
        return self.conn.request("GET", "/timezone", headers=self.headers)
    def seasons(self):
        return self.conn.request("GET", "/leagues/seasons", headers=self.headers)
    def list_countries(self):
        """
            id	integerThe id of the country
            name	stringThe name of the country
            code	string 2 characters Example: code=EN, IT, FR The code of the country
            search	string >= 3 characters
        """
        return self.conn.request("GET", f"/countries{self.endpoint(**self.kwargs)}", headers=self.headers)
    def leagues(self):
        """"""
        """**kwargs ::
            id	integerThe id of the league
            name	stringThe name of the league
            country	stringThe country name of the league
            country_id integer The id of the country
            code	string 2 characters FR, GB, IT…The Alpha2 code of the country
            season	integer 4 characters YYYYThe season of the league
            type	string Enum: "league" "cup"The type of the league
            search	string >= 3 charactersThe name or the country of the league
            """
        return self.conn.request("GET", f"/leagues{self.endpoint(**self.kwargs)}", headers=self.headers)

    def team_by_id(self):
        """ **kwargs ::
            id integer :: The id of the team
            name string The name of the team
            league integer  The id of the league
            season integer 4 characters YYYY The season of the league
            search	string >= 3 characters The name or the country name of the team"""
        return self.conn.request("GET", f"/teams{self.endpoint(**self.kwargs)}", headers=self.headers)
    def team_statistics(self):
        """ **kwargs ::
        league required integer The id of the league
        season required integer 4 characters YYYYThe season of the league
        team required integerThe id of the team
        date string YYYY-MM-DDThe limit date"""
        return self.conn.request("GET", f"/teams/statistics{self.endpoint(**self.kwargs)}", headers=self.headers)


    def standings(self):
        """ **kwargs ::
        league integer The id of the league
        season required integer 4 characters YYYY The season of the league
        team	integer The id of the team
        stage	string A valid stage
        group	string A valid group"""

        return self.conn.request("GET", f"/standings{self.endpoint(**self.kwargs)}", headers=self.headers)

    def standings_stages(self):
        """ **kwargs ::
            league required integer The id of the league
            season required string 4 characters The season of the league"""

        return self.conn.request("GET", f"/standings/stages{self.endpoint(**self.kwargs)}", headers=self.headers)

    def standings_groups(self):
        """ **kwargs ::
            league required integer The id of the league
            season required string 4 characters The season of the league"""

        return self.conn.request("GET", f"/standings/groups{self.endpoint(**self.kwargs)}", headers=self.headers)
    def games(self):
        """
            **kwargs ::
            id integer The id of the game
            date	stringA valid date
            league	integerThe id of the league
            season	integer 4 charactersThe season of the league
            team	integerThe id of the team
            timezone	stringA valid timezone
        """
        return self.conn.request("GET", f"/games{self.endpoint(**self.kwargs)}", headers=self.headers)


    def head_to_head(self):
        """ h2h required string ID-IDThe ids of the teams
            date stringYYYY-MM-DD
            league integerThe id of the league
            season	integer 4 characters YYYYThe season of the league
            timezone stringA valid timezone from the endpoint Timezone"""

        return self.conn.request("GET", f"/games{self.endpoint(**self.kwargs)}", headers=self.headers)


class F1Api(AFB):
    def __init__(self, **kwargs):
        super().__init__("v1.formula-1.api-sports.io", ApiKeys.AFB_keys['f1'], **kwargs)

    def timezone(self):
        return self.conn.request("GET", "/timezone", headers=self.headers)

    def seasons(self):
        return self.conn.request("GET", "/leagues/seasons", headers=self.headers)

    def competitions(self):
        """
            id	integer The id of the competition
            name	string The name of the competition
            country	string The name of the country
            city	string The name of the city
            search	string >= 3 charactersAllow to search for a competition name

        """
        return self.conn.request("GET", f"/competitions{self.endpoint(**self.kwargs)}", headers=self.headers)


    def circuits(self):
        """**kwargs ::
               id	integer The id of the circuit
                competitionin integer The id of the competition
                name	string The name of the circuit
                search	string >= 3 characters Allow to search for a circuit name
"""
        return self.conn.request("GET", f"/circuits{self.endpoint(**self.kwargs)}", headers=self.headers)

    def teams(self):
        """ **kwargs ::
            id	integerThe id of the team
            namestringThe name of the team
            search	string >= 3 charactersAllow to search for a team name"""

        return self.conn.request("GET", f"/teams{self.endpoint(**self.kwargs)}", headers=self.headers)

    def drivers(self):
        """ id	integer The id of the driver
            name	string The name of the driver
            search	string >= 3 characters Allow to search for a driver name
"""
        return self.conn.request("GET", f"/drivers{self.endpoint(**self.kwargs)}", headers=self.headers)

    def races(self):
        """ **kwargs ::
        idintegerThe id of the race
        date	string YYYY-MM-DDA valid date
        next	integer <= 2 characters The x next races
        last	integer <= 2 characters The x last races
        competition integer The id of the competition
        season	integer 4 characters The season of the race
        type string The type of the race
        time zone stringA valid timezone
"""
        return self.conn.request("GET", f"/races{self.endpoint(**self.kwargs)}", headers=self.headers)

    def rankings_races(self):
        """ **kwargs :: race
required

integer

The id of the race
team
integer

The id of the team
driver
integer """
        return self.conn.request("GET", f"/rankings/races{self.endpoint(**self.kwargs)}", headers=self.headers)
    def rankings_teams(self):
        """ **kwargs ::
        season
required

string 4 characters

The season
team
integer

The id of the team
"""
        return self.conn.request("GET", f"/rankings/teams{self.endpoint(**self.kwargs)}", headers=self.headers)
    def rankings_drivers(self):
        """ **kwargs ::
        season
required

integer 4 characters

The season
driver
integer

The id of the driver
team
integer

The id of the team
"""
        return self.conn.request("GET", f"/rankings/drivers{self.endpoint(**self.kwargs)}", headers=self.headers)



def fba_sports(sport_api, func):
    return sport_api.get_data(func)


def fba_sport_methods(sport):
    sports_methods = inspect.getmembers(sport, predicate=inspect.ismethod)
    # TODO works only because there is __init__ and no other dunders in Apifb.AFB object
    sports_methods = dict(sports_methods[1:])
    print(sports_methods)


def save_response(name, response):
    name = name+'.txt'
    with open(name, 'w') as x:
        x.write(str(response))


if __name__ == '__main__':
    pass

