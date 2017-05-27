from handlers import ApiHandler


lolHandler = ApiHandler()
lolHandler.championMastery.get_all_champion_mastery(1)
lolHandler.Champion.get_all_champions_by_id(1)
lolHandler.Masteries.get_mastery_pages_for_summoner_id(1)
lolHandler.League.get_challenger_ties_leagues('RU')
lolHandler.LeagueV3.get_challenger_league_for_queue('RANKED_SOLO_5x5')
lolHandler.LoLStatus.get_lol_status_for_shard()
lolHandler.Masteries.get_mastery_pages_for_summoner_id(1)