# dictionaries

# creating dictionaries
import day_6
d = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
# exemplary dictionary
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# shows that values can be of any data type

len(d)  # 4
person.items()  # shows all pairs in tuples

# accessing items:
d['key1']  # 'value1'
d['value1']  # error
d[1]  # error
print(person['skills'][1])  # React

person.get('first_name')  # 'Asabeneh'
# how to get key based on value in dict

# adding items to dict
person.update({'hobbies': ['cycling', 'reading', 'knitting']})
person['skills'].append('R')
person['hobbies']
person['hello'] = 'my name is'
person['hello']  # 'my name is'

# modifying items
person['hello'] = 'i am'
person['hello']  # 'i am'
person['skills'] = 'R', 'Python'
print(person)

# modifying keys
person['programs'] = 'R', 'Python'
del person['skills']

# removing pairs
person.pop('age')
person['age']
person.popitem()  # removes last key and value pair?


d.copy()

d.clear()
d

# values and keys as list
# dict_values(['Asabeneh', 'Yetayeh', 'Finland', True, {'street': 'Space street', 'zipcode': '02210'}, ['cycling', 'reading', 'knitting'], 'i am'])
person.values()
# dict_keys(['first_name', 'last_name', 'country', 'is_marred', 'address', 'hobbies', 'hello'])
person.keys()

# Exercises
day_6.create_randint(1, 11, 3)
# [10, 4, 2]

# 2: Add name, color, breed, legs, age to the dog dictionary
dog = dict()
dog = {'name': 'ella', 'color': 'black', 'breed': [
    'i', 'dont', 'know'], 'legs': 4, 'age': 7}

# 4: Get the length of the student dictionary
student = dog
print(len(student))  # 5

# 10: Delete one of the items in the dictionary
del student['legs']
print(student)
