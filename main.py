import pygame
from pygame.locals import *

import gamelib
from elements import Block, Player

class DarkMaze(gamelib.SimpleGame):
	BROWN = pygame.Color('brown') #around wall
	RED = pygame.Color('red') #block1
	GREEN = pygame.Color('green') #block2
	BLUE = pygame.Color('blue') #block3
	YELLOW = pygame.Color('yellow') #block4

	def __init__(self):
		super(DarkMaze, self).__init__('Dark Maze', DarkMaze.BROWN)

	def run(self):
		self.init()
		while not self.is_terminated:
			self.update()
			self.render()
			self.__handle_events()

	def __handle_events(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.terminate()

	def init(self):
		pass

	def update(self):
		pass

	def render(self, surface):
		pass

def main():
	game = DarkMaze()
	game.run()


if __name__ == '__main__':
	main()