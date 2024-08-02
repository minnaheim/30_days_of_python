# strings
# escape sequences
name = ' My \tName \\ is \n Minna \' Heim \"'
print(name)

# string formatting old style
first_name = 'Minna'
last_name = 'Heim'
language = 'Python'
age = 22
formatted_string = 'I am %s %s. I am %i years old. I teach %s' % (
    first_name, last_name, age, language)
print(formatted_string)

# string formatting new style
formatted_string = 'I am {} {}. I am {} years old. I am learning {}'.format(
    first_name, last_name, age, language)
print(formatted_string)

# f-string
formatted_string = f'Hello my name is {first_name} and {last_name}'
print(formatted_string)

# reversing strings
print(first_name[::-1])
# anniM
# slicing
first_name[3:]
# na

language = 'Python'
language[0:6:2]  # 'Pto' -> since [start:stop:step]


# ways to find or count strings
language.count('y')  # 1
formatted_string.rfind("n")  # at position 24 is the last n
formatted_string.find('n')  # first is at position 9
formatted_string.endswith("na")  # False
formatted_string.startswith("He")  # True

# same with...
formatted_string.isalnum()  # False not just alphanumeric characters
formatted_string.isdigit()  # False, not digit...
formatted_string.islower()  # False, upper case letters too
formatted_string.isupper()  # false, also lower case letters
formatted_string.swapcase()  # 'hELLO MY NAME IS mINNA AND hEIM'

# Exercises:
# Use index to determine the position of the first occurrence of F in Coding For All.
statement = 'Coding For All'
statement.index("F")  # 7

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
slice_out = 'because because because'
# sentence.find('because')  #31
# sentence.rfind('because') #47 -> only start of the word
# sentence[31:47]
sentence.index(slice_out) + len(slice_out) - 1
sentence[31:53]


# Use the new line escape sequence to separate the following sentences.
sentence = 'I am enjoying this challenge.\nI just wonder what is next.'
print(sentence)
