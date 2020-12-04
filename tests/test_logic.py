import game_2048.models as models
import game_2048.logic as logic


def make_test_empty_board():
    return [[0 for _ in range(models.BOARD_WIDTH)] for _ in range(models.BOARD_HEIGHT)]


def test_game_state_default():
    actual = logic.empty_board()
    expected = make_test_empty_board()
    assert actual == expected


def test_spawn_x0_y0():
    actual = logic.spawning.spawn(
        board=make_test_empty_board(),
        get_spawn_location=lambda choices: models.Point(x=0, y=0),
        get_value=lambda: 2)
    expected = [[2, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
    assert actual == expected


def test_spawn_x1_y0():
    actual = logic.spawning.spawn(
        board=make_test_empty_board(),
        get_spawn_location=lambda choices: models.Point(x=1, y=0),
        get_value=lambda: 2)
    expected = [[0, 0, 0, 0],
                [2, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
    assert actual == expected


def test_spawn_value_4():
    actual = logic.spawning.spawn(
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

    actual = logic.spawning.spawn(
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

    actual = logic.spawning.spawn(
        board=board,
        get_spawn_location=first_index,
        get_value=lambda: 2)
    expected = [[1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 2, 1],
                [1, 1, 1, 1]]
    assert actual == expected
