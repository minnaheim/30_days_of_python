# lists
'''
There are four collection data types in Python :

List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.
Array: data structure used to store multiple items, vector containing multiple items
'''

# create lists
import random as rd
list = list()
list = []

names = ['Minna', 'Ben', 'Carina', 'Mathilde']
print(f'Names: {names}')

# lists can have different inputs
list = [True, 'Minna', {'Eyes': 'Green'}, (1, 2, 3, 4, 5)]
print(list)
list[2]  # {'Eyes': 'Green'}

first, second, third, *rest = names
print(rest)

names[::2]  # take by two's


# modifying
names[3] = 'Maja'
names.append('Mathilde')
names.insert(2, 'Lisa')
# ['Minna', 'Ben', 'Lisa', 'Carina', 'Maja']

minna = 'Minna' in names  # True

# removing items
names.remove('Carina')
names.pop()  # 'Maja'
# ['Minna', 'Ben', 'Lisa']

del names[2]
# ['Minna', 'Ben']

names2 = names.copy()

all_names = names + names2

all_names.count('Minna')  # 2
len(all_names)
print(all_names)

# sorting
all_names.sort()  # ['Ben', 'Ben', 'Minna', 'Minna']
all_names.sort(reverse=True)  # ['Minna', 'Minna', 'Ben', 'Ben']

names2.clear()  # deletes all elements

# how to know whether something is a method (var.method) or a function (function(var)) -> usually method, unless you wrote it yourself, or few cases see [here](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/02_Day_Variables_builtin_functions/02_variables_builtin_functions.md)

# Exercises
rd.randint(1, 40)
# 6 : Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon']

# 14: Join the it_companies with a string '#;  '
'#;  '.join(it_companies)


# Level 2:3
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA',
             'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic = countries
scandic
