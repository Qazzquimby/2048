from game_2048 import GameState, BOARD_HEIGHT, BOARD_WIDTH


def test_game_state():
    sut = GameState()
    actual = sut.board
    expected = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    assert actual == expected


"""
test 1 finished. I think we're supposed to commit after every succesful test? I'll do that but I usually dont.
ctrl k



"""
