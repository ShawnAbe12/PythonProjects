#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# list_names = []
# list_letters = []
# with open("Input/Names/invited_names.txt") as file:
#     for i in file.readlines():
#         list_names.append(i.strip("\n"))
#     print(list_names)
# for names in list_names:
#     with open("Input/Letters/starting_letter.txt", "r") as r_file:
#         str = r_file.readlines()
#         x = str[0].replace("[name]", names)
#
#         with open(f"Output/ReadyToSend/{names}.txt", "w") as w_file:
#             w_file.writelines(x)
#             w_file.writelines(str[1:])

with open("./Input/Names/invited_names.txt") as file:
    list_names = file.readlines()

with open("./Input/Letters/starting_letter.txt") as file:
    letter_contents = file.read()
    for name in list_names:
        name = name.strip("\n")
        letter = letter_contents.replace("[name]", name)
        with open(f"./Output/ReadyToSend/{name}.txt", "w") as w_file:
            w_file.write(letter)
