"""
Calculate the value of pi using different formulas.

author: Thomas Lolk Schmidt
email: thomaslolkschmidt@gmail.com
date: 25mar2017
"""

import matplotlib.pylab as pl


def leibniz_formula(iterations):
    pi_leibniz = 0
    for k in range(iterations):
        pi_leibniz += 4*(-1)**k/(2*k + 1)

    return pi_leibniz


def my_factorial(k):
    """
    My own factorial function. We could use the math module instead.
    """
    if k == 0:
        factorial_k = 1
    else:
        factorial_k = 1
        for i in range(k):
            factorial_k *= i+1

    return factorial_k


def efficient_formula(iterations):
    pi_efficient = 0
    for k in range(iterations):
        pi_efficient += 2*(2**k * my_factorial(k)**2)/(my_factorial(2*k + 1))

    return pi_efficient


pi = 3.141592653589793
plot_iterations = 10

# Print pi from online source: http://www.piday.org/million/
print("pi_online    = %.15f" % pi)

# Using Leibniz formula for pi: https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
pi_leibniz = [None]*plot_iterations
for i in range(plot_iterations):
    pi_leibniz[i] = leibniz_formula(i)

print("pi_leibniz   = %.15f" % pi_leibniz[-1])

# Efficient formula for pi: https://en.wikipedia.org/wiki/List_of_formulae_involving_%CF%80
pi_efficient = [None]*plot_iterations
for i in range(plot_iterations):
    pi_efficient[i] = efficient_formula(i)

print("pi_efficient = %.15f" % pi_efficient[-1])

# Plot the convergence
pl.plot(pi_leibniz, 'b', label='Leibniz')
pl.plot(pi_efficient, 'r', label='Efficient')
pl.hlines(pi, 0, plot_iterations, colors='gray', linestyle='dotted')
pl.xlabel("Iterations")
pl.ylabel("pi")
pl.legend(loc='lower right')
