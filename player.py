from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.endpoints import commonallplayers


class Player:
    def __init__(self, name):
        self.name = name
        player_info = players.find_players_by_full_name(name)
        self.id = player_info[0]["id"]

    def get_game_log_for_year(self, year):
        # Get player game log for given year
        return playergamelog.PlayerGameLog(player_id=self.id, season=year)
