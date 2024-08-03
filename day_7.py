# sets

# creating a set
import day_6
st = set()
type(st)  # set
s = {}  # this is a dictionary, only if you dont assign key and value is it a set
st = {'item1', 'item2', 'item3', 'item4'}
type(st)  # set

#  useful functions for sets
len(st)  # 4
st.add('item5')  # add adds the element right in the middle...
st.update(['item6', 'item7'])
print(st)

s = {'hello', 'my', 'name', 'is', 'brat'}
s.update(st)
print(s)

fruits = {'banana', 'orange', 'mango', 'lemon'}  # adds alphabetically?
fruits.add('lime')
print(fruits)
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits.update(vegetables)
print(fruits)  # why is the new list so randomly assorted?


# remove (items)
fruits.pop()
# if doesn't work (already has been removed) just pass over it
try:
    fruits.remove('lemon')
except KeyError:
    pass
fruits.clear()  # just an empty set
del vegetables  # not defined

# math operations with sets
s.union(st)
print(s)  # difference between update and union?
# finds common values.. {'item6', 'item2', 'item4', 'item1', 'item3', 'item5', 'item7'}
s.intersection(st)
s.issubset(st)  # false
s.issuperset(st)  # true
# {'brat', 'my', 'hello', 'is', 'name'} -> gives elements in s but not in st
s.difference(st)
s.symmetric_difference(st)  # -> gives elements in either s or st, not in both
# false -> only disjoint if no common items, not the case here.
s.isdisjoint(st)

# set to list, tuple, etc.
s = tuple(s)  # yes and reordered
s = list(s)  # yes, also reordered

print(day_6.create_randint(1, 15, 3))
# why is this not up to date with day_6???

# 1: find the length of the set
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
len(it_companies)  # 7
# 3:Insert multiple IT companies at once to the set it_companies
it_companies.update(['Nvidia', 'Armstrong Systems'])

# 12:Explain the difference between the following data types: string, list, tuple and set
'''a string is a text of any kind, a list is a collection of data types that is mutable, a tuple is the same as the list but immutable and a set is one data type which is unordered, and immutable, but things can be added '''
