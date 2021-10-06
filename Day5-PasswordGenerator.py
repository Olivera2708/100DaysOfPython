import random

print("Welcome to PyPassword Generator!")
letters = int(input("How many letters would you like? -> "))
symbols = int(input("How many symbols would you line? -> "))
numbers = int(input("How many numbers would you like? -> "))

password = []
for i in range(0, letters):
    password += chr(random.randint(65, 90))
for i in range(0, symbols):
    password += chr(random.randint(33, 47))
for i in range(0, numbers):
    password += str(random.randint(0, 9))

random.shuffle(password)

passw = ""
for char in password:
    passw += char

print("Here is your password: " + passw)
