# with open('.\\week 1\\intro.md', 'r') as file:
#     print(file.read())

# with open('.\\week 1\\ex_text.md', 'w') as new_file:
#     new_file.write("""Hello tlkajnskfljas; dxklgvh kas;djhgf ;laskj kdf jjl;ksad jfk;djf ha;lkshjgskjhgalk; sjdk;sh;lkshklj;dhsg""")


# val = input("Enter num: ")

# print(val + "!")
# -------------------------------------------------------------------------------------------------------------------------

# Create an empty dictionary

# come up with 5 vocabulary words as a group. It can be related to python or something separate

# Create a dictionary with the vocabulary words as keys and a nested dictionary with the definition and key 

# Make a list out of the values and pick a random question

# Use the built in input() function to get user input for the answer

# Compare the input to the key and print correct if its right, and incorrect if its wrong. 

# Wrap this all in a function called flash_cards(dictionary)

# Example

import random as rnd

dict = {}

dict["int"] = "A number value"
dict["string"] = "An array of characters"
dict["float"] = "A number w/ decimal"
dict["boolean"] = "True or False value"
dict["list"] = "An Array of items"

keylist = list(dict.keys())
key = str(rnd.sample(keylist, 1)[0])
print(key)
user_inpt = input("Input your definition: ")
if user_inpt == dict.get(key):
    print("Correct!")
else:
    print("Incorrect, the answer is: " + dict.get(key))








# dictionary = {
#     "python": {
#         "definition": "A standardized interpreted programming language universally used in web development, software, data science and machine learning",
#         "key": "python"
#     }
# }

# defi = dictionary['python']['definition']
# # print(defi)
# answer = input(defi + "\n")
# print(answer)
# if answer == dictionary['python']['key']:
#     print("Way to go!")