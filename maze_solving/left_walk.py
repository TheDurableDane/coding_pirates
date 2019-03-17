#!/home/thomas/miniconda3/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import time

def find_direction(pre, now):
    """
    pre: previous_position
    now: current_position
    """
    print(pre, now)
    if now[1] - pre[1] == 1:
        return 'right'
    elif now[1] - pre[1] == -1:
        return 'left'
    elif now[0] - pre[0] == 1:
        return 'down'
    elif now[0] - pre[0] == -1:
        return 'up'
    else:
        return 'down'


def find_moves(maze, position):
    possible_moves = []

    if position[0] == 0:
        possible_moves.append('down')
        return possible_moves

    if maze[position[0]-1, position[1]] == 1:
        possible_moves.append('up')
    if maze[position[0]+1, position[1]] == 1:
        possible_moves.append('down')
    if maze[position[0], position[1]-1] == 1:
        possible_moves.append('left')
    if maze[position[0], position[1]+1] == 1:
        possible_moves.append('right')

    return possible_moves


def walk(position, move):
    if move == 'right':
        position[1] += 1
    elif move == 'up':
        position[0] -= 1
    elif move == 'left':
        position[1] -= 1
    elif move == 'down':
        position[0] += 1

    return position, move


# Read maze and get maze stats
maze_path = plt.imread('mazes/logo.png')
maze = maze_path[:, :, 0]

height, width = maze.shape
start = np.where(maze[0, :] == 1)[0][0]
end = np.where(maze[-1, :] == 1)[0][0]

# Initialization
position = [0, start]
maze_path[position[0], position[1], :] = [1, 0, 0]

fig, ax = plt.subplots()
ax.imshow(maze_path, interpolation='none')

time_start = time.time()
while position[0] != height-1:
    previous_position = position[:]

    # Calculate next step
    possible_moves = find_moves(maze, position)

    if len(possible_moves) == 1:
        position, direction = walk(position, possible_moves[0])
    elif direction == 'down':
        if 'right' in possible_moves:
            position, direction = walk(position, 'right')
        elif 'down' in possible_moves:
            position, direction = walk(position, 'down')
        elif 'left' in possible_moves:
            position, direction = walk(position, 'left')
        elif 'up' in possible_moves:
            position, direction = walk(position, 'up')
    elif direction == 'right':
        if 'up' in possible_moves:
            position, direction = walk(position, 'up')
        elif 'right' in possible_moves:
            position, direction = walk(position, 'right')
        elif 'down' in possible_moves:
            position, direction = walk(position, 'down')
        elif 'left' in possible_moves:
            position, direction = walk(position, 'left')
    elif direction == 'up':
        if 'left' in possible_moves:
            position, direction = walk(position, 'left')
        elif 'up' in possible_moves:
            position, direction = walk(position, 'up')
        elif 'right' in possible_moves:
            position, direction = walk(position, 'right')
        elif 'down' in possible_moves:
            position, direction = walk(position, 'down')
    elif direction == 'left':
        if 'down' in possible_moves:
            position, direction = walk(position, 'down')
        elif 'left' in possible_moves:
            position, direction = walk(position, 'left')
        elif 'up' in possible_moves:
            position, direction = walk(position, 'up')
        elif 'right' in possible_moves:
            position, direction = walk(position, 'right')

    # Show path and position
    maze_path[previous_position[0], previous_position[1], :] = [1, 1, 0]
    maze_path[position[0], position[1], :] = [1, 0, 0]

    plt.cla()
    ax.imshow(maze_path, interpolation='none')
    time_current = time.time()
    ax.set_title("Seconds in maze: " + str(int(time_current - time_start)))

    plt.pause(0.1)

plt.show(block=True)
