import random

secretNumber = random.randrange(1, 10)

userInput = input("Enter a number between 1 and 10 or type 'quit' to exit: ")

while (userInput != 'quit'):

    if int(userInput) == secretNumber:
        print("You did it!")
        secretNumber = random.randrange(1, 10)

    elif int(userInput) > secretNumber:
        print("Too high!")

    elif int(userInput) < secretNumber:
        print("Too low!")

    userInput = input("Try again or type 'quit' to exit: ")