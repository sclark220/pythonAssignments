guessMe = 7
number = 1

while number <= guessMe:

    if number < guessMe:
        print("Too low!")
    elif number == guessMe:
        print("Found it!")
        break
    elif number > guessMe:
        print("Oops!")
        break
    
    number += 1