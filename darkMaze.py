import pygame, sys
from pygame.locals import *

WINDOWWIDTH = 400
WINDOWHEIGHT = 550

pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Dark Maze')

array = [[0 for x in range(8)] for x in range(11)]
pygame.draw.rect(Surface, red, Rect, width=10)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()