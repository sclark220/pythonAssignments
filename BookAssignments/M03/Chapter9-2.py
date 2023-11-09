

def Get_Odds():
    odds = []
    for num in range(10):
        if num % 2 != 0:
            odds.append(num)
    return odds
    

print(Get_Odds())
oddNumber = Get_Odds()

#Print 3rd number
print(oddNumber[2])

#Only prints 3rd number but with a loop for some reason
for i in range(len(oddNumber)):
    if i == 2:
        print(oddNumber[i])