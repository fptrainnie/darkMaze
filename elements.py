import pygame
from pygame.locals import *

class Block(object):
	def __init__():
		maze = [[0,1,3,3,0,4,4,4],
				[0,1,3,3,0,0,3,4],
				[1,1,2,2,2,0,3,4],
				[4,0,0,0,0,0,2,2],
				[4,0,3,3,4,1,1,2],
				[4,0,2,0,0,0,4,2],
				[4,0,2,0,1,1,4,2],
				[4,0,2,0,0,1,4,3],
				[1,0,2,2,0,1,0,3],
				[1,0,0,0,0,0,0,3],
				[1,1,1,1,3,3,3,3]]

class Player(object):
	def __init__(self, pos, color, width = 50):
		player_image = pygame.image.load('player.png')
		surface.blit(self.player_image, self.player_position)