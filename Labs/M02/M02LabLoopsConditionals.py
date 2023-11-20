""" 
Checks if a number is greater than 3.5 and 3.25
Prints if true or false
If both false print a little sympathy 
"""
quitInputs = ("zzz", "ZZZ")
while True:
    userInput = input("Enter last name or 'zzz' to quit: ")

    if userInput in quitInputs:
        print("Fine leave then")
        break
    else:
        lastName = userInput

    userInput = input("Enter last name or 'zzz' to quit: ")

    if userInput in quitInputs:
        print("Fine leave then")
        break
    else:
        firstName = userInput

    userInput = input("Enter GPA with up to 2 decimal places 'Ex: 3, 3.1, or 3.99': ")

    if userInput in quitInputs:
        print("Fine leave then")
        break
    else:
        gpa = float(userInput)

    if gpa >= 3.5:
        print(f"\n {firstName} {lastName}, you are on the Dean's list!")
    
    if gpa >= 3.25:
        print(f"\n {firstName} {lastName}, you are on the Honor Roll! \n")
        break

    if gpa < 3.25:
        print(f"\n Me too {firstName} {lastName}... me too...\n")
        break