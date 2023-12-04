import datetime

# I wanted to the time and the date
today = datetime.datetime.now()
weekday = today.strftime('%A')

# Testing
#print(today)
#print(weekday)

# Write to end of file
with open("M06/today.txt", "a") as file:
    file.write(f"Today is {weekday} {today} \n")

# Read from file
with open("M06/today.txt") as file:
    todayString = file.readlines()[-1]
    print(todayString)

