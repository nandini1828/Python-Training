"""Number Guessing Game"""

import random


def safe_input(prompt, default=""):
    """Read input, but return a default when no input is available."""
    try:
        value = input(prompt).strip()
    except EOFError:
        print("No input provided. Using the default value.")
        return default
    return value if value else default


def get_valid_guess(low, high):
    """Ask for a guess until the input is valid."""
    while True:
        try:
            guess = int(input(f"Enter a number between {low} and {high}: "))
            if low <= guess <= high:
                return guess
            print("That number is outside the allowed range.")
        except EOFError:
            print("No input provided. Using a default guess.")
            return (low + high) // 2
        except ValueError:
            print("Please enter a whole number.")


def play_round(max_attempts):
    """Play a single round of the guessing game."""
    secret_number = random.randint(1, 20)
    score = 0

    print(f"\nI picked a number between 1 and 20. You have {max_attempts} attempts.")

    for attempt in range(1, max_attempts + 1):
        guess = get_valid_guess(1, 20)

        if guess == secret_number:
            print(f"Correct! You guessed it in {attempt} attempt(s).")
            score = max_attempts - attempt + 1
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        if attempt == max_attempts:
            print(f"No more attempts. The number was {secret_number}.")
    else:
        print("You completed all attempts without breaking the loop.")

    return score


def main():
    print("Welcome to the Number Guessing Game")
    total_score = 0

    while True:
        round_score = play_round(5)
        total_score += round_score
        print(f"Your score for this round: {round_score}")
        print(f"Total score: {total_score}")

        while True:
            replay = safe_input("Play again? (y/n): ", "n").strip().lower()
            if replay in {"y", "n"}:
                break
            print("Please enter 'y' or 'n'.")
        if replay == "n":
            print("Thanks for playing!")
            break
        elif replay == "y":
            pass


if __name__ == "__main__":
    main()
