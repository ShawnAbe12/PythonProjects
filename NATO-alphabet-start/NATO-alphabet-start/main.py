# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
import pandas
is_on = True

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"
data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data)
NATO_dict ={row.letter:row.code for (index,row) in data.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while is_on:
    word = input("Please enter a word")
    try:
        code_words = [NATO_dict[letter.upper()] for letter in word]
        print(code_words)
        is_on = False
    except KeyError:
        print("Please only enter letters from the Alphabet")
