import pygame, sys
from pygame.locals import *

maze = [[10,10,10,10,10,10,10,10,10,10],
        [10, 0, 1, 3, 3, 0, 4, 4, 4,10],
        [10, 0, 1, 3, 3, 0, 0, 3, 4,10],
        [10, 1, 1, 2, 2, 2, 0, 3, 4,10],
        [10, 4, 0, 0, 0, 0, 0, 2, 2,10],
        [10, 4, 0, 3, 3, 4, 1, 1, 2,10],
        [10, 4, 0, 2, 0, 0, 0, 4, 2,10],
        [10, 4, 0, 2, 0, 1, 1, 4, 2,10],
        [10, 4, 0, 2, 0, 0, 1, 4, 3,10],
        [10, 1, 0, 2, 2, 0, 1, 0, 3,10],
        [10, 1, 0, 0, 0, 0, 0, 0, 3,10],
        [10, 1, 1, 1, 1, 3, 3, 3, 3,10],
        [10,10,10,10,10,10,10,10,10,10]]


WHITE = pygame.Color('white')
RED = pygame.Color('red')
GREEN = pygame.Color('green')
BLUE = pygame.Color('blue')
YELLOW = pygame.Color('yellow')
BROWN = pygame.Color('brown')

pygame.init()
surface = pygame.display.set_mode((400, 550))

for y in range(11):
	for x in range(8):
		if maze[y][x] == 0:
			pygame.draw.rect(surface, WHITE, pygame.Rect(x*50, y*50, 50, 50), 0)
		elif maze[y][x] == 1:
			pygame.draw.rect(surface, RED, pygame.Rect(x*50, y*50, 50, 50), 0)
		elif maze[y][x] == 2:
			pygame.draw.rect(surface, GREEN, pygame.Rect(x*50, y*50, 50, 50), 0)
		elif maze[y][x] == 3:
			pygame.draw.rect(surface, YELLOW, pygame.Rect(x*50, y*50, 50, 50), 0)
		elif maze[y][x] == 4:
			pygame.draw.rect(surface, BLUE, pygame.Rect(x*50, y*50, 50, 50), 0)	
		elif maze[y][x] == 10:
			pygame.draw.rect(surface, BROWN, pygame.Rect(x*50, y*50, 50, 50), 0)

pygame.draw.rect(surface, YELLOW, pygame.Rect(100, 50, 20, 50), 0)

pygame.draw.circle(surface, pygame.Color('purple'), (175,375), 20, 0)

pygame.display.update()

while True:
	pass
