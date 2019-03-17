import pygame as pg
import sys


class player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('platformerArtDeluxe/Player/p1_jump.png').convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()

    def move_right(self):
        self.rect.x += 10


# Under opstart
pg.init()
game_w = 800
game_h = 450
game_screen = pg.display.set_mode((game_w, game_h))

# Farver
black = (0, 0, 0)
blue = (0, 0, 255)

# Sprites
all_sprites = pg.sprite.Group()
player1 = player()
player2 = player()
all_sprites.add(player1)
all_sprites.add(player2)

# Game loop
exit_game = False
while not exit_game:

    # Input-behandling (events)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit_game = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                player1.move_right()
            if event.key == pg.K_d:
                player2.move_right()

    # Tegn
    game_screen.fill(blue)
    all_sprites.draw(game_screen)

    # Efter alt er tegnet, opdateres skærmen
    pg.display.update()

pg.quit()
sys.exit()
