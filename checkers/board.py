from piece import Piece


class Board:
    # Constants
    LIGHT_BROWN = (219, 192, 158)
    DARK_BROWN = (109, 71, 27)
    RED = (234, 51, 35)
    BLACK = (0, 0, 0)

    def __init__(self, GRID_SIZE, FIELD_SIZE):
        self.GRID_SIZE = GRID_SIZE
        self.FIELD_SIZE = FIELD_SIZE
        self.board = [
            [0 for _ in range(FIELD_SIZE)] for _ in range(FIELD_SIZE)
                      ]
        self.legal_moves = {}
        self.jumps_only = {}
        self.create_pieces()

    def get_piece(self, row, col):
        # Get the item on the board given row and col
        return self.board[row][col]

    def create_pieces(self):
        # Initial the board with pieces
        for row in range(self.FIELD_SIZE):
            for col in range(self.FIELD_SIZE):
                if (row + col) % 2 == 1:
                    if row < 3:
                        self.board[row][col] = Piece(
                            row, col, self.RED, self.GRID_SIZE
                            )
                    elif row > 4:
                        self.board[row][col] = Piece(
                            row, col, self.BLACK, self.GRID_SIZE
                            )

        # Get the dict of all legal moves for the inital setup
        self.get_legal_moves(self.BLACK)

    def select_piece(self, piece):
        # If the piece is movable, set it to be selected
        if (piece.row, piece.col) in self.legal_moves:
            piece.select()

    def move_piece(self, piece, row, col):
        # Move the piece to a new position
        # Firstly, set it to be unselected
        piece.unselect()

        # If this position is within the set of its all movable positions
        if (piece.row, piece.col) in self.legal_moves:
            if (row, col) in self.legal_moves[(piece.row, piece.col)]:

                # Swap the piece and 0 in the 2-D board list
                self.board[piece.row][piece.col], self.board[row][col] = (
                    self.board[row][col], self.board[piece.row][piece.col]
                    )

                # Check if the move is a jump
                move_pos = (row, col)
                piece_pos = (piece.row, piece.col)
                if self.is_jump(move_pos, piece_pos):
                    # Remove the jumped piece from the board
                    row_middle = (row + piece.row) // 2
                    col_middle = (col + piece.col) // 2
                    self.board[row_middle][col_middle] = 0
                    piece.jumped = True
                else:
                    piece.jumped = False

                # Update the row and col attributes of the piece
                piece.move(row, col)

                # Check if the piece reaches the edge
                # If yes, make it king
                if ((row == 0 and piece.colour == self.BLACK)
                    or
                   (row == self.FIELD_SIZE - 1 and piece.colour == self.RED)):
                    piece.be_king()
            else:
                return None
        else:
            return None

        return piece

    def get_legal_moves(self, player_colour, piece_jumped=None):
        # Initialize an empty dictionary to store legal moves
        legal_moves = {}

        # Iterate through all the board positions
        for row in range(self.FIELD_SIZE):
            for col in range(self.FIELD_SIZE):
                piece = self.get_piece(row, col)

                # If the current position contains a piece
                # of the player's colour
                if piece != 0 and piece.colour == player_colour:
                    # Get the legal moves for the current piece
                    moves = self.get_piece_moves(piece)
                    # If there are any legal moves, add them to the dictionary
                    if moves:
                        legal_moves[(row, col)] = moves

        # Initialize an empty dictionary to store jump moves only
        jumps_only = {}

        # If a piece has just made a jump
        if piece_jumped is not None:
            piece_pos = (piece_jumped.row, piece_jumped.col)
            if piece_pos in legal_moves:
                moves_pos = legal_moves[piece_pos]

                # Filter out non-jump moves
                jumps = [move_pos for move_pos in moves_pos
                         if self.is_jump(move_pos, piece_pos)]

                # If there are any jump moves,
                # add them to the jumps_only dictionary
                if jumps:
                    jumps_only[piece_pos] = jumps
        else:
            # If no piece has just made a jump, check all pieces for jump moves
            for piece_pos, moves_pos in legal_moves.items():
                jumps = [move_pos for move_pos in moves_pos
                         if self.is_jump(move_pos, piece_pos)]

                # If there are any jump moves,
                # add them to the jumps_only dictionary
                if jumps:
                    jumps_only[piece_pos] = jumps

        # Update the jumps_only attribute
        self.jumps_only = jumps_only

        # If there are any jump moves, prioritize them
        if jumps_only:
            self.legal_moves = jumps_only
        else:
            self.legal_moves = legal_moves

        return self.legal_moves

    def is_jump(self, move_pos, piece_pos):
        row_diff = abs(move_pos[0] - piece_pos[0])
        col_diff = abs(move_pos[1] - piece_pos[1])
        if row_diff == 2 and col_diff == 2:
            return True
        else:
            return False

    def get_piece_moves(self, piece):
        valid_moves = []
        valid_jumps = []

        # Generate all possible move directions
        if piece.is_king:
            row_range = [-1, 1]
        else:
            if piece.colour == self.RED:
                row_range = [1]
            else:
                row_range = [-1]
        col_range = [-1, 1]

        for row_dir in row_range:
            for col_dir in col_range:
                row_new = piece.row + row_dir
                col_new = piece.col + col_dir

                # Check if the destination cell is within the board
                if (0 <= row_new < self.FIELD_SIZE and
                   0 <= col_new < self.FIELD_SIZE):
                    # Check if the destination cell is empty
                    if self.board[row_new][col_new] == 0:
                        valid_moves.append((row_new, col_new))

                jump_row_new = piece.row + 2 * row_dir
                jump_col_new = piece.col + 2 * col_dir

                # Check if the destination cell is within the board
                if (0 <= jump_row_new < self.FIELD_SIZE and
                   0 <= jump_col_new < self.FIELD_SIZE):
                    # Check if the destination cell is empty
                    if self.board[jump_row_new][jump_col_new] == 0:
                        # Get the coordinates of the piece being jumped over
                        row_middle = (jump_row_new + piece.row) // 2
                        col_middle = (jump_col_new + piece.col) // 2
                        middle_piece = self.board[row_middle][col_middle]

                        # Check if the jumped piece is an opponent's piece
                        if (middle_piece != 0 and
                           middle_piece.colour != piece.colour):
                            valid_jumps.append((jump_row_new, jump_col_new))

        moves = valid_jumps + valid_moves
        return moves

    def loop_through_board(self, fn):
        """
        loops through mine field and carries
        out passed function with x and y arguments
        """
        # This will save some reduplication of code in the
        # following methods
        for x in range(self.FIELD_SIZE):
            for y in range(self.FIELD_SIZE):
                fn(x, y)

    def display_grid(self, x, y):
        # Draw a single grid
        noStroke()

        # Fill different colour according to grid's position
        if (x + y) % 2 != 0:
            fill(*self.DARK_BROWN)
        else:
            fill(*self.LIGHT_BROWN)
        square(x * self.GRID_SIZE, y * self.GRID_SIZE, self.GRID_SIZE)

    def display_piece(self):
        # Draw all the pieces
        self.loop_through_board(
            lambda x, y: self.board[x][y].display() if self.board[x][y] != 0
            else None
            )

    def display(self):
        # Draw all grids first and then pieces
        self.loop_through_board(
            lambda x, y: self.display_grid(x, y)
            )
        self.display_piece()
