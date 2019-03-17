#!/home/thomas/miniconda3/bin/python3

import pygame as pg
import numpy as np
import matplotlib.pyplot as plt
import sys
import time

# Initialize pygame
pg.init()

# Define colors [R, G, B]
black = (0, 0, 0, 255)
white = (255, 255, 255, 255)
red = (255, 0, 0, 255)

# Setup the screen
maze = plt.imread('../maze_solving/mazes/small.png')[:, :, 0]
h_maze, w_maze = maze.shape
scale = 40

width = scale*w_maze
height = scale*h_maze
game_screen = pg.display.set_mode((width, height))
pg.display.set_caption("The aMAZEing game")

# Other definitions
x = scale*np.where(maze[0, :] == 1)[0][0]
y = 0
y_end = scale*h_maze - scale
start_time = time.time()

# The core of the game
exit_game = False
while not exit_game:
    # Check for key events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit_game = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT and game_screen.get_at((x-scale, y)) == white:
                x -= scale
            elif event.key == pg.K_RIGHT and game_screen.get_at((x+scale, y)) == white:
                x += scale
            elif event.key == pg.K_UP and y != 0 and game_screen.get_at((x, y-scale)) == white:
                y -= scale
            elif event.key == pg.K_DOWN and game_screen.get_at((x, y+scale)) == white:
                y += scale

    if y == y_end:
        print("Gratz, you've completed the maze in {0} seconds.".format(np.round(time.time() - start_time, decimals=2)))
        exit_game = True

    # Draw screen
    game_screen.fill(white)
    
    for c in range(w_maze):
        for r in range(h_maze):
            if maze[r, c] == 0:
                pg.draw.rect(game_screen, black, [c*scale, r*scale, scale, scale])
        
    pg.draw.rect(game_screen, red, [x, y, scale, scale])

    pg.display.update()

# Shutdown the game
pg.quit()
sys.exit()
