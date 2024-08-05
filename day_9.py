# conditonals
# differences between if, if else and elif:

# if condition true, run certain thing, if not true (aka else) then the other block will run
# we use elif if we have multiple conditions

import day_6
a = range(1, 10)
for i in a:
    if i < 5:
        print('small')
    elif i == 5:
        print('five')
    else:
        print('large')

# short hand
print("a") if len(a) >= 10 else print("b")

# if and or conditions
a = 3
if a == 3 or a > 3:
    print("3")


# Exercises:
day_6.create_randint(1, 7, 3)

# 2:
'''Compare the values of age1 and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if age1 = your_age.
Output:'''


def age(age1: int):
    your_age = input("What is your age?")
    your_age = int(your_age)
    if your_age > age1:
        diff = your_age - age1
        s = f'You are {diff} years older than me!'
        return s
    elif your_age == age1:
        s = "We are the same age"
        return s
    else:
        diff = age1 - your_age
        s = f'I am {diff} years older than you!'
        return s


my_age = 22
agee = age(my_age)
print(agee)

# 6 If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')


def fruits():
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruit = input('Name a fruit:')
    if fruit in fruits:
        print("Already in the fruit list")
    else:
        fruits.append(fruit)
        print(fruits)


fruits()

# 7
'''
* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:'''

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

if person['skills']:
    print(person['skills'])
else:
    print("no skills")
