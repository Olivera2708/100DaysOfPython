from replit import clear
import random

logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal():
    return random.choice(cards)

def checkwinner(myCards, computer):
    mysum = 0
    for i in myCards:
        mysum += i
    if (11 in myCards) and mysum > 21:
        mysum -= 10
    compsum = 0
    for j in computer:
        compsum += j
    if (11 in computer) and compsum > 21:
        compsum -= 10
    if mysum > 21 and compsum > 21:
        print("Went over. You lose!")
    elif compsum > 21:
        print("Opponent went over. You win!")
    elif abs(21 - mysum) < abs(21 - compsum):
        print("You win!")
    elif abs(21 - mysum) > abs(21 - compsum):
        print("You lose!")
    else:
        print("It's a tie!")
    beg()

def startGame():
    clear()
    print(logo)
    myCards = []
    myCards.append(deal())
    myCards.append(deal())
    print(f"Your cards: {myCards}")
    computer = []
    computer.append(deal())
    print(f"Computer's first card: {computer}")
    ans = input("Type 'y' to get another card, type 'n' to pass -> ").lower()
    if ans == "y":
        myCards.append(deal())
    computer.append(deal())
    print(f"Your final hand: {myCards}")
    print(f"Computer's final hand: {computer}")
    checkwinner(myCards, computer)

def beg():
    ans = input("Do you want to play a game of Blackjack? Type 'y' or 'n' -> ").lower()
    if ans == "y":
        startGame()

beg()
