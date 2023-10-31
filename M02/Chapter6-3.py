guessMe = 5
number = 1

for number in range(10):

    if number < guessMe:
        print("Too low!")
    elif number == guessMe:
        print("Found it!")
        break
    elif number > guessMe:
        print("Oops!")
        break
    
    number += 1