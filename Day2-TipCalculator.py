print("Welcome to tip calculator.")
total = float(input("What was your total bill? $"))
people = int(input("How many people to split the bill? "))
tippercentage = int(input("What percentage tip would you like to give? "))
result = (total + total * tippercentage / 100) / people

print("Each person should pay: $" + str(round(result, 1)))