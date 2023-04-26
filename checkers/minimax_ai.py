from copy import deepcopy


class MinimaxAI:
    def __init__(self, gm, depth):
        self.gm = gm
        self.depth = depth

    def ai_move(self):
        # Get the best move using the minimax algorithm
        best_move = self.minimax(self.depth, self.gm,
                                 float('-inf'), float('inf'), True)
        # Make the best move, if one is found
        if best_move is not None:
            row, col, row_new, col_new = best_move
            self.gm.move(row, col, row_new, col_new)

    def minimax(self, depth, gm, alpha, beta, max_player):
        # Base case: return the board evaluation
        # if depth is 0 or the game is over
        if depth == 0 or gm.winner is not None:
            return self.evaluate_board(gm)

        # Maximizing player's turn
        if max_player:
            max_eval = float('-inf')
            best_move = None
            for move in self.get_all_moves(gm, gm.turn):
                game_manager_copy = deepcopy(gm)
                game_manager_copy.copy = True
                game_manager_copy.move(*move)
                eval_value = self.minimax(depth - 1, game_manager_copy,
                                          alpha, beta, False)
                # Update max_eval and best_move if a better move is found
                if eval_value > max_eval:
                    max_eval = eval_value
                    best_move = move
                # Update alpha and perform alpha-beta pruning
                alpha = max(alpha, eval_value)
                if beta <= alpha:
                    break
            # Return the best move if at the root of the search tree
            if depth == self.depth:
                return best_move
            return max_eval
        # Minimizing player's turn
        else:
            min_eval = float('inf')
            for move in self.get_all_moves(gm, gm.turn):
                game_manager_copy = deepcopy(gm)
                game_manager_copy.copy = True
                game_manager_copy.move(*move)
                eval_value = self.minimax(depth - 1, game_manager_copy,
                                          alpha, beta, True)
                # Update min_eval
                min_eval = min(min_eval, eval_value)
                # Update beta and perform alpha-beta pruning
                beta = min(beta, eval_value)
                if beta <= alpha:
                    break
            return min_eval

    def get_all_moves(self, gm, player_colour):
        all_moves = []
        # Get legal moves for the given player colour
        legal_moves = gm.board.get_legal_moves(player_colour)
        # Iterate through the legal moves and create tuples for each move
        for piece_pos, moves_pos in legal_moves.items():
            for move_pos in moves_pos:
                all_moves.append((piece_pos[0], piece_pos[1],
                                  move_pos[0], move_pos[1]))
        return all_moves

    def evaluate_board(self, gm):
        score = 0
        # Iterate through the board and update the score based on the pieces
        for row in range(gm.FIELD_SIZE):
            for col in range(gm.FIELD_SIZE):
                piece = gm.board.get_piece(row, col)
                if piece != 0:
                    # Decrease the score for black pieces,
                    # increase it for red ones
                    if piece.colour == gm.BLACK:
                        score -= 1
                    else:
                        score += 1
                    # Add a bonus for kings
                    if piece.is_king:
                        if piece.colour == gm.RED:
                            score += 1
                        else:
                            score -= 1
        return score
