# operators
x = 3
x += 3
x -= 3
# x = 3
x *= 3
# x = 9
x = 9
x // 2  # means 2 fits into 9 4 times
x % 1  # modulo: 4 fits into 1 4 times, no rest, which is the output of using modulo

# new operator -> bitwise AND operator
# means that when looking at the numbers in binary, and stacking them, if both numbers are 1 in the same field the new number (z) = 1 there, if not, aka only one or none = 0
z = 1
z &= 3
# equivalent to z = z & 3
z


# |= is ior in python, meaning in-place or, aka assignment functions as or (one or the other (or both?)) and assigns the new value to the assigned variable
b = {'a', 'b', 'c'}
c = {'d', 'e', 'f'}
b |= c
#  equivalent to b = b | c
b = {'a', 'b', 'c', 'd', 'e', 'f'}
#  so b is the OR of both of these sets, not just b as before, as it would be if we only applied the or operator

# bitwise XOR (not and or but OR - either this or that, not both)
# means that in binary, when you take the OR (and if both, then also 0) and stack the binary numbers of 10 and 2, you get 8
a = 10
a ^= 2
# a = a ^ 2

# bitwise NOT a
~a
# a = -9? how come, if a = 8
# because we show negative in binary with a leading number, where 0 = pos and 1 = negative, and we dont add binary but subtract it

# bitwise shifts (and assign)
d = 2
d <<= 2  # 8
d >>= 2  # 2

# logic operators
d & a  # always take the value of the latter variable?
# not the same thing as above, the one combines the binary (bitwise and) and this one just checks which are true, if both t or f then = true if not then f
d and a
d or a  # if one or the other is true then true, if both true then true

# imp: know the difference between python bitwise- and normal operators


# exercises:
# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

def check_even(number: int):
    if number % 2 == 0:
        print("hooray! this is an even number")
    else:
        print("sorry, this is not an even number")


check_even(6)
