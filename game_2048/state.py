"""Handles the immutable game state and logic."""

import typing as t

BOARD_WIDTH = 4
BOARD_HEIGHT = 4
Board = t.List[t.List[int]]


class GameState:
    def __init__(self, board: Board = None):
        if board is None:
            board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.board = board

    def spawn(self):
        pass
