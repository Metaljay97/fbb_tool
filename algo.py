# Define the categories and their weights
categories = {
    "points": 0,
    "rebounds": 0,
    "assists": 0,
    "steals": 0,
    "blocks": 0,
    "3-pointers": 0,
    "field goal percentage": 0,
    "free throw percentage": 0,
}


# Define a function to calculate the average stat line of the first n players in a list of players
def calculate_average_stats(players, n):
    stats = {category: 0 for category in categories}
    for i in range(n):
        for category in categories:
            stats[category] += players[i][category]
    for category in categories:
        stats[category] /= n
    return stats


def calculate_score(player):
    score = 0
    for category, weight in categories.items():
        if player[category] >= (sum(p[category] for p in players) / len(players)):
            score += weight
    return score


# Create a list of players with their predicted season averages
players = [
    {
        "name": "Player A",
        "points": 20,
        "rebounds": 8,
        "assists": 5,
        "steals": 1,
        "blocks": 1,
        "3-pointers": 2,
        "field goal percentage": 0.5,
        "free throw percentage": 0.8,
    },
    {
        "name": "Player B",
        "points": 18,
        "rebounds": 6,
        "assists": 7,
        "steals": 2,
        "blocks": 1,
        "3-pointers": 1,
        "field goal percentage": 0.45,
        "free throw percentage": 0.9,
    },
    {
        "name": "Player C",
        "points": 22,
        "rebounds": 10,
        "assists": 3,
        "steals": 0,
        "blocks": 3,
        "3-pointers": 0,
        "field goal percentage": 0.6,
        "free throw percentage": 0.85,
    },
    {
        "name": "Player D",
        "points": 16,
        "rebounds": 4,
        "assists": 5,
        "steals": 1,
        "blocks": 0,
        "3-pointers": 3,
        "field goal percentage": 0.4,
        "free throw percentage": 0.8,
    },
    {
        "name": "Player E",
        "points": 15,
        "rebounds": 6,
        "assists": 4,
        "steals": 2,
        "blocks": 1,
        "3-pointers": 2,
        "field goal percentage": 0.5,
        "free throw percentage": 0.75,
    },
    {
        "name": "Player F",
        "points": 17,
        "rebounds": 5,
        "assists": 8,
        "steals": 0,
        "blocks": 0,
        "3-pointers": 1,
        "field goal percentage": 0.47,
        "free throw percentage": 0.9,
    },
    {
        "name": "Player G",
        "points": 14,
        "rebounds": 9,
        "assists": 2,
        "steals": 2,
        "blocks": 2,
        "3-pointers": 0,
        "field goal percentage": 0.52,
        "free throw percentage": 0.75,
    },
    {
        "name": "Player H",
        "points": 19,
        "rebounds": 7,
        "assists": 4,
        "steals": 1,
        "blocks": 0,
        "3-pointers": 2,
        "field goal percentage": 0.43,
        "free throw percentage": 0.85,
    },
    {
        "name": "Player I",
        "points": 13,
        "rebounds": 4,
        "assists": 3,
        "steals": 3,
        "blocks": 0,
        "3-pointers": 3,
        "field goal percentage": 0.38,
        "free throw percentage": 0.8,
    },
    {
        "name": "Player J",
        "points": 12,
        "rebounds": 3,
        "assists": 6,
        "steals": 2,
        "blocks": 1,
        "3-pointers": 1,
        "field goal percentage": 0.44,
        "free throw percentage": 0.7,
    },
    {
        "name": "Player K",
        "points": 21,
        "rebounds": 8,
        "assists": 1,
        "steals": 0,
        "blocks": 1,
        "3-pointers": 2,
        "field goal percentage": 0.43,
        "free throw percentage": 0.7,
    },
]
# Calculate the average stat line of the first 3 players for each category
average_stats = calculate_average_stats(players, 5)

# Select the first 3 players using the best player available method
selected_players = []
for i in range(3):
    best_player = max(players, key=lambda player: player["points"])
    selected_players.append(best_player)
    players.remove(best_player)

# Calculate the weight of each category based on how much better the top player in that category is compared to the average
for category in categories:
    top_stats = calculate_average_stats(selected_players, 3)
    if top_stats[category] > average_stats[category]:
        categories[category] = top_stats[category] - average_stats[category]

# Sort the players by their score and select the top n players
n = 15  # You can change this value based on the
top_players = sorted(players, key=lambda player: calculate_score(player), reverse=True)[
    :n
]

print(categories)

# Print the names of the top players
print("Selected players:")
for player in selected_players:
    print(player["name"])


print("Top Players:")
for player in top_players:
    print(player["name"])
