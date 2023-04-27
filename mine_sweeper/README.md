# Minesweeper

Minesweeper is a classic single-player game in which the player tries to clear a minefield without detonating a mine.

## Requirements

- Python 3
- Processing Python Library

## Installation

1. Install Python 3 from the [official website](https://www.python.org/downloads/).
2. Install the Processing Python library by following the instructions on the [Processing website](https://py.processing.org/tutorials/gettingstarted/). 

## How to play

1. Clone or download the repository.
2. Run the `mine_sweeper.pyde` file with Processing. Click the "Run" button in the Processing window.
3. The game will start and a minefield will appear. The field is a square grid of cells. Some cells contain mines and some cells are safe to click.
4. The game is played by clicking on cells in the minefield. If a mine is clicked, the game is over and the player loses. If a safe cell is clicked, the cell will be revealed, and the player will see a number indicating how many mines are adjacent to that cell.
5. The player wins the game by revealing all safe cells without detonating any mines.

## How to customize the game

You can change the size of the minefield by changing the value of the `FIELD_SIZE` constant in the `Minefield` class. You can also change the number of mines in the minefield by changing the value of the `NUMBER_OF_MINES` constant in the `GameController` class.