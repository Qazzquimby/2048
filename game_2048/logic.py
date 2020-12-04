"""Handles the immutable game state and logic."""
import typing as t

import game_2048.models as models
from game_2048 import random_spawn


def empty_board() -> models.Board:
    return [[0 for _ in range(models.BOARD_WIDTH)] for _ in range(models.BOARD_HEIGHT)]


def spawn(
        board: models.Board,
        get_spawn_location=random_spawn.get_spawn_location,
        get_value=random_spawn.get_value
) -> models.Board:
    board = board.copy()

    choices = _get_empty_spaces(board)
    spawn_location = get_spawn_location(choices)
    board[spawn_location.x][spawn_location.y] = get_value()
    return board


def _get_empty_spaces(board: models.Board) -> t.Set[models.Point]:
    empty_spaces = set([models.Point(x=x, y=y)
                        for x in range(models.BOARD_WIDTH)
                        for y in range(models.BOARD_HEIGHT)
                        if board[x][y] == 0])
    return empty_spaces
