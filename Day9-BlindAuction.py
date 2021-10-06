from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bids = {}

def finish():
    highest = 0
    winner = ""
    for bidder in bids:
        amount = bids[bidder]
        if amount > highest:
            highest = amount
            winner = bidder
    clear()
    print(f"The winner is {winner} with the bid of ${highest}")


def main():
    name = input("What is your name? -> ")
    bid = int(input("What is your bid? -> $"))
    bids[name] = bid
    next = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if next == "yes":
        clear()
        main()
    elif next == "no":
        finish()

print(logo)
main()