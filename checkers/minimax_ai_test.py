from game_manager import GameManager
from minimax_ai import MinimaxAI

GRID_SIZE = 100
FIELD_SIZE = 8


@pytest.fixture
def game_manager():
    return GameManager(GRID_SIZE, FIELD_SIZE)


@pytest.fixture
def minimax_ai(game_manager):
    return MinimaxAI(game_manager, 2)


def test_constructor(minimax_ai, game_manager):
    assert minimax_ai.gm == game_manager
    assert minimax_ai.depth == 2


def test_evaluate_board(minimax_ai, game_manager):
    # Move two black pieces and one red piece on the board
    game_manager.move(5, 0, 4, 1)  # Move black piece
    game_manager.move(2, 5, 3, 4)  # Move red piece
    game_manager.move(5, 5, 4, 4)  # Move black piece
    score = minimax_ai.evaluate_board(game_manager)
    assert score == 0


def test_get_all_moves(minimax_ai, game_manager):
    # Get all moves for the black player
    moves = minimax_ai.get_all_moves(game_manager, GameManager.RED)
    expected_moves = [
        (2, 1, 3, 0), (2, 1, 3, 2), (2, 3, 3, 2), (2, 3, 3, 4),
        (2, 5, 3, 4), (2, 5, 3, 6), (2, 7, 3, 6)
    ]
    assert set(moves) == set(expected_moves)
