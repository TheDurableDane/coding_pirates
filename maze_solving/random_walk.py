#!/home/thomas/miniconda3/bin/python3
"""
Simple script to solve perfect mazes.

author: Thomas Lolk Schmidt
email: thomaslolkschmidt@gmail.com
date: 04mar2017
"""

import numpy as np
import matplotlib.pylab as plt
import time


def find_directions(maze, current_position):
    """
    Find the possible direction from the current position, i.e. direction
    where there are no walls.
    """
    directions = np.zeros(4)
    if current_position[0] == 0:        # starting position
        directions[0] = maze[0, current_position[1]+1]
        directions[2] = maze[0, current_position[1]-1]
        directions[3] = maze[1, current_position[1]]
    elif current_position[0] != maze.shape[0]-1:
        directions[0] = maze[current_position[0], current_position[1]+1]
        directions[1] = maze[current_position[0]-1, current_position[1]]
        directions[2] = maze[current_position[0], current_position[1]-1]
        directions[3] = maze[current_position[0]+1, current_position[1]]

    return directions


# Read maze from file
maze_path = plt.imread('mazes/tiny.png')
maze = maze_path[:, :, 0]

# Get basic maze stats
height, width = maze.shape
start = np.where(maze[0, :] == 1)[0][0]
end = np.where(maze[-1, :] == 1)[0][0]

# Solve maze
current_position = [0, start]
maze_path[current_position[0], current_position[1], 1:3] = 0
fig, ax = plt.subplots()
ax.imshow(maze_path, interpolation='none')

time_start = time.time()

while current_position[0] != height-1:
    previous_position = current_position[:]
    directions = find_directions(maze, current_position)

    new_direction = np.random.choice(np.where(directions)[0])

    if new_direction == 0:
        current_position[1] += 1
    elif new_direction == 1:
        current_position[0] -= 1
    elif new_direction == 2:
        current_position[1] -= 1
    elif new_direction == 3:
        current_position[0] += 1

    maze_path[previous_position[0], previous_position[1], 0:2] = 1
    maze_path[current_position[0], current_position[1], 1:3] = 0
    time_current = time.time()
    plt.cla()
    ax.imshow(maze_path, interpolation='none')
    ax.set_title("Seconds in maze: " + str(int(time_current - time_start)))

    plt.pause(0.1)

plt.show(block=True)
print('Labyrinten gennemført på {0} sekunder.'.format(str(int(time_current - time_start))))
