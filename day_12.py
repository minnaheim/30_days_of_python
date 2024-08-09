# modules
# A module is a file containing a set of codes or a set of functions which can be included to an application. -> like a configuration file?
import sys
from day_6 import create_randint as rand
import random
from statistics import *
import os
rand(1, 20, 2)


os.getcwd()  # '/Users/minna/Py/30_days_python'
# uses this output for the welcome message
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[0], sys.argv[0]))
# when running this script in commandline "python3 day_12.py Minna 30daysofpython" we get: Welcome Minna. Enjoy  30daysofpython challenge!

# dont quite know how to use the sys library

# print(rand(1, 8, 3))

# 5: Write a function list_of_rgb_colors which returns any number of RGB colors in an array.


def list_of_rgb_colors(n):
    l = []
    for i in range(n):
        a = ()
        r = random.randint(0, 255)
        b = random.randint(0, 255)
        g = random.randint(0, 255)
        a += (r, g, b)
        # print(a)
        l.append(a)
    return l


rgb = list_of_rgb_colors(2)
# print(rgb)


# 7 Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

def shuffle_list(l: list) -> list:
    # print(l)
    random.shuffle(l)
    return l


l = [1, 2, 3, 4, 5, 6, 7, 8]
li = shuffle_list(l)
# print(li)


# 8 Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def butterbrot():
    a = []
    while len(a) < 7:
        n = random.randint(0, 9)
        if n in a:
            pass
        else:
            a.append(n)
    return a


print(butterbrot())
