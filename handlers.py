import requests
from creds import apikey

class ApiHandler(object):
    api_key = apikey
    payload = {'api_key': api_key}
    endpoint = 'https://ru.api.riotgames.com/'
    game = 'lol/'

    def __init__(self):
        assert isinstance(apikey, str)
        self.championMastery = ChampionMastery()
        self.Champion = Champion()
        self.League = League()
        self.LeagueV3 = LeagueV3()
        self.LoLStatus = LoLStatus()
        self.Masteries = Masteries()


class ChampionMastery(ApiHandler):
    method_endpoint = 'champion-mastery/v3/'

    def __init__(self):
        super(ApiHandler)
        self.method_ref = '{ep}{gm}{mep}'.format(ep=self.endpoint, gm=self.game, mep=self.method_endpoint)


    def get_all_champion_mastery(self, summoner_id):
        """Get all champion mastery entries sorted by number of champion points descending."""
        url = self.method_ref + 'champion-masteries/by-summoner/{summonerId}'
        r = requests.get(url.format(summonerId=summoner_id), params=self.payload)
        return r.json()

    def get_champion_mastery_by_id(self, summoner_id, champion_id):
        """Get a champion mastery by player ID and champion ID."""
        url = self.method_ref + 'champion-masteries/by-summoner/{summonerId}/by-champion/{championId}'
        r = requests.get(url.format(summonerId=summoner_id, championId=champion_id), params=self.payload)
        return r.json()

    def get_players_champion_mastery_score(self, summoner_id):
        """Get a player's total champion mastery score, which is the sum of individual champion mastery levels."""
        url = self.method_ref + 'scores/by-summoner/{summonerId}'
        r = requests.get(url.format(summonerId=summoner_id), params=self.payload)
        return r.json()

class Champion(ApiHandler):
    method_endpoint = 'platform/v3/'

    def __init__(self):
        super(ApiHandler)
        self.method_ref = '{ep}{gm}{mep}'.format(ep=self.endpoint, gm=self.game, mep=self.method_endpoint)

    def get_all_champions(self):
        """Retrieve all champions."""
        url = self.method_ref + 'champions'
        r = requests.get(url, params=self.payload)
        return r.json()

    def get_all_champions_by_id(self, champion_id):
        """Retrieve champion by ID."""
        url = self.method_ref + 'champions/{id}'
        r = requests.get(url.format(id=champion_id), params=self.payload)
        return r.json()

class League(ApiHandler):
    method_endpoint = '{region}/v2.5/league/'

    def __init__(self):
        super(ApiHandler)
        self.method_ref = '{ep}{gm}{mep}'.format(ep=self.endpoint, gm=self.game, mep=self.method_endpoint)

    def get_leagues_by_summoner_id(self, summoner_id, region):
        """Get leagues mapped by summoner ID for a given list of summoner IDs. (REST)."""
        url = self.method_ref + 'by-summoner/{summonerIds}'
        r = requests.get(url.format(summonerId=summoner_id, region=region), params=self.payload)
        return r.json()

    def get_league_entries_by_summoner_id(self, summoner_id, region):
        """Get league entries mapped by summoner ID for a given list of summoner IDs. (REST)."""
        url = self.method_ref + '{summonerIds}/entry'
        r = requests.get(url.format(summonerId=summoner_id, region=region), params=self.payload)
        return r.json()

    def get_challenger_ties_leagues(self, region):
        """Get challenger tier leagues. (REST)."""
        url = self.method_ref + 'challenger'
        r = requests.get(url.format(region=region), params=self.payload)
        return r.json()


    def get_master_ties_leagues(self, region):
        """Get master tier leagues. (REST)."""
        url = self.method_ref + 'master'
        r = requests.get(url.format(region=region), params=self.payload)
        return r.json()

class LeagueV3(ApiHandler):
    method_endpoint = 'league/v3/'

    def __init__(self):
        super(ApiHandler)
        self.method_ref = '{ep}{gm}{mep}'.format(ep=self.endpoint, gm=self.game, mep=self.method_endpoint)

    def get_challenger_league_for_queue(self, queue):
        """Get the challenger league for a given queue."""
        url = self.method_ref + 'challengerleagues/by-queue/{queue}'
        r = requests.get(url.format(queue=queue), params=self.payload)
        return r.json()

    def get_leagues_for_summoner_id(self, summoner_id):
        """Get leagues in all queues for a given summoner ID."""
        url = self.method_ref + 'leagues/by-summoner/{summonerId}'
        r = requests.get(url.format(summonerId=summoner_id), params=self.payload)
        return r.json()

    def get_master_league_for_queue(self, queue):
        """Get the master league for a given queue."""
        url = self.method_ref + 'masterleagues/by-queue/{queue}'
        r = requests.get(url.format(queue=queue), params=self.payload)
        return r.json()


    def get_league_positions_for_summoner_id(self, summoner_id):
        """Get league positions in all queues for a given summoner ID."""
        url = self.method_ref + 'positions/by-summoner/{summonerId}'
        r = requests.get(url.format(summonerId=summoner_id), params=self.payload)
        return r.json()

class LoLStatus(ApiHandler):
    method_endpoint = 'status/v3/'

    def __init__(self):
        super(ApiHandler)
        self.method_ref = '{ep}{gm}{mep}'.format(ep=self.endpoint, gm=self.game, mep=self.method_endpoint)

    def get_lol_status_for_shard(self):
        """Get League of Legends status for the given shard."""
        url = self.method_ref + 'shard-data'
        r = requests.get(url, params=self.payload)
        return r.json()

class Masteries(ApiHandler):
    method_endpoint = 'platform/v3/masteries/'

    def __init__(self):
        super(ApiHandler)
        self.method_ref = '{ep}{gm}{mep}'.format(ep=self.endpoint, gm=self.game, mep=self.method_endpoint)

    def get_mastery_pages_for_summoner_id(self, summoner_id):
        """Get mastery pages for a given summoner ID."""
        url = self.method_ref + 'by-summoner/{summonerId}'
        r = requests.get(url.format(summonerId=summoner_id), params=self.payload)
        return r.json()


#TODO MATCH-V3
#TODO RUNES-V3
#TODO SPECTATOR-V3
#TODO STATIC-DATA-V3
#TODO SUMMONER-V3
#TODO TOURNAMENT-STUB-V3
#TODO TOURNAMENT-V3
#TODO ERROR HANDLER

# 400	Bad request
# 401	Unauthorized
# 403	Forbidden
# 404	Data not found
# 405	Method not allowed
# 415	Unsupported media type
# 429	Rate limit exceeded
# 500	Internal server error
# 502	Bad gateway
# 503	Service unavailable
# 504	Gateway timeout