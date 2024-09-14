import random


lower_bound = 1
higher_bound =100
max_attempts = 10


secret_number = random.randint(lower_bound, higher_bound)


def get_guess():
    while True:
        try:
            guess = int(input(f"Guess a number between {lower_bound} and {higher_bound}: "))
            if lower_bound <= guess <= higher_bound:
                return guess
            else:
                print("Invalid Input. Please enter a number within the specified range")
        except ValueError:
            print("Invalid input. Please enter a Valid number")


def check_guess(guess, secret_number):
    if guess == secret_number:
        return "correct" 
    elif guess < secret_number:
        return "Too Low"
    else:
        return "Too High"


def play_game():
    attempts = 0
    won = False

    while attempts < max_attempts:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, secret_number)

        if result == "correct":
            print(f"Congratulations! You have guessed the secret number {secret_number} in {attempts} attempts.")
            won = True
            break
        else:
            print(f"The answer is {result}. Try Again!")

    if not won:
        print(f"Sorry, you ran out of attempts! The secret number is {secret_number}. Try Again?")
    
if __name__== "__main__":
    print("Welcome to the Number Guessing Game!")
    play_game()