# loops
from data.countries import countries
import day_6

# while loop
c = 0
while c < 5:
    print(c)
    c += 1
print(c)
# ends as soon as c = 5.

# break
c = 0
while c < 5:
    print(c)
    c += 1
    if c == 3:
        break
# breaks when condition is met, doesnt print

# continue
c = 0
while c < 5:
    # if c == 3:
    #     c -= 1
    #     continue
    print(c)
    c += 1
# prints 0,1,2 (and 2 infinitely)

# for loops
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
# to unpack the value, you need to do items, not just person
for key, value in person.items():
    print(key, value)

# same with continue and break
for key, value in person.items():
    print(key, value)
    if isinstance(value, int):
        break


# Exercises
day_6.create_randint(1, 13, 3)

# 4: Use nested loops to create the following:
for i in range(9):
    print('# # # # # # # #')
    continue

# 7: Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(100):
    if i % 2 == 0:
        print(i)

# 12: Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
print(countries)

for country in countries:
    if 'land' in country:
        print(country)
