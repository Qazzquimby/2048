import typing as t
import random


def get_spawn_location(empty_spaces: t.Set[int]) -> int:
    return random.sample(empty_spaces, 1)[0]


def get_value() -> int:
    return 2
