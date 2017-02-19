"""
Dice roll -- Showing the law of large numbers: https://en.wikipedia.org/wiki/Law_of_large_numbers

author: Thomas Lolk Schmidt
email: thomaslolkschmidt@gmail.com
date: 29jan2017
"""

import numpy as np
import matplotlib.pylab as plt


# Get some random numbers
np.random.seed(1)
N = 10000
randomNumbers = np.random.rand(N)
diceRoll = np.ceil(randomNumbers*6)

# Plot histogram to show uniformity
plt.hist(diceRoll, bins=np.arange(1,8)-0.5)
plt.xlabel("Number of eyes on dice")
plt.ylabel("Number of rolls")

# Find the average of the rolls after each new roll
meanDiceRoll = np.zeros(N)
meanDiceRoll[0] = diceRoll[0]

for i in range(1,N):
    meanDiceRoll[i] = np.mean(diceRoll[:i+1])

# Plot average vs numbers of rolls    
plt.figure()
plt.plot(meanDiceRoll)
plt.axhline(y=3.5)
plt.xlabel("Number of dice rolls")
plt.ylabel("Average of dice rolls")
plt.show()