# functions
from data.countriesdata import country_info
import day_6
import matplotlib.pyplot as plt

# function with arbitrary number of arguments


def sums(*nums: int) -> int:
    total = 0
    for num in nums:
        total += num
    return total


sums(1, 2, 3, 4, 5, 6, 7, 8)

# function in another -> not recursion
# You can pass functions around as parameters


def square_number(n):
    return n * n


def do_something(f, x):
    return f(x)


# print(do_something(square_number, 3))

day_6.create_randint(1, 24, 3)

# 8: Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.


def print_list(l: list):
    for i in l:
        print(i)


letters = ['a', 'b', 'c', 'd']
# print_list(letters)

# 17: Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number


def factorial(number: int) -> int:
    val = 1
    for i in reversed(range(1, number+1)):
        # print(i)
        val *= i

    return val


# fac = factorial(5)
# print(fac)

# 24:
'''Go to the data folder and access the countries-data.py file.
Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
'''


def most_spoken_langs():
    d = dict()
    languages_list = [country['languages'] for country in country_info]
    # add to dictionary: key: language, value: number of appearances
    for languages in languages_list:
        for language in languages:
            # print(language)
            if language in d:
                d[language] += 1
            else:
                d[language] = 1
    # transform dictionary to list
    l = list(d.items())
    l = sorted(l, key=lambda x: x[1], reverse=True)
    return l


msl = most_spoken_langs()
# print(msl) # [('English', 91), ('French', 45), ('Arabic', 25), ('Spanish', 24), ('Portuguese', 9), ('Russian', 9), ('Dutch', 8), ('German', 7), ('Chinese', 5), ('Serbian', 4), ('Swahili', 4), ('Italian', 4), ('Swedish', 3), ('Albanian', 3), ('Croatian', 3), ('Norwegian', 3), ('Uzbek', 2), ('Turkmen', 2), ('Samoan', 2), ('Guaraní', 2)]

# interesting progression of languages spoken, plot this? is it exponential decay?
# extract all 2nd value in each tuple

m = [x[1] for x in msl]
print(m)
plt.plot(m)
plt.show()
# looks like exponential decay


def most_populated_countries():
    l = []
    for country in country_info:
        t = tuple()
        popu = country['population']
        name = country['name']
        t = (name, popu)
        l.append(t)
    ls = sorted(l, key=lambda x: x[1], reverse=True)
    return ls[:20]


# mpc = most_populated_countries()
# print(mpc)
