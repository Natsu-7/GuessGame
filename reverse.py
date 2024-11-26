'''
Title : Reverse Guess the Number Game
Author : Chaitanya Shah
Class : CYSE1002
Date : 25th November 2024

Description :
In this version of the game, the player selects a number between 1 and 100,
and the computer guesses the number.
The player provides hints ('higher', 'lower', or 'correct') to guide the
computer's guesses.
The computer follows the binary search algorithm to guess the correct number.
The game allows for multiple runs.
'''


# I have used strip() to cut out out the spaces in user inputs from either side.


def get_player_hint():
    """
    Description :
    This function takes a hint from the player and validates it.
    The valid inputs are 'higher', 'lower', or 'correct'.
    :return:
    A valid hint as a string
    """
    while True:
        try:
            hint = (input("Enter your hint ('higher', 'lower', 'correct'): ")
                    .strip().lower())
            if hint in {'higher', 'lower', 'correct'}:
                return hint
            else:
                raise ValueError("Invalid Hint.Please enter 'higher', 'lower'"
                                 ",or 'correct'")
        except ValueError as e:
            print(e)


def play_game():
    """
    Description :
    This function runs the game loop. The player selects a number, and the
    computer guesses it using binary search.
    The player provides hints to guide the computer's guesses.
    """
    print("\nThink of a number between 1 and 100. The computer will try to "
          "guess it!")
    start, end = 1, 100
    attempts = 0

    while start <= end:
        try:
            guess = (start + end) // 2
            print(f"The computer guesses: {guess}")
            hint = get_player_hint()
            attempts += 1

            if hint == 'correct':
                print(f"Yay! The computer guessed your number {guess} in "
                      f"{attempts} attempts.")
                break
            elif hint == 'higher':
                start = guess + 1
            elif hint == 'lower':
                end = guess - 1
            if start > end:
                raise RuntimeError("Hints provided are inconsistent")
        except RuntimeError as e:
            print(e)
            print("Restarting the game ...")
            break


def main():
    """
    Description :
    The main function runs the game and allows for multiple runs.
    """
    while True:
        play_game()
        while True:
            replay = (input("\nDo you want to play again? (yes/no): ").strip()
                      .lower())
            if replay in {'yes', 'no'}:
                break
            print("Invalid input. Please enter 'yes' or 'no'.")

        if replay == 'no':
            print("Thank you for playing! Goodbye.")
            break


# Call the main function
main()
