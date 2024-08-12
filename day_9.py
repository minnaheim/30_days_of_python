### Conditonals
# Differences between if, if else and elif conditionals.

# If condition true, run certain thing, if not true (aka else) then the other block will run
# We use elif if we have multiple conditions

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

matias = {
    'first_name': 'Matias',
    'last_name': 'Turkulainen',
    'age': 27,
    'country': 'Finland',
    'is_marred': False,
    'skills': ['Python', 'Coffee', 'Cycling'],
    'address': {
        'street': 'Riihitie 12 A 16',
        'zipcode': '00330'
    }
}
ben = {
     'first_name': 'Ben',
     'last_name': 'Armstrong',
     'age': 24,
     'country': 'Austria',
     'is_marred': True,
     'skills': ['Python', 'Coffee', 'Cycling', 'MongoDB', 'Node'],
     'address': {
         'street': 'Bachlerstrasse 44',
         'zipcode': '8046'
     }
 }

minna = {
      'first_name': 'Minna',
      'last_name': 'Heim',
      'age': 22,
      'country': 'Austria',
      'is_marred': True,
      'skills': ['Python', 'Coffee', 'Cycling', 'MongoDB', 'Node','React'],
      'address': {
          'street': 'Somewhere in St. Gallen, or Zurich depending on the day.',
          'zipcode': 'Mrs.WorldWide'
      }
  }

The_Gang = [matias, ben, minna]
def check_this_persons_skillz(person):
    print(f"Let's check {person['first_name']} skills!")
    if 'skills' in person:
        num_skills = len(person['skills'])
        middle_skill = num_skills//2
        print(f"\tThis person has skills, {person['first_name']}'s middle skill is {person['skills'][middle_skill]}")
        if 'Python' in person['skills']:
            print(f"\t{person['first_name']} knows Python!")
            if len(person['skills']) == 2 and 'Node' in person['skills'] and 'React' in person['skills']:
                print(f"\tWhozie, {person['first_name']} has no other skills besides Front End Developerment! What a nerd.")
            elif 'Node' in person['skills'] and  'Python' in person['skills'] and  'MongoDB' in person['skills'] and not 'React' in person['skills']:
                print(f"\tWhozie, {person['first_name']} is a Back End Developer! You can DeVeLoP mY BaCkEnD any day of the week, wink wink.")
            elif  'Node' in person['skills'] and  'React' in person['skills'] and  'MongoDB' in person['skills']:
                print(f"\tGyyat! My boi {person['first_name']} is a FuLl StAcK DeVeLoPeR!")
            else:
                print(f"\tWhadaheel bruv got secret skills.")
                print("\tUnknown title")
    else:
        print("\tThis person has no skills")

for person in The_Gang:
    check_this_persons_skillz(person)
