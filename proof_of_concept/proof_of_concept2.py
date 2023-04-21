from nba_api.stats.library.parameters import LeagueID, Season, SeasonType, StatCategory
from nba_api.stats.endpoints import leaguedashplayerstats
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# Define the list of seasons you want to collect data for
seasons = ["2015-16", "2016-17", "2017-18", "2018-19", "2019-20"]
seasonsNum = [1, 2, 3, 4, 5]

# Collect data for each season and append to a list
data_list = []
for season in seasons:
    stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season=season,
        season_type_all_star="Regular Season",
        league_id_nullable=LeagueID.default,
        per_mode_detailed="PerGame",
    )
    data = stats.get_data_frames()[0]
    data_list.append(data)

# Concatenate the data for all seasons into a single DataFrame
data = pd.concat(data_list, ignore_index=True)

# Clean and preprocess the data as necessary
data = data.dropna()  # Remove any NaN values

# Get a player's career averages
player_name = "LeBron James"
player_data = data[data["PLAYER_NAME"] == player_name]
player_data = player_data[["PTS", "REB", "AST", "FT_PCT", "FG_PCT", "BLK", "STL"]]
print(f"Career averages for {player_name}:")
print(player_data)

X = np.array(seasonsNum).reshape((-1, 1))
y = np.array(player_data[["PTS"]]).reshape((-1, 1))
print(y)

print(X)

# Train the model
model = LinearRegression()
model.fit(X, y)


# Make a prediction using the model
prediction = model.predict([[6]])
print(prediction)
