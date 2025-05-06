import random
import time


def get_attempts(difficulty):
    levels = {'easy': 10, 'medium': 5, 'hard': 3}
    return levels.get(difficulty, 5)  # default difficulty when invalid input


loop = True
while loop:
    print("\nWelcome to the Number Guessing Game !")
    print("Rules: The computer will randomly select a number from 1 - 100")
    print("You have to guess the number based on the hints provided")
    print("Difficulty: Easy (10 attempts), Medium (5 attempts), Hard (3 attempts). \n")

    difficulty = input("Please select difficulty level (easy, medium, hard): ").strip().lower()
    chosen_num = random.randint(1, 100)
    attempts = get_attempts(difficulty)

    print(f"You have {attempts} attempts to guess the number. Good Luck! :)")
    time_start = time.time()

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"\nAttempt no. {attempt}/{attempts} \nEnter Guess: "))
        except ValueError:
            print("Invalid Input! Please enter a number between 1-100.")
            continue

        if guess < 1 or guess > 100:
            print("Out of range! Please guess a number between 1 and 100.")
            continue

        if guess == chosen_num:
            end_time = time.time()
            time_elapsed = end_time - time_start
            print(f"CONGRATULATIONS YOU GOT IT! Within {attempt} attempts and in {time_elapsed:.2f} second/s.")
            break
        elif guess < chosen_num:
            print("Nope! Try higher.")
        else:
            print("Oops! Try lower.")
    else:
        print(f"\nG A M E  O V E R . \nThe correct number is {chosen_num}.")

    while True:
        repeat = input("Would you like to play again? (yes/no): ").strip().lower()
        if repeat == "yes":
            loop = True
            break
        elif repeat == "no":
            print("Thank you for playing! :)")
            loop = False
            break
        else:
            print("INVALID INPUT! Please enter yes or no.")
            continue
