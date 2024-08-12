# higher order functions

# function as parameters
from day_6 import create_randint as rand
from data.countries import countries
from data.countriesdata import country_info


def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<


def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation


result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
# print(result)       # 15
# we take one function as an input for another

# function as a return value


def square(x):          # a square function
    return x ** 2


def cube(x):            # a cube function
    return x ** 3


def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)


def higher_order_function(type):  # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute


result = higher_order_function('square')
# print(result(3))       # 9
result = higher_order_function('cube')
# print(result(3))       # 27
result = higher_order_function('absolute')
# print(result(-3))      # 3

# here function isnt a parameter, but an option?


# python closures
# Python allows a nested function to access the outer scope of the enclosing function.
def add_ten():
    ten = 10

    def add(num):
        return num + ten  # how does it recognise ten as a variable?
    return add


closure_result = add_ten()
# print(closure_result(5))  # 15
# print(closure_result(10))  # 20

# python decorators
# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.

# Normal function


def greeting():
    return 'Welcome to Python'


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper


g = uppercase_decorator(greeting)
# print(g())          # WELCOME TO PYTHON

# Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper


@uppercase_decorator
def greeting():
    return 'Welcome to Python'


# print(greeting())   # WELCOME TO PYTHON
# i dont get the second one yet?

# built in higher order functions
# map() function is a built-in function that takes a function and iterable as parameters
numbers = [1, 2, 3, 4, 5]  # iterable


def square(x):
    return x ** 2


numbers_squared = map(square, numbers)
# print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x: x ** 2, numbers)
# print(list(numbers_squared))    # [1, 4, 9, 16, 25]

# filter()
# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable


def is_even(num):
    if num % 2 == 0:
        return True
    return False


even_numbers = filter(is_even, numbers)
# print(list(even_numbers))       # [2, 4]

# reduce()
numbers_str = ['1', '2', '3', '4', '5']  # iterable


def add_two_nums(x, y):
    return int(x) + int(y)


# total = reduce(add_two_nums, numbers_str)
# print(total)    # 15 -> adds all numbers together?

# exercises
rand(1, 24, 3)


# 1 : Explain the difference between map, filter, and reduce.
''' the difference between these 3 lies in the return, they each apply functions to arguments
map iterates a function over another data storing element (returns all)
filter applies a function over function, and only keeps the elements which remain after the function was applies
reduce applies the function onto the arguments, but only returns the result'''

# 19 : Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.


def countries_starting_with(letter: str) -> list:
    l = []
    for i in countries:
        if i.startswith(letter):
            l.append(i)
        else:
            pass
    return l


c = countries_starting_with('A')
# print(c)

''' 24 : Use the countriesdata.py file and  follow the tasks below:
Sort countries by name, by capital, by population
Sort out the ten most spoken languages by location. -> dont have location in countriesdata?
Sort out the ten most populated countries.'''

# sort countries by name, capital and population

# create sort function


def sort_by_key(string: str, n: int) -> list:
    '''function that sorts the countries_info list by key'''
    d = dict()
    for country in country_info:
        key = country['name']
        value = country[string]
        d.update({key: value})
        # print(d)
    # sort d by value
    sorted_dict = sorted(d.items(), key=lambda item: item[1], reverse=True)
    # print(type(sorted_dict))
    if string == 'name':
        l = []
        for i in sorted_dict:
            l.append(i[1])
        return l[:n]
    return sorted_dict[:n]


s = sort_by_key('name', 5)
print(s)

# now we can do:
sort_by_key('population', 3)
sort_by_key('name', 3)
sort_by_key('capital', 3)

# or we can do:


def sort_by_category(function, category: str, n: int):
    '''function which executes inputed function and arguments'''
    res = function(category, n)
    return res


s = sort_by_category(sort_by_key, 'population', 5)
print(s)
