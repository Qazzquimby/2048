import typing as t
import random

from game_2048 import models as models


def _get_spawn_location(empty_spaces: t.Set[models.Point]) -> models.Point:
    return random.sample(empty_spaces, 1)[0]


def _get_value() -> int:
    return 2


def spawn(
        board: models.Board,
        get_spawn_location=_get_spawn_location,
        get_value=_get_value
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
