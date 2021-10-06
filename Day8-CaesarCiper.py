logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

def encode(message, shift):
    result = ""
    for i in message:
        letter = chr(ord(i) + shift)
        if ord(letter) > 122:
            letter = chr(ord(letter) - 25)
        result += letter
    return result

def decode(message, shift):
    result = ""
    for i in message:
        letter = chr(ord(i) - shift)
        if ord(letter) < 97:
            letter = chr(ord(letter) + 25)
        result += letter
    return result

def game():
    type = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type yout message:\n").lower()
    shift = int(input("Type the shift number\n"))
    if (type == "encode"):
        result = encode(message, shift)
        print("Here is encoded result: " + result)
    elif (type == "decode"):
        result = decode(message, shift)
        print("Here is decoded result: " + result)
    else:
        print("Error")
    again = input("Type 'yes' if you want to go again.\n").lower()
    if (again == "yes"):
        game()

print(logo)
game()