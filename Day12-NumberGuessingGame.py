import random

print('''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard'.''')
difficulty = input()
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("Error")
number = random.randint(0, 100)
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it!.")
        attempts = 0
    elif guess > number:
        print("Too high.")
        attempts -= 1
    elif guess < number:
        print("Too low.")
        attempts -= 1
    if attempts != 0:
        print("Guess again.")
print(f"The answer was {number}.")
