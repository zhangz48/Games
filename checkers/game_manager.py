from board import Board
from minimax_ai import MinimaxAI


class GameManager:
    # Constants
    RED = (234, 51, 35)
    BLACK = (0, 0, 0)

    def __init__(self, GRID_SIZE, FIELD_SIZE):
        self.GRID_SIZE = GRID_SIZE
        self.FIELD_SIZE = FIELD_SIZE
        self.board = Board(GRID_SIZE, FIELD_SIZE)
        self.turn = self.BLACK
        self.draw_counter = 0
        self.winner = None
        self.game_over = False
        self.ai = MinimaxAI(self, 1)
        self.ai_move_countdown = 0
        self.prompt_countdown = 30
        self.copy = False
        if not self.copy:
            print("Black's turn")

    def update(self):
        # If game is not over
        if not self.game_over:

            # Update the drawing
            self.board.display()

            # Find the row and column of the piece under the mouse cursor
            row = mouseY // self.GRID_SIZE
            col = mouseX // self.GRID_SIZE

            # Highlight the piece when moused over
            piece = self.board.get_piece(row, col)
            if (piece != 0 and
                self.BLACK == piece.colour and
               (row, col) in self.board.legal_moves):
                piece.display(True)

            # Checking winning conditions
            self.win()

            # If there's no winner or no draw yet
            if self.winner is None:

                # Set the countdown for the AI move
                if self.turn == self.RED and self.ai_move_countdown == 0:
                    self.ai_move_countdown = 30
                # Countdown for the AI move
                if self.ai_move_countdown > 0:
                    self.ai_move_countdown -= 1
                    # Execute the AI move
                    if self.ai_move_countdown == 0:
                        self.ai_move()

            # If there's a winner or draw
            else:
                self.display_end_game_text()

                # Prompt player to input name
                # Countdown for the player input prompt
                if self.prompt_countdown > 0:
                    self.prompt_countdown -= 1
                    # Execute the player input prompt
                    if self.prompt_countdown == 0:
                        winner_name = self.input('Thanks for playing!\n' +
                                                 'Please enter your name:')
                        if winner_name is not None:
                            self.update_scores(winner_name)
                            self.game_over = True

    def select(self, row, col):
        piece = self.board.get_piece(row, col)

        # if the selected item is a piece of the current player's turn
        if (piece != 0 and piece.colour == self.turn):
            self.board.select_piece(piece)

    def move(self, row, col, row_new, col_new):
        # Get the piece at the given row and col
        piece = self.board.get_piece(row, col)

        # Check if there's a piece in the given position and
        # if it matches the current player's turn
        if (piece != 0 and piece.colour == self.turn):
            # Move the piece to the new position
            piece_moved = self.board.move_piece(piece, row_new, col_new)

            # If the piece has been successfully moved
            if piece_moved is not None:

                if piece_moved.jumped is True:
                    self.draw_counter = 0
                    self.board.get_legal_moves(self.turn, piece_moved)
                    # If there are no more jump moves available,
                    # change the turn
                    if not self.board.jumps_only:
                        self.change_turn()
                else:
                    self.draw_counter += 1
                    self.change_turn()

    def win(self):
        # Check winning conditions
        if self.draw_counter >= 50:
            self.winner = "Draw!"

        self.board.get_legal_moves(self.turn)
        if not self.board.legal_moves:
            if self.turn == self.RED:
                self.winner = "Black Win!"
            else:
                self.winner = "Red Wins!"

    def change_turn(self):
        # Change player's turn
        if self.turn == self.RED:
            self.turn = self.BLACK
            if not self.copy:
                print("Black's turn")
        else:
            self.turn = self.RED
            if not self.copy:
                print("Red's turn")

    def input(self, message=''):
        # Define the input function of our own
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def update_scores(self, winner_name):
        # Save winner's name and score in a file
        scores_file = 'scores.txt'
        scores = []

        try:
            with open(scores_file, 'r') as file:
                for line in file:
                    name, score = line.strip().rsplit(' ', 1)
                    scores.append((name, int(score)))
        except OSError as err:
            return

        # Find the winner in the scores list and
        # increment their score, or add a new entry
        name_found = False
        for i, (name, score) in enumerate(scores):
            if name == winner_name:
                name_found = True
                if self.winner == "Black Win!":
                    scores[i] = (name, score + 1)
                else:
                    scores[i] = (name, score + 0)
                break

        if not name_found:
            if self.winner == "Black Win!":
                scores.append((winner_name, 1))
            else:
                scores.append((winner_name, 0))

        # Sort the scores list from highest to lowest
        scores.sort(key=lambda x: x[1], reverse=True)

        # Write the updated scores back to the file
        with open(scores_file, 'w') as file:
            for name, score in scores:
                file.write("{} {}\n".format(name, score))

    def ai_move(self):
        self.ai.ai_move()

    def display_end_game_text(self):
        fill(255)
        textSize(100)
        textAlign(CENTER)
        text(self.winner, self.GRID_SIZE * self.FIELD_SIZE / 2,
             self.GRID_SIZE * self.FIELD_SIZE / 2)
