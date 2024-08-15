# file handling
from day_18 import most_frequent_words
from day_6 import create_randint as rand
import xml.etree.ElementTree as ET
import pandas as pd
import re
import collections
import csv
import json
import os
import random as rd

countries = open("data/countries.py", mode="r")  # x if you want to create one
f = open('data/names.py')
f.read(5)  # can only read if mode = r
f = open('data/names.py', mode='w')
f.write("adding this?")  # is 12 characters long?
f.writelines('this is an exemplary written line')

'''"r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)'''


f.close()


# print()

with open("data/countries.py") as f:
    lines = f.read().splitlines()
    # print(lines[:20])  # ['countries = [', "    'Afghanistan',", "    'Albania',", "    'Algeria',", "    'Andorra',", "    'Angola',", "    'Antigua and Barbuda',", "    'Argentina',", "    'Armenia',", "    'Australia',", "    'Austria',", "    'Azerbaijan',", "    'Bahamas',", "    'Bahrain',", "    'Bangladesh',", "    'Barbados',", "    'Belarus',", "    'Belgium',", "    'Belize',", "    'Benin',"]

# append:
# with open('./data/reading_file_example.txt', 'x') as f:
#     f.write('This file will be created')

with open('./data/reading_file_example.txt', 'a') as f:
    f.write('This text has to be appended at the end')

with open('./data/writing_file_example.txt', 'w') as f:
    f.write('This text will be written in a newly created file')


# to remove files in an elegant way:
# if os.path.exists('./files/example.txt'):
#     os.remove('./files/example.txt')
# else:
#     print('The file does not exist')

# different file types:
# txt files

# json files -> are like dictionary objects but need to be strings

person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# print(type(person_json))  # str
# let's change JSON to dictionary
person_dct = json.loads(person_json)
# print(type(person_dct))  # dict

# important that age is str
matias_json = '''{
    "first_name": "Matias",
    "last_name": "Turkulainen",
    "age": "27"
}'''
# print(type(matias_json))  # str

matias_dict = json.loads(matias_json)
# print(type(matias_dict))  # dict

# dictionary to json
matias_to_json = json.dumps(matias_dict)
# print(type(matias_to_json))  # str

# create new json file
# use with as so that we create a file pointer - so that i have unique access and file doesnt get corrupted (automatic closer, by using with it closes after automatically)
with open("data/test.json", mode='w') as f:
    json.dump(matias_json, f)
    json.dump(matias_to_json, f)


# working with csv

with open("data/example.csv", "w") as f:
    beans = "beans"
    beans_csv = ",".join([beans]*5)
    f.write(beans_csv)


# print(rand(1, 9, 3))


# 6 : Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) The ten most frequent words used in Melania's speech

with open("data/obama_speech.txt") as obama:
    # remove line breaks
    obama = obama.read().replace('\n', '')
    m = most_frequent_words(obama)
    print(m)  # ('the', 120), ('and', 107), ('of', 81), ('to', 66), ('our', 58)]

with open("data/michelle_obama_speech.txt") as michelle:
    michelle = michelle.read().replace('\n', '')
    m = most_frequent_words(michelle)
    print(m)  # [('to', 84), ('and', 80), ('the', 78), ('', 48), ('of', 46)]


# 7
''' Write a python application that checks similarity between two texts. 
It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. 
For instance check the similarity between the transcripts of Michelle's and Melanina's speech. 
You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). 
List of stop words are in the data directory'''

# what is the metric to evaluate similarity? how many words are in both texts out of all words


# 9
