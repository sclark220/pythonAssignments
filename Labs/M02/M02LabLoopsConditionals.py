# These numbers are the gpa requirment for the dean's list and honor roll respectivly 
DEANTHRESHOLD = 3.5
HONORTHRESHOLD = 3.25

quitInputs = ("zzz", "ZZZ")
isRunning = True
while isRunning:
    # Get user input
    userInput = input("Enter last name or 'zzz' to quit: ")
    
    if userInput in quitInputs: # checks for string and quits
        print("Fine leave then")
        isRunning = False
    else:
        lastName = userInput
    # Get user input
    userInput = input("Enter last name or 'zzz' to quit: ")

    if userInput in quitInputs: # checks for string and quits
        print("Fine leave then")
        isRunning = False
    else:
        firstName = userInput
    # Get user input
    userInput = input("Enter GPA with up to 2 decimal places 'Ex: 1, 2.1, or 3.99': ")
    
    if userInput in quitInputs: # checks for string and quits
        print("Fine leave then")
        isRunning = False
    else:
        gpa = float(userInput)
    # Checks entered gpa and prints results
    if gpa >= DEANTHRESHOLD:
        print(f"\n {firstName} {lastName}, you are on the Dean's list!")
    # Checks entered gpa and prints results
    if gpa >= HONORTHRESHOLD:
        print(f"\n {firstName} {lastName}, you are on the Honor Roll! \n")
        isRunning = False
    # Checks entered gpa and prints results
    if gpa < HONORTHRESHOLD:
        print(f"\n Me too {firstName} {lastName}... me too...\n")
        isRunning = False
