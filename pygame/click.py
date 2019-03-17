import pygame as pg
import numpy as np
import sys
import time


# Initialization
pg.init()
game_w = 800
game_h = 450
game_screen = pg.display.set_mode((game_w, game_h))
pg.display.set_caption('Sir Click-a-Lot')
score = 0
font = pg.font.SysFont('Arial', 30)
start_time = None
total_time = 10

# Button specs
btn_w = 50
btn_h = 50

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
light_gray = (150, 150, 150)
red = (255, 0, 0)

exit_game = False
while not exit_game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit_game = True
        if event.type == pg.MOUSEBUTTONDOWN and game_screen.get_at(pg.mouse.get_pos()) == light_gray:
            score += 1
            if start_time is None:
                start_time = time.time()

    game_screen.fill(white)
    pg.draw.rect(game_screen, light_gray, [(game_w - btn_w)*2/3, (game_h - btn_h)/2, btn_w, btn_h])

    # Print score on screen
    text_score = font.render(str(score), True, black)
    game_screen.blit(text_score, (game_w/3, (game_h - text_score.get_height())/2))

    # Print time on screen
    if start_time is not None:
        time_left = np.around(total_time - (time.time() - start_time), decimals=1)
        text_time = font.render(str(time_left) + " sekunder tilbage", True, black)
        game_screen.blit(text_time, ((game_w - text_time.get_width())/2, 10))

        if time_left <= 0:
            exit_game = True
            pg.display.update()
            time.sleep(3)

    pg.display.update()

pg.font.quit()
pg.quit()
sys.exit()
