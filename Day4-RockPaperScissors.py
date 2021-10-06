import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gameimage = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 fot Paper or 2 for Scissors. -> "))
if player < 0 or player > 2:
    print("Invalid number")
print(gameimage[player])
computer = random.randint(0, 3)
print("Computer:\n" + gameimage[computer])

if (player == computer):
    print("Draw!")
elif (player == 0 and computer == 1) or (player == 1 and computer == 2) and (player == 2 and computer == 0):
    print("You lose!")
else:
    print("You win!")