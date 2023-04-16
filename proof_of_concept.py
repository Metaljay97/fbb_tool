from nba_api.stats.library.parameters import LeagueID, Season, SeasonType, StatCategory
from nba_api.stats.endpoints import leaguedashplayerstats

season = "2020-21"  # Replace with the season you're interested in, e.g. '2019-20'
stats = leaguedashplayerstats.LeagueDashPlayerStats(
    season=season,
    season_type_all_star="Regular Season",
    league_id_nullable=LeagueID.default,
    per_mode_detailed="PerGame",
)

data = stats.get_data_frames()[0]  # Get the first (and only) DataFrame
print(data)  # Print the first five rows of the DataFrame

# iterating over rows using iterrows() function
for i, j in data.iterrows():
    print(i, j)
    print()
