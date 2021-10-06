student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

import pandas
student_data_frame = pandas.DataFrame(student_dict)

data = pandas.read_csv("C:/Users/Olivera/Documents/Python learning/Day26-NATOAlfabet/nato_phonetic_alphabet.csv")
phonetic_dic = {row.letter:row.code for (index, row) in data.iterrows()}

def enter_word():
    word = input("Eneter some word ").upper()
    try:
        result = [phonetic_dic[letter] for letter in word]
    except KeyError:
        print("Only letters please")
        enter_word()
    else:
        print(result)

enter_word()
