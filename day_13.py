# List comprehension
from day_6 import create_randint as rand

# is a faster way of creating a list through a sequence, instead of looping through it
name = 'Minna'
lc = [i for i in name]
# print(lc)  # ['M', 'i', 'n', 'n', 'a']

nums = [i for i in range(10)]
# print(nums)

# lambda function
# is a small anonymous function without a name. It can take any number of arguments, but can only have one expression.

# syntax
# def x(param1, param2, param3): return param1 + param2 + param3
# print(x(arg1, arg2, arg3))

# python3 lintr always corrects this to a normal function, instead of lambda..
# add_two_nums = lambda a, b: a + b
# print(add_two_nums(2, 3))

# or
# print((lambda a, b: a + b)(2, 3))


# lambda inside another function:
def power(x):
    return lambda n: x ** n


cube = power(2)(3)
# print(cube)


# Exercises
rand(1, 7, 3)

# 4: Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]


def abbrev(l: list) -> list:
    new_list = []
    for li in l:
        new_inner_list = []
        for tuple in li:
            country = tuple[0].upper()
            abbrev = country[:3].upper()
            new_inner_list = [country, abbrev, tuple[1].upper()]
        new_list.append(new_inner_list)
    return new_list


a = abbrev(countries)
# print(a) #[['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]


# 5: Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]

l = []
for list in countries:
    for country in list:
        d = dict()
        d.update({'country': country[0]})
        d.update({'city': country[1]})
        l.append(d)

print(l)

# 7: Write a lambda function which can solve a slope or y-intercept of linear functions.
# solve_lin_fun = lambda m, x, b: m * x + b
# print(solve_lin_fun(3,4,2))
# output: 14
