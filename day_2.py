#  day 2:
#  use built in functions:
type('hello world!')
# <class 'str'>
len('hello world!')
# 12
input("What did you eat today?")
sum([2, 3, 4, 5, 6])

# can declare multiple variables in one row
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

# data types
print(type([1, 2, 3, 4]))     # list
print(type({'name': 'Asabeneh', 'age': 250, 'is_married': 250}))    # dict
print(type((1, 2)))                                              # tuple
print(type(zip([1, 2], [3, 4])))                                   # set

# Exercise 2:
'''The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.'''

# r = 30
pi = 3.1415927
r = int(input("What is your desired radius, in int and cm"))
area_of_circle = r**2*pi
print(area_of_circle)
# circum_of_circle = print(2*r*pi)


# OWN ASSIGNMENT - CREATE A FIBONACCI SEQUENCE LOOP
l = [0, 1]
for position in range(9):
    fsum = l[position] + l[position + 1]
    l.append(fsum)
# print(l)


l = []
for position in range(9):
    if position == 0:
        l.append(0)
    elif position == 1:
        l.append(1)
        print(l)
    else:  # position > 1
        fsum = l[position - 1] + l[position - 2]
        l.append(fsum)
# print(l)


# write a function that takes n and spits out the nth fibonacci
def fibonacci_bitch(number: int) -> int:
    """write function

    Args:
        number (int): the nth number

    Returns:
        int: nth fibonacci sequence
    """
    l = [0, 1]
    for position in range(9):
        fsum = l[position] + l[position + 1]
        l.append(fsum)
    return l[number]


fibonacci_bitch(4)
