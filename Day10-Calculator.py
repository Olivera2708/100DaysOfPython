logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
    return n1 + n2

def min(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def dev(n1, n2):
    return n1 / n2

def calc(num1):
    operation = input("Pick an operation -> ")
    number2 = float(input("What's the second number? -> "))
    if operation == "+":
        res = add(num1, number2)
    elif operation == "-":
        res = min(num1, number2)
    elif operation == "*":
        res = mul(num1, number2)
    elif operation == "/":
        res = dev(num1, number2)

    print(f"{num1} {operation} {number2} = {res}")
    again = input(f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation -> ")
    if again == "y":
        calc(res)
    elif again == 'n':
        beg()

def beg():
    number1 = float(input("What's the first number? -> "))
    print("+\n-\n*\n/")
    calc(number1)

print(logo)
beg()