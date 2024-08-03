# lists
# a list is a collection of different data types that is immutable (unchangeable)

# create a list & important functions
import random as rd
tup = tuple()
tup = (1, 2, 3, 4, 5, 6, 7)

tup.index(2)  # at position 1
tup.count(2)  # once
len(tup)  # 7

# slicing, counting, etc. just like with lists

# transforming lists
tup = list(tup)
# print(tup)


# create a function that assigns random numbers 3 times
def create_randint(start, end, rep):
    l = []
    for i in range(rep):
        int = rd.randint(start, end)
        l.append(int)
    return l


# do random exercises
create_randint(1, 12, 3)

# 9: Slice out the middle item or items from the food_stuff_lt list.

food_stuff_lt = ['apples', 'rotten', 'right', 'to', 'the', 'core']


def get_middle(list):
    if len(list) % 2 == 0:
        second = len(list) / 2
        first = second - 1
        return int(first), int(second)
    else:  # len(list) % 2 != 0
        first = len(list) // 2
        return first


mid = get_middle(food_stuff_lt)
# determine how to input 2 vs 1....

# function remove at index


def remove_at_index(list, index):
    if isinstance(index, int):
        return list[:index] + list[index+1:]

    else:  # tuple
        l = list  # need to feed the list of the one prev. removed list into the next one
        for i in index:  # element in tuple
            l = remove_at_index(l, i)
    return l


new_list = remove_at_index(food_stuff_lt, mid)
# print(new_list)
# ['apples', 'rotten', 'to', 'core']

# 10: Slice out the first three items and the last three items from food_staff_lt list
food_stuff_lt = ['apples', 'rotten', 'right', 'to', 'the', 'core']
food_stuff_lt += 'kamala', 'harris'

food_stuff_lt = food_stuff_lt[3:]
food_stuff_lt = food_stuff_lt[:-3]
# print(food_stuff_lt)


# 12:
'''Check if an item exists in tuple:
Check if 'Estonia' is a nordic country

Check if 'Iceland' is a nordic country
'''

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
est = 'Estonia' in nordic_countries
est
ice = 'Iceland' in nordic_countries
ice
