import random

def guess_number(min_value, max_value):
    """Guesses a number between min_value and max_value.

    Args:
        min_value (int): The minimum possible value.
        max_value (int): The maximum possible value.

    Returns:
        int: The guessed number.
    """

    guesses = 0
    while True:
        # Generate a random number within the range
        guess = random.randint(min_value, max_value)
        guesses += 1

        response = input(f"Is {guess} too high (h), too low (l), or correct (c)? ").lower()
        if response == "c":
            print(f"You guessed it in {guesses} guesses!")
            return guess
        elif response == "h":
            max_value = guess - 1
        elif response == "l":
            min_value = guess + 1
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")

# Example usage
min_value = 1
max_value = 100
guessed_number = guess_number(min_value, max_value)
