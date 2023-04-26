from board import Board


def test_init_board():
    GRID_SIZE = 80
    FIELD_SIZE = 0
    board = Board(GRID_SIZE, FIELD_SIZE)
    assert board.board == []

    GRID_SIZE = 80
    FIELD_SIZE = 2
    board = Board(GRID_SIZE, FIELD_SIZE)
    assert board.board[0][0] == 0
    assert board.board[0][1].row == 0
    assert board.board[0][1].col == 1
    assert board.board[0][1].colour == (234, 51, 35)
    assert board.board[1][0].row == 1
    assert board.board[1][0].col == 0
    assert board.board[1][0].colour == (234, 51, 35)
    assert board.board[1][1] == 0


def test_get_piece():
    GRID_SIZE = 80
    FIELD_SIZE = 8
    board = Board(GRID_SIZE, FIELD_SIZE)

    piece = board.get_piece(0, 0)
    assert piece == 0

    piece = board.get_piece(0, 1)
    assert piece != 0


def test_is_jump():
    GRID_SIZE = 80
    FIELD_SIZE = 8
    board = Board(GRID_SIZE, FIELD_SIZE)

    move_pos = (4, 4)
    piece_pos = (2, 2)
    assert board.is_jump(move_pos, piece_pos) is True

    move_pos = (3, 3)
    piece_pos = (2, 2)
    assert board.is_jump(move_pos, piece_pos) is False


def test_get_piece_moves():
    GRID_SIZE = 80
    FIELD_SIZE = 8
    board = Board(GRID_SIZE, FIELD_SIZE)

    red_piece = board.get_piece(2, 1)
    moves = board.get_piece_moves(red_piece)
    assert moves == [(3, 0), (3, 2)]

    black_piece = board.get_piece(5, 0)
    moves = board.get_piece_moves(black_piece)
    assert moves == [(4, 1)]
