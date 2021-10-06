#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = open("C:/Users/Olivera/Documents/Python learning/Day24-MailMerge/Input/Names/invited_names.txt")
name_list = names.readlines()
names.close()

starting = open("/Users/Olivera/Documents/Python learning/Day24-MailMerge/Input/Letters/starting_letter.txt")
message = starting.read()
starting.close()
for name in name_list:
    strip_name = name.strip()
    new_letter = message.replace("[name]", strip_name)
    with open(f"/Users/Olivera/Documents/Python learning/Day24-MailMerge/Output/ReadyToSend/letter_for_{strip_name}.txt", "w") as completed_leter:
        completed_leter.write(new_letter)