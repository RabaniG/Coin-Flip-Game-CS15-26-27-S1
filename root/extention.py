# Coin Game: Extension Three Strikes [You can name anything you want]

import random

number_of_incorrect_guesses = 0

while True:
    coin = random.choice(["heads", "tails"])
    guess = None


    while not (guess == "heads" or guess == "tails"):
        guess = input("Guess heads or tails: ")
        guess = guess.lower()  # put user input in lowercase

    if coin == guess:
        print("Correct!")
        number_of_incorrect_guesses = 0  # reset the incorrect counter
    else:
        print("Incorrect!")
        number_of_incorrect_guesses = number_of_incorrect_guesses + 1  # increase the incorrect counter by 1

        # Game Ending Condition
        if number_of_incorrect_guesses == 3:
            break  # Stops the while loop

    print("Number of incorrect guesses is:", number_of_incorrect_guesses)

print("Game Ends!")