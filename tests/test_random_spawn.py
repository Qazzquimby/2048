import pytest

import game_2048.logic.spawning as spawning


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
