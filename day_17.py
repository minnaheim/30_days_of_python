# Exception Handling
# we use try except to create more elegant error handlings, with more detailed results
# for this, we reuse functions from previous modules
from day_14 import countries_starting_with
from data.countries import countries

# define exceptions:


class LowerCaseException(Exception):
    pass


class TwoLetterException(Exception):
    pass


def countries_by_letters(letter: str) -> None:
    try:
        c = countries_starting_with(letter)
        if not c:  # is the simplified version of: c == []
            raise LowerCaseException
        if len(c) > 1:
            raise TwoLetterException
        print(c)
    except LowerCaseException:
        print("Please use only Upper Case Letters, i.e. transform string .isupper()")
    except TwoLetterException:
        print("please only put one Letter into the function")


hey = countries_by_letters('ab')
# print(hey)

# Unpacking Elements in Python


def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e


lst = [1, 2, 3, 4, 5]
# print(sum_of_five_nums(*lst))  # 15

numbers = range(2, 7)  # normal call with separate arguments
# print(list(numbers))  # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
# print(numbers)      # [2, 3, 4, 5,6]

# unpacking dictionaries


def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'


dct = {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
# Asabeneh lives in Finland, Helsinki. He is 250 years old.
print(unpacking_person_info(**dct))


# we can use this */** not only to unpack but also to pack, when we dont know how many variables are used as an input in the function/ multiple amounts can be used
# like above.
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s


# print(sum_all(1, 2, 3))             # 6
# print(sum_all(1, 2, 3, 4, 5, 6, 7))  # 28


# spreading in python
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
# print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]

# enumerate: saves indexes and values together in a tuple, in case we need both in the function
for index, i in enumerate(countries):
    if i == 'Switzerland':
        print(f'The country {i} has been found at index {index}')

# zip: combine lists by looping through them,
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit': f, 'veg': v})

# [{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, {'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}, {'fruit': 'lime', 'veg': 'Carrot'}]
# print(fruits_and_veges)

# Exercise:
# Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
names = ['Finland', 'Sweden', 'Norway',
         'Denmark', 'Iceland', 'Estonia', 'Russia']
nordic_countries, es, ru = names[:4], names[5], names[6]
# print(nordic_countries, es, ru)
