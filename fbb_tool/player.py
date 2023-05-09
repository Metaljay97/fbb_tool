class Player:
    def __init__(
        self,
        name,
        points,
        rebounds,
        assists,
        steals,
        blocks,
        three_pointers,
        field_goal_percentage,
        free_throw_percentage,
    ):
        self.name = name
        self.points = points
        self.rebounds = rebounds
        self.assists = assists
        self.steals = steals
        self.blocks = blocks
        self.three_pointers = three_pointers
        self.field_goal_percentage = field_goal_percentage
        self.free_throw_percentage = free_throw_percentage

    def __str__(self):
        return f"{self.name} (PTS: {self.points}, REB: {self.rebounds}, AST: {self.assists}, STL: {self.steals}, BLK: {self.blocks}, 3PT: {self.three_pointers}, FG%: {self.field_goal_percentage}, FT%: {self.free_throw_percentage})"
