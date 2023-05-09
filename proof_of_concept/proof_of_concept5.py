from nba_api.stats.library.parameters import LeagueID, Season, SeasonType, StatCategory
from nba_api.stats.endpoints import leaguedashplayerstats
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# Define the list of seasons you want to collect data for
season = "2022-23"

# Collect data for each season and append to a list
stats = leaguedashplayerstats.LeagueDashPlayerStats(
    season=season,
    season_type_all_star="Regular Season",
    league_id_nullable=LeagueID.default,
    per_mode_detailed="PerGame",
)

data = stats.get_data_frames()[0]

# Clean and preprocess the data as necessary
data = data.dropna()  # Remove any NaN values

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
print(data)


# Extract relevant player statistics from the game logs
player_stats = []

for index, row in data.iterrows():
    print(row)
    player_id = row["PLAYER_ID"]
    player_name = row["PLAYER_NAME"]

    score = (
        row["PTS"]
        + row["REB"]
        + row["AST"]
        + row["BLK"]
        + row["STL"]
        + row["FG3M"]
        - (row["FGA"] - row["FGM"])
        - (row["FTA"] - row["FTM"])
    )
    score = score * row["GP"]

    player_stats.append({"name": player_name, "score": score})
    # Define a list of dictionaries representing NBA players


# Sort the players list by points (in descending order)
sorted_players = sorted(player_stats, key=lambda p: p["score"], reverse=True)


# Print the sorted list
for player in sorted_players:
    print(player["name"], player["score"])
