import pygame as pg
import sys

# Under opstart
pg.init()
game_w = 800
game_h = 450
game_screen = pg.display.set_mode((game_w, game_h))

# Spillet starter her
exit_game = False
while not exit_game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit_game = True

    pg.display.update()

pg.quit()
sys.exit()
