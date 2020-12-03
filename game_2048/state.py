"""Handles the immutable game state and logic."""
import collections
import typing as t
from game_2048 import random_spawn

BOARD_WIDTH = 4
BOARD_HEIGHT = 4
Board = t.List[t.List[int]]

Point = collections.namedtuple('Point', ['x', 'y'])


class GameState:
    def __init__(self, board: Board = None):
        if board is None:
            board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.board = board

    def spawn(
            self,
            get_spawn_location=random_spawn.get_spawn_location,
            get_value=random_spawn.get_value
    ) -> "GameState":
        board = self.board.copy()

        choices = set([Point(x=x, y=y)
                       for x in range(BOARD_WIDTH)
                       for y in range(BOARD_HEIGHT)
                       if board[x][y] == 0])
        spawn_location = get_spawn_location(choices)
        board[spawn_location.x][spawn_location.y] = get_value()
        return GameState(board)

    def __eq__(self, other):
        return isinstance(other, GameState) and self.board == other.board
