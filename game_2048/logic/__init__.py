"""Handles the immutable game state and logic."""

import game_2048.models as models
from game_2048.logic.spawning import spawn


def empty_board() -> models.Board:
    return [[0 for _ in range(models.BOARD_WIDTH)] for _ in range(models.BOARD_HEIGHT)]
