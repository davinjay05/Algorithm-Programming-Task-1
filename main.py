# imports
import random

# initiate variable
lower_bound = 1
higher_bound =100
max_attempts = 5

#generate random number
secret_number = random.randint(lower_bound, higher_bound)

#guess the number
def get_guess():
    # while loop for players to input answer. until it's correct
    while True:
        # mechanism to catch value errors. 
        # if the player enter number that is outside the range of the lower and higher bound, it will print "invalid number!".   
        try:
            guess = int(input(f"Guess a number between {lower_bound} and {higher_bound}: "))
            if lower_bound <= guess <= higher_bound:
                return guess
            #if the player enter non numbers it will print "Invalid Number. Please enter a valid number"
            else:
                print("Invalid Number!")
        except ValueError:
            print("Invalid number. Please enter a Valid number")

# check the players whether it's correct or wrong
def check_guess(guess, secret_number):
    #if the player answer is correct then the check definition is correct
    if guess == secret_number:
        return "correct" 
    #if the player answer is wrong it can show the player that the number is too high or low
    elif guess < secret_number:
        return "The number that you have answered is Too Low!"
    else:
        return "The number that you have answered is Too High!"

#play the guess number
def play_game():
    attempts = 0
    won = False

    #attempts for players that needed to be answer
    while attempts < max_attempts:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, secret_number)

        if result == "correct":
            print(f"Congratulations! You have guessed the number {secret_number} in {attempts} attempts.")
            won = True
            break
        else:
            print(f"{result}. Try Again!")

    if not won:
        print(f"Sorry, you ran out of attempts! The answer is {secret_number}. Try Again?")

# this code allows you to execute code as a standalone script but you can also use it as a module.
if __name__== "__main__":

# intro of a game.
    print("Welcome to the Number Guessing Game!")
    play_game()