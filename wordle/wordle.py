import sys
import random

# G and Y represent text formatting codes for green and
# yellow text output. Variable names are brief so as to
# be unobtrusive when interspersed with text
G = '\x1b[0;30;42m'  # green text
Y = '\x1b[0;30;43m'  # yellow text
N = '\x1b[0m'        # normal text/no highlighting

ALLOWED_GUESSES = 6
WORD_LENGTH = 5


def main(args):
    # If there is an argument, set that argument to be the word.
    # Otherwise, the word should be randomly selected from valid
    # letters of WORD_LENGTH in the Scrabble words file. (Use a
    # separate function to get the valid words from the
    # Scrabble words files)
    valid_words = get_valid_words(WORD_LENGTH)

    if args:
        wordle = str(args).upper()
    else:
        wordle = str(random.choice(valid_words)).upper()

    # Study the following string to underestand how G, Y and N
    # behave for colored text highlights
    print("-------------------------------------")
    print(f"Welcome to {Y}PY{G}WOR{Y}D{G}LE{N}!")
    print("-------------------------------------")
    print("Try to guess the secret word in", ALLOWED_GUESSES, "tries or less.")
    print("When you make a guess, the letters will be highlighted in the following colors:")
    print("  -", G, "Green:", N, "Letters that are in the correct position")
    print("  -", Y, "Yellow:", N, "Letters that are in the word, but not in the correct position")
    print("  -", N, "Normal:", N, "Letters that are not in the word at all")
    print("-------------------------------------")

    # Create a list to collect failed guesses. You can use
    # this list to print the guesses each time, and also use
    # the list's length to keep track of how many guesses have
    # been made
    guesses = []
    new_guess = str()

    # Use a while loop to continue as long
    # as the user's answer is not correct and the guesses are
    # fewer than the allowed number of guesses.
    while new_guess != wordle and len(guesses) < ALLOWED_GUESSES:
        new_guess = input("Enter your guess (5 letters):\n").upper()

        # Use another while loop to repeat the prompt
        # in case of invalid guesses
        while new_guess not in valid_words or len(new_guess) != WORD_LENGTH:
            new_guess = input("Please enter a valid 5-letter word: \n").upper()

        # Use a separate function, format_guess, to format
        # the guess with green and yellow highlighting for printing out.
        # That's where you'll compare it to the correct word.
        coloured_new_guess = format_guess(new_guess, wordle)

        # Print out the list of guesses so far with each new guess
        guesses.append(coloured_new_guess)
        for guess in guesses:
            print(f"                 {guess}")

    # Print an appropriate message when the game ends
    if new_guess == wordle:
        print(f"Congrats! You got it in {len(guesses)} tries")
    else:
        print(f"Sorry, the word was {wordle}")


def format_guess(guess, wordle):  # Add necessary parameters

    # Implement this function so that it returns
    # the guess string highlighted with green and yellow based
    # on comparing letters with the original word.

    # See assignment instructions for specifics about how
    # letters should be highlighted
    coloured_guess = str()
    for i in range(len(guess)):
        # Any characters shared by the guessed word and the secret word
        # in the correct positions will be highlighted in green
        if guess[i] == wordle[i]:
            coloured_guess = coloured_guess + G + guess[i]
        # Any characters shared by the guessed word and the secret word
        # but not in the correct positions will be yellow
        elif guess[i] in wordle:
            coloured_guess = coloured_guess + Y + guess[i]
        # Characters that are not shared at all between the words will
        # show up in white on black
        else:
            coloured_guess = coloured_guess + N + guess[i]
    # Rest colours and text effects at the end of the word
    coloured_guess = coloured_guess + N
    return coloured_guess


def get_valid_words(word_length):  # Add necessary parameters

    # Implement this function so that it returns
    # a list of words consisting of only words of the
    # correct length from the Scrabble word list
    scrabble_words = open("Collins Scrabble Words (2019).txt", "r")
    valid_words = []
    for word in scrabble_words:
        if len(word.rstrip()) == word_length:
            valid_words.append(word.rstrip())
    return valid_words


# Check for the length of sys.argv array so that the
# optional argument in the command line can be treated properly
if len(sys.argv) == 2:
    main(sys.argv[1])
if len(sys.argv) == 1:
    main(None)
