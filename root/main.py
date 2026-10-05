import random

coin = random.choice(["heads", "tails"])

guess = None

while not (guess == 'heads' or guess == 'tails'):
    guess = input("Guess heads or tails! ")

if guess == coin:
    print("Correct!")
else:
    print("Incorrect!")