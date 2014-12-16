import pygame
from pygame.locals import *

class SimpleGame(object):

	def __init__(self,
				 title,
				 background_color,
				 window_size = (407, 560), 
				 fps = 60):
		self.title = title
		self.window_size = window_size
		self.fps = fps
		self.is_terminated = False

	def terminate(self):
		self.is_terminated = True

	def game_init(self):
		pygame.init()
		self.surface =pygame.display.set_mode(self.window_size)
		pygame.display.set 

	def init(self):
		self.game_init()
