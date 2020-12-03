import pytest

import game_2048.random_spawn


def test_get_spawn_location_returns_only_item_in_set():
    options = {1}
    actual = game_2048.random_spawn.get_spawn_location(options)
    expected = 1
    assert actual == expected


def test_get_spawn_location_returns_something_in_set():
    for _ in range(10):
        options = {1, 2, 3}
        actual = game_2048.random_spawn.get_spawn_location(options)
        assert actual in options


def test_get_spawn_location__when_empty__raise_IndexError():
    options = set()
    with pytest.raises(ValueError):
        game_2048.random_spawn.get_spawn_location(options)


def test_get_value():
    expected = 2
    actual = game_2048.random_spawn.get_value()
    assert actual == expected
