from game_2048 import GameState, BOARD_HEIGHT, BOARD_WIDTH


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


"""
Huzzah



yeah multiply by board width
"""
