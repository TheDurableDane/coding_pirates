"""
Sum of natural numbers

author: Thomas Lolk Schmidt
email: thomaslolkschmidt@gmail.com
date: 25mar2017
"""


def add_integers(n, N):
    if n > N:
        return "n can not be larger than N, you n00b!"
    elif n == N:
        return n
    else:
        return n + add_integers(n+1, N)


n = 1
N = 100

# Easy mode
my_sum1 = sum(range(n, N+1))
print("sum = ", my_sum1)

# Loop mode
my_sum2 = 0
for i in range(n, N+1):
    my_sum2 += i
print("sum = ", my_sum2)

# Recursive mode
my_sum3 = add_integers(n, N)
print("sum = ", my_sum3)
