class Piece:
    def __init__(self, row, col, colour, GRID_SIZE):
        self.row = row
        self.col = col
        self.colour = colour
        self.GRID_SIZE = GRID_SIZE
        self.is_king = False
        self.is_selected = False
        self.jumped = False

    def be_king(self):
        self.is_king = True

    def select(self):
        self.is_selected = True

    def unselect(self):
        self.is_selected = False

    def move(self, row, col):
        # Update row and column coordinates
        self.row = row
        self.col = col

    def display(self, highlight=False):
        STROKE_COLOR = (255, 255, 255)
        STROKE_WEIGHT = 2
        OUTER_DIAMETER = 0.9 * self.GRID_SIZE
        INNER_DIAMETER = 0.7 * self.GRID_SIZE

        # If the piece is not selected
        # the center of the circle is the center of the grid
        if not self.is_selected:
            x = self.GRID_SIZE * self.col + self.GRID_SIZE / 2
            y = self.GRID_SIZE * self.row + self.GRID_SIZE / 2

        # If the piece is selected
        # the center of the circle is the mouse cursor
        else:
            x = mouseX
            y = mouseY

        # Draw two circles
        stroke(*STROKE_COLOR)

        # If the piece is highlighted or
        # is selected, make it highlighted
        if highlight or self.is_selected:
            strokeWeight(STROKE_WEIGHT * 2)
        else:
            strokeWeight(STROKE_WEIGHT)

        fill(*self.colour)
        circle(x, y, OUTER_DIAMETER)
        strokeWeight(STROKE_WEIGHT)
        circle(x, y, INNER_DIAMETER)

        if self.is_king:
            # Draw the crown shape (cross shape)
            img = loadImage("crown.png")
            imageMode(CENTER)
            image(img, x, y, 0.6 * self.GRID_SIZE, 0.6 * self.GRID_SIZE)
