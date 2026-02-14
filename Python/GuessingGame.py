
import random

print("Welcome to the Number Guessing Game!")

while True:
    print("\nI'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess_str = input("Enter your guess: ")
            guess = int(guess_str)
        except ValueError:
            print("That's not a number! Try again.")
            continue 
        attempts = attempts + 1 
        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else: 
            print(f"Correct! You guessed the number in {attempts} attempts.")
            break 
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'no':
        break 
print("Thanks for playing!")