# Regular Expressions
import re
import math
from day_6 import create_randint
import collections

# print(dir(math))

# find all
s = 'hello my name is'
l = re.findall('[a,m]', s)  # ['m', 'a', 'm']
# print(l)

# match
txt = 'I love to teach python and javaScript'
# It returns an object with span, and match -> ONLY IF BEGINNING OF STRING
match = re.match('I love to teach', txt, re.I)
# print(match) # <re.Match object; span=(0, 15), match='I love to teach'>

# search
match = re.search('python', txt)
# print(match) # <re.Match object; span=(16, 22), match='python'>
span = match.span()
start, end = span
# print(start, end)  # 0, 15
substring = txt[start:end]
# print(substring)

# sub
sub = re.sub('javascript', 'R', txt, flags=re.I)
# print(sub)

split = re.split(' ', sub)
# print(split)  # ['I', 'love', 'to', 'teach', 'python', 'and', 'R']

# regex pattern in r

regex_pattern = r'[Aa]pple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['Apple', 'apple']


# Exercises:
#  What is the most frequent word in the following paragraph? create function that goes through each word and determines frequency
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'


def word_frequency(text:  str) -> list:
    # string split by ' '
    text = re.sub('[.]', '', text)
    # print(text)
    text = re.split(' ', text)
    # print(text)
    d = dict()
    for i in text:
        if i in d:
            count = d[i]
            count += 1
            d[i] = count
        else:
            d.update({i: 1})
    return sorted(d.items(), key=lambda x: x[1], reverse=True)


wf = word_frequency(paragraph)
# print(wf)

# 2
paragraph = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'


particles = re.findall('-?[0-9]?[0-9]', paragraph)
particles = [eval(i) for i in particles]  # eval notices these are ints?
# print(particles)  # ['-12', '-4', '-3', '-1', '0', '4', '8']

# do this with map?


def max_dist(l: list) -> int:
    d = dict()
    for i in l:
        for j in l[i+1:]:
            dist = i - j
            d[dist] = i, j
    # print(d.keys())
    return max(abs(k) for k in d.keys())


m = max_dist(particles)
# print(m)


# 3 Write a pattern which identifies if a string is a valid python variable

def is_valid_variable(variable: str) -> bool:
    if re.match('^[0-9]', variable):
        return False
    if '-' in variable:
        return False
    return True


i = is_valid_variable('1-hi')
# print(i)

# 4 Clean the following text. After cleaning, count three most frequent words in the string.

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''


def most_frequent_words(text: str) -> list:
    # keep only words
    words = re.sub('[^a-zA-Z ]', '', text)
    words = re.split(' ', words)
    # print(words)
    words = collections.Counter(words)
    s = sorted(words.items(), key=lambda x: x[1], reverse=True)
    # s = sorted(words, key=words.get, reverse=True)
    return s[:10]


# [('I', 3), ('a', 2), ('teacher', 2), ('and', 2), ('teaching', 2)]
# m = most_frequent_words(clean)
# print(m)
