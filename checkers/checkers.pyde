from game_manager import GameManager

GRID_SIZE = 90  # set the size of each square on the board
FIELD_SIZE = 8  # set the size of the game board

# create a new game manager object
gm = GameManager(GRID_SIZE, FIELD_SIZE)


def setup():
    loadImage("crown.png")

    # set the size of the display window based on the size of the game board
    size(GRID_SIZE * FIELD_SIZE,
         GRID_SIZE * FIELD_SIZE)


def draw():
    # update the drawing
    gm.update()


def mousePressed():
    global row
    global col

    # the row and column of the current mouse position
    row = mouseY // GRID_SIZE
    col = mouseX // GRID_SIZE

    # select the piece at the current position
    gm.select(row, col)


def mouseReleased():
    # get the row and column of the new mouse position
    row_new = mouseY // GRID_SIZE
    col_new = mouseX // GRID_SIZE

    # move the selected piece to the new position
    gm.move(row, col, row_new, col_new)
