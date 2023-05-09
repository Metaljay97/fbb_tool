from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll

# Get a list of all NBA players
n_players = 40
player_list = players.get_players()
players = player_list[:n_players]

# Get game logs for each player in the current season
player_logs = []
for player in players:
    print(player)
    player_id = player["id"]
    game_log = playergamelog.PlayerGameLog(
        player_id=player_id, season="2022"
    ).get_data_frames()[0]
    player_logs.append(game_log)

# Extract relevant player statistics from the game logs
player_stats = {}
for game_log in player_logs:
    for index, row in game_log.iterrows():
        print(row)
        print(index)
        # player_id = row["PLAYER_ID"]
        player_name = row["PLAYER_NAME"]
        # points = row["PTS"]
        # rebounds = row["REB"]
        # assists = row["AST"]
        score = (
            row["PTS"] + row["REB"] + row["AST"] + row["BLK"] + row["STL"] + row["FG3M"]
        )

        print(player_name)
        print(score)

        player_stats[player_id] = {
            "name": player_name,
            "points": points,
            "rebounds": rebounds,
            "assists": assists,
            "score": score,
        }
