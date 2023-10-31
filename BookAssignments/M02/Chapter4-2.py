yesAnswers = ('y', 'Y', 'yes', 'Yes','YES')
noAnswers = ('n', 'N', 'no', 'No','NO')

small = True
green = True

userInput = input("Is it small? Enter 'y' or 'n': ")

if userInput in yesAnswers:
    print("The object is small!")
    small = True
elif userInput in noAnswers:
    print("The object is NOT small!")
    small = False
else:
    print("YOU BROKE IT!")

userInput = input("Is it green? Enter 'y' or 'n': ")

if userInput in yesAnswers:
    print("The object is green!")
    green = True
elif userInput in noAnswers:
    print("The object is NOT green!")
    green = False
else:
    print("YOU BROKE IT!")

print(f"\nThe object is \n \
    Green: {green}\n \
    Small: {small}\n")

if small == True and green == True:
    print("It is a Pea \n")
elif small == True and green == False:
    print("It is a Cherry \n")
elif small == False and green == True:
    print("It is a Watermelon \n")
elif small == False and green == False:
    print("It is a Pumpkin \n")
