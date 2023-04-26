from board import Board
from minimax_ai import MinimaxAI
from game_manager import GameManager

GRID_SIZE = 100
FIELD_SIZE = 8


@pytest.fixture
def game_manager():
    return GameManager(GRID_SIZE, FIELD_SIZE)


def test_constructor(game_manager):
    assert isinstance(game_manager.board, Board)
    assert game_manager.turn == GameManager.BLACK
    assert game_manager.draw_counter == 0
    assert game_manager.winner is None
    assert game_manager.game_over is False
    assert isinstance(game_manager.ai, MinimaxAI)
    assert game_manager.ai_move_countdown == 0
    assert game_manager.prompt_countdown == 30
    assert game_manager.copy is False


def test_change_turn(game_manager):
    current_turn = game_manager.turn
    game_manager.change_turn()
    assert game_manager.turn != current_turn


def test_win_draw(game_manager):
    game_manager.draw_counter = 50
    game_manager.win()
    assert game_manager.winner == "Draw!"


def test_select_piece(game_manager):
    game_manager.select(5, 0)
    piece = game_manager.board.get_piece(5, 0)
    assert piece.is_selected
    game_manager.select(2, 1)
    piece = game_manager.board.get_piece(2, 1)
    assert not piece.is_selected
