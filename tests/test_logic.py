import game_2048.models as models
import game_2048.logic as logic


def make_test_empty_board():
    return [[0 for _ in range(models.BOARD_WIDTH)] for _ in range(models.BOARD_HEIGHT)]


def test_game_state_default():
    actual = logic.empty_board()
    expected = make_test_empty_board()
    assert actual == expected
