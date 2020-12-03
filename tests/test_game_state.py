from game_2048.state import *


def test_game_state_default():
    sut = GameState()
    actual = sut.board
    expected = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    assert actual == expected


def test_game_state_init_board():
    board = [[x + y * BOARD_WIDTH for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]
    sut = GameState(board)

    actual = sut.board
    expected = board
    assert actual == expected


def test_spawn_x0_y0():
    sut = GameState()
    actual = sut.spawn(
        get_spawn_location=lambda choices: Point(x=0, y=0),
        get_value=lambda: 2)
    expected = GameState([[2, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]])
    assert actual == expected


def test_spawn_x1_y0():
    sut = GameState()
    actual = sut.spawn(
        get_spawn_location=lambda choices: Point(x=1, y=0),
        get_value=lambda: 2)
    expected = GameState([[0, 0, 0, 0],
                          [2, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]])
    assert actual == expected


def test_spawn_value_4():
    sut = GameState()
    actual = sut.spawn(
        get_spawn_location=lambda choices: Point(x=0, y=0),
        get_value=lambda: 4)
    expected = GameState([[4, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]])
    assert actual == expected


def test_spawn_avoids_filled_spaces():
    sut = GameState([[1, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]])

    def first_index(choices):
        return min(choices, key=lambda choice: choice.x + 4 * choice.y)

    actual = sut.spawn(
        get_spawn_location=first_index,
        get_value=lambda: 2)
    expected = GameState([[1, 0, 0, 0],
                          [2, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]])
    assert actual == expected


def test_spawn_avoids_filled_spaces_2():
    sut = GameState([[1, 1, 1, 1],
                     [1, 1, 1, 1],
                     [1, 1, 0, 1],
                     [1, 1, 1, 1]])

    def first_index(choices):
        return min(choices, key=lambda choice: choice.x + 4 * choice.y)

    actual = sut.spawn(
        get_spawn_location=first_index,
        get_value=lambda: 2)
    expected = GameState([[1, 1, 1, 1],
                          [1, 1, 1, 1],
                          [1, 1, 2, 1],
                          [1, 1, 1, 1]])
    assert actual == expected
