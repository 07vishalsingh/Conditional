import random

def play_rock_paper_scissors():
    """Plays a game of Rock-Paper-Scissors against the computer."""

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        return

    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose.")

# Example usage
play_rock_paper_scissors()
