"""
Find square root of number using Newton's method

author: Thomas Lolk Schmidt
email: thomaslolkschmidt@gmail.com
date: 25mar2017
"""

import math


def my_sqrt(n):
    epsilon = 0.0001                # precision
    my_sqroot = [3.90234, 5.902]    # "random" starting points
    i = 1
    while abs(my_sqroot[i] - my_sqroot[i-1]) > epsilon:
        my_sqroot.append(my_sqroot[i] - (my_sqroot[i]**2 - n)/(2*my_sqroot[i]))
        i += 1

    return my_sqroot[-1]


# Find square root of this number
n = 10

# Compare build-in function and my function
print("   sqrt(%.3f) = %.20f" % (n, math.sqrt(n)))
print("my_sqrt(%.3f) = %.20f" % (n, my_sqrt(n)))
