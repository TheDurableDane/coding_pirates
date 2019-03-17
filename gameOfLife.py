"""
Game of Life

author: Thomas Lolk Schmidt
email: thomaslolkschmidt@gmail.com
date: 29jan2017
"""

import numpy as np
import sys
import matplotlib.pylab as plt


def numberOfNeighbours(world, row, col):
    """
    Find the number of alive neighbours for a given cell.
    """
    world_v, world_h = world.shape

    world_temp = np.zeros((world_v+2, world_h+2))
    world_temp[1:-1, 1:-1] = world
    neighbourhood = world_temp[row:row+3, col:col+3]
    neighbourhood[1, 1] = 0

    return np.sum(neighbourhood)


def newCondition(n, condition):
    """
    Given the number of alive neighbours n and the current condition of the
    cell, compute the new condition of the cell (dead/alive, 0/1) according to
    the rules of the game.
    """
    if condition == 0:
        if n == 3:
            return 1
        else:
            return 0
    elif condition == 1:
        if n < 2:
            return 0
        elif n > 3:
            return 0
        else:
            return 1
    else:
        print(condition)
        print("\nCondition must be either 0 or 1.\n")
        sys.exit()


def getCrossWorld(world_v, world_h):
    min_dim = min(world_v, world_h)
    world = np.zeros((world_v, world_h))
    world[:min_dim, :min_dim] = np.fliplr(np.eye(min_dim)) + np.eye(min_dim)

    return world


def getRandomWorld(world_v, world_h):
    np.random.seed(27)

    return np.round(np.random.rand(world_v, world_h))


def getPlusWorld(world_v, world_h):
    world = np.zeros((world_v, world_h))
    world[:, int(np.round(world_h/2))] = 1
    world[int(np.round(world_v/2)), :] = 1

    return world


def getCheckersWorld(world_v, world_h):
    world = np.zeros((world_v, world_h))
    world[::2, ::2] = 1
    world[1::2, 1::2] = 1

    return world


# Initialize game
world_v = 50       # vertical size
world_h = 50       # horizontal size
total_time = 40    # number of iterations in simulation

world = np.zeros((world_v, world_h, total_time), dtype=int)
world[:, :, 0] = getCheckersWorld(world_v, world_h)
plt.axis('off')
plt.imshow(-1*world[:, :, 0]+1, interpolation='none', cmap='gray')
plt.pause(5)

# Start game
for t in range(1, total_time):
    for row in range(world_v):
        for col in range(world_h):
            n = numberOfNeighbours(world[:, :, t-1], row, col)
            world[row, col, t] = newCondition(n, world[row, col, t-1])

    # Plot world
    plt.clf()
    plt.imshow(-1*world[:, :, t]+1, interpolation='none', cmap='gray')
    plt.title("t = %d" % t)
    plt.axis('off')
    plt.pause(0.05)
