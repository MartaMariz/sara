import pygame, sys
from settings import *
from tiles import Tile
from level import Level

# Pygame initialization
pygame.init()
# Screen
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)

# Game loop
while True: 
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    level.draw()
    # Update
    # Draw
    pygame.display.flip()
    clock.tick(60)
