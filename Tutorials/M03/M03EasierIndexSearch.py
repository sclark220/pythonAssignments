arr = [1, 2, 3, 4, 5]

k = int(input(f"Which number do you want to know the index of in a list from {arr}: "))

for number in arr:
	if number == k:
		print(f"The index of {k} is {arr.index(k)}")
        break