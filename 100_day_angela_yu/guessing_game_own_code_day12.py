#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
from art import logo


def game():
    print(logo)
    print("Welcome to the guessing game\n")
    level = input("Choose the difficulty 'easy' or 'hard'")

    def choose_difficulty(level):
        if level == 'easy':
            return 5
        else:
            return 10

    actual_number = random.randint(1, 101)
    # Allow the player to submit a guess for a number between 1 and 100.
    no_of_turns_remaining = choose_difficulty(level)
    turn_left = True
    while turn_left:
        guessed_number = int(input("Guess the number \n"))
        # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
        if actual_number == guessed_number:
            print(f"Your guess {actual_number} is right , You win")
            turn_left = False
        elif actual_number > guessed_number:
            print("Too low")
        else:
            print("Too high")
        # If they got the answer correct, show the actual answer to the player.
        # Track the number of turns remaining.
        no_of_turns_remaining -= 1
        if no_of_turns_remaining == 0:
            print("NO turns left")
            turn_left = False


play_again = input(
    "Do you like to play the guessing game? Enter 'y' for yes and 'n' for no")
if play_again == 'y':
    game()
else:
    quit()
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
