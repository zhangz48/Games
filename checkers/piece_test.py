from piece import Piece


def test_constructor():
    row = 1
    col = 0
    colour = (255, 0, 0)
    GRID_SIZE = 80
    piece = Piece(row, col, colour, GRID_SIZE)

    assert piece.row == row
    assert piece.col == col
    assert piece.colour == colour
    assert piece.GRID_SIZE == GRID_SIZE
    assert piece.is_king is False
    assert piece.is_selected is False
    assert piece.jumped is False


def test_be_king():
    row = 1
    col = 0
    colour = (255, 0, 0)
    GRID_SIZE = 80
    piece = Piece(row, col, colour, GRID_SIZE)

    piece.be_king()
    assert piece.is_king is True


def test_select_and_unselect():
    row = 1
    col = 0
    colour = (255, 0, 0)
    GRID_SIZE = 80
    piece = Piece(row, col, colour, GRID_SIZE)

    piece.select()
    assert piece.is_selected is True

    piece.unselect()
    assert piece.is_selected is False


def test_move():
    row = 1
    col = 0
    colour = (255, 0, 0)
    GRID_SIZE = 80
    piece = Piece(row, col, colour, GRID_SIZE)

    new_row = 2
    new_col = 1
    piece.move(new_row, new_col)
    assert piece.row == 2
    assert piece.col == 1
