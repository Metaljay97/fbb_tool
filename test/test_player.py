import unittest
import fbb_tool
from fbb_tool.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Test Player", 10, 5, 3, 1, 1, 1, 0.5, 0.8)

    def test_player_name(self):
        self.assertEqual(self.player.name, "Test Player")

    def test_player_points(self):
        self.assertEqual(self.player.points, 10)

    def test_player_rebounds(self):
        self.assertEqual(self.player.rebounds, 5)

    def test_player_assists(self):
        self.assertEqual(self.player.assists, 3)

    def test_player_steals(self):
        self.assertEqual(self.player.steals, 1)

    def test_player_blocks(self):
        self.assertEqual(self.player.blocks, 1)

    def test_player_three_pointers(self):
        self.assertEqual(self.player.three_pointers, 1)

    def test_player_field_goal_percentage(self):
        self.assertEqual(self.player.field_goal_percentage, 0.5)

    def test_player_free_throw_percentage(self):
        self.assertEqual(self.player.free_throw_percentage, 0.8)


if __name__ == "__main__":
    unittest.main()
