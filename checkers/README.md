# Checkers

This is a game of checkers created using the Processing Python library. This is a game of checkers that pits a human player playing black against an AI player playing red. The AI uses the minimax algorithm, and the depth can be adjusted to increase or decrease the difficulty. The game board is displayed on the screen, and players take turns moving their pieces diagonally across the board.

## Requirements

- Python 3
- Processing Python Library

## Installation

1. Install Python 3 from the [official website](https://www.python.org/downloads/).
2. Install the Processing Python library by following the instructions on the [Processing website](https://py.processing.org/tutorials/gettingstarted/). 

## How to Play

1. Clone or download the repository.
2. Run the `checkers.pyde` file with Processing. Click the "Run" button in the Processing window.
3. The game will start with a standard checkers board displayed on the screen.
4. Pieces with possible moves will be highlighted when moused over.
5. Click on a piece and drag it to the valid location to make a move.

## Rules

- Each player starts with 12 pieces of their own color.
- Black always moves first and the players take turns moving one piece at a time.
- Pieces move diagonally, one square at a time, in a forward direction.
- If a player's piece reaches the opposite end of the board, it is crowned and can move in any direction.
- If a player's piece is adjacent to an opponent's piece with an empty square on the other side, the player can "jump" over the opponent's piece and remove it from the board.
- If a player can make a jump, they must do so. If they have multiple possible jumps, they can choose which one to take.
- The game ends when one player captures all of the other player's pieces, or when one player is unable to make a legal move. A draw will be declared if 50 moves have passed without a single jump.

## Scoreboard

At the end of a game, no matter how it ended, the player will be prompted for their name. The program will save their name and score in a file called scores.txt. If the user's name already exists in the file, their score will be incremented by 1. The scores file will always remain ranked from highest score to lowest score.

## Adjusting AI Difficulty

To adjust the AI difficulty, modify the depth variable in the minimax_ai.py file. A higher depth will make the AI more difficult to beat, while a lower depth will make it easier.