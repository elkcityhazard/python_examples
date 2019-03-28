#This is a guess the number game

import random

secret_number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20...")

#ask the player to guess 6 Times

for guesses_taken in range(1,7):
    guess = int(input("Take a guess..."))
    if guess < secret_number:
        print("You guessed too low.")
    elif guess > secret_number:
        print("You guessed too high")
    else:
        break #This condition is the correct guess!

if guess == secret_number:
    print("Good Job! you guessed my number in, " + str(guesses_taken) + " guesses!")
else:
    print("Sorry, the number I was thinking of was, " + str(secret_number) + '.')
