from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.endpoints import commonallplayers


# Get player ID
player_info = players.find_players_by_full_name("Lebron James")
player_id = player_info[0]["id"]

# Get player game log for given year
game_log = playergamelog.PlayerGameLog(player_id=player_id, season="2022")

# Get player list for given year
player_list = commonallplayers.CommonAllPlayers(
    is_only_current_season=0, season="2022"
).get_data_frames()[0]

# Get player names
player_names = player_list["DISPLAY_FIRST_LAST"].tolist()


# Get game statistics
game_stats = game_log.get_data_frames()[0]
print(game_stats)
print(player_names)
