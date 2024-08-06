# Largest Odd Number in string
import day_6
day_6.create_randint(1, 10000, 1)


def largest_odd_number(number: str):
    for i, value in enumerate(reversed(number)):
        if not int(value) % 2 == 0:  # aka if odd
            if i == 0:
                return number
            return number[:-i]
    return ""


# largest_odd_number('24687')

# Two Sum
def two_sums(nums: list[int], target: int):
    for i, val1 in enumerate(nums):
        for j, val2 in enumerate(nums[i+1:]):
            if val2 + val1 == target:
                # print(val1, val2)
                return [i, i+1+j]


ts = two_sums([-3, 4, 3, 90], 0)
# print(ts)
# to get a runtime that is not O(n^2), which it is here, is to create a one pass hash map


# is Palindrome?
# Given an integer x, return true if x is a palindrome, and false otherwise.

def is_palindrome(number: int) -> int:
    number = str(number)
    if number.startswith('-'):
        return False
    s = ''
    for i in reversed(number):
        s += i
    if s == number:
        return True
    return False


print(is_palindrome(-121))
