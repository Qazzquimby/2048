import pytest

import game_2048.models as models
import game_2048.logic.spawning as spawning

from test_logic import make_test_empty_board


def test_spawn_x0_y0():
    actual = spawning.spawn(
        board=make_test_empty_board(),
        get_spawn_location=lambda choices: models.Point(x=0, y=0),
        get_value=lambda: 2)
    expected = [[2, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
    assert actual == expected


def test_spawn_x1_y0():
    actual = spawning.spawn(
        board=make_test_empty_board(),
        get_spawn_location=lambda choices: models.Point(x=1, y=0),
        get_value=lambda: 2)
    expected = [[0, 0, 0, 0],
                [2, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
    assert actual == expected


def test_spawn_value_4():
    actual = spawning.spawn(
        board=make_test_empty_board(),
        get_spawn_location=lambda choices: models.Point(x=0, y=0),
        get_value=lambda: 4)
    expected = [[4, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
    assert actual == expected


def test_spawn_avoids_filled_spaces():
    board = [[1, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

    def first_index(choices):
        return min(choices, key=lambda choice: choice.x + 4 * choice.y)

    actual = spawning.spawn(
        board=board,
        get_spawn_location=first_index,
        get_value=lambda: 2)
    expected = [[1, 0, 0, 0],
                [2, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
    assert actual == expected


def test_spawn_avoids_filled_spaces_2():
    board = [[1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 1, 0, 1],
             [1, 1, 1, 1]]

    def first_index(choices):
        return min(choices, key=lambda choice: choice.x + 4 * choice.y)

    actual = spawning.spawn(
        board=board,
        get_spawn_location=first_index,
        get_value=lambda: 2)
    expected = [[1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 2, 1],
                [1, 1, 1, 1]]
    assert actual == expected


def test_get_spawn_location_returns_only_item_in_set():
    options = {(1, 3)}
    actual = spawning._get_spawn_location(options)
    expected = (1, 3)
    assert actual == expected


def test_get_spawn_location_returns_something_in_set():
    for _ in range(10):
        options = {(1, 2), (2, 3), (3, 4)}
        actual = spawning._get_spawn_location(options)
        assert actual in options


def test_get_spawn_location__when_empty__raise_index_error():
    options = set()
    with pytest.raises(ValueError):
        spawning._get_spawn_location(options)


def test_get_value():
    expected = 2
    actual = spawning._get_value()
    assert actual == expected
