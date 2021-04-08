import csv

### Compile CSV data into a list of lists
with open('pizzaingred.csv', newline='') as f:
    reader = csv.reader(f)
    reader.__next__()
    ingred_list = list(reader)

### Prompts the user for pizza size
def getSize():
	while True:
		try:
			size = int(input("Enter Size (1 = Small, 2 = Medium, 3 = Large): "))
		except ValueError:
			print("Try again!")
			continue
		if size > 3 or size < 1:
			print("Try again!")
			continue
		return(size)

order_list = []

### Prompt the user for the toppings they want
def getToppings():
	while True:
		try:
			toppings = int(input("Enter Toppings (-1 to complete): "))
		except ValueError:
			print("Try again!")
			continue
		if toppings > 23 or toppings < -1:
			print("Try again!")
			continue
		elif toppings == -1:
			return(order_list)
		order_list.append(toppings)

### Use the user's topping list to gather calorie and portion counts
def calcCalories(size, toppings):
	calorie_list = []
	for i in range(len(toppings)):
		x = toppings[i]
		calories = ingred_list[x][1]
		portion = ingred_list[x][2]
		total = float(calories) * float(portion)
		if size == 2:
			total *= 1.5
			z = 1.5
		elif size == 3:
			total *= 1.75
			z = 1.75
		else:
			z = 1
		calorie_list.append(total)
	y = z * 860
	calorie_list.append(y)
	final = 0
	for j in range(len(calorie_list)):
		final += float(calorie_list[j])
	print("Total Pizza Calories: " + str(final))

### Prints a key for all the toppings for accessibility
def printToppings(list):
	for i, key in enumerate(list):
		print(i, key[0])

pizza_size = getSize()
printToppings(ingred_list)
toppings = getToppings()
calcCalories(pizza_size, toppings)