# Wordle

Wordle is a classic word guessing game where the player has to guess a 5-letter word within a limited number of attempts. In this implementation of Wordle, the player is prompted to input a 5-letter word and the program provides feedback on the correctness of the guess. The game can be played in the command line interface.

## How to play

1. Clone or download the repository to your local machine.
2. Navigate to the `Games/wordle` directory in your terminal or command prompt.
3. Run the following command to start the game: `python wordle.py`.
4. If you want to specify the word to be guessed, you can provide it as an argument when starting the game: `python wordle.py TESTS`.
5. Enter a 5-letter word as your guess when prompted. If the guess is invalid, you will be prompted again to enter a valid guess.
6. After each guess, the program will provide feedback on the correctness of the guess by highlighting the letters in green or yellow depending on their position in the word. If a letter is not in the word at all, it will be displayed in normal text.
7. The game ends when the player correctly guesses the word or reaches the maximum number of attempts.
8. If the player guesses the word correctly within the allotted attempts, they win the game. If not, they lose and the correct word is revealed.
