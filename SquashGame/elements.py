import pygame
from pygame.locals import *

BROWN = pygame.Color('brown') #around wall
RED = pygame.Color('red') #block1
GREEN = pygame.Color('green') #block2
BLUE = pygame.Color('blue') #block3
YELLOW = pygame.Color('yellow') #block4
BLACK = pygame.Color('black') #default block
WHITE = pygame.Color('white')

class Player(object):
    checkStatus = False
    color=0
    def __init__(self, x, y, cols, rows, color, radius, maze):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.i = cols
        self.j = rows
        self.maze = maze

    def getStatus(self):
        return self.checkStatus, self.color

    def setStatus(self, check, _color):
        self.checkStatus = check
        self.color = _color

    def move_up(self):
        #print self.maze[self.j - 1][self.i - 1], self.maze[self.j - 1][self.i], self.maze[self.j - 1][self.i + 1]
        #print self.j, self.i
        #print self.maze[self.j + 1][self.i - 1], self.maze[self.j + 1][self.i], self.maze[self.j + 1][self.i + 1]
        if self.maze[self.j - 1][self.i] == 0:
            self.y -= 50
            pygame.time.wait(200)
            self.j -= 1
            #print 'UP',
            #print self.maze[self.j][self.i]
        else:
            self.checkStatus = True
            self.color=self.maze[self.j - 1][self.i]

    def move_down(self):
        #print self.j, self.i
        if self.maze[self.j + 1][self.i] == 0:
            self.y += 50
            pygame.time.wait(200)
            self.j += 1
            #print 'DOWN'
            #print self.maze[self.j][self.i]
        else:
            self.checkStatus = True
            self.color=self.maze[self.j + 1][self.i]


    def move_left(self):
        #print self.j, self.i
        if self.maze[self.j][self.i - 1] == 0:
            self.x -= 50
            pygame.time.wait(200)
            self.i -= 1
            #print 'LEFT'
            #print self.maze[self.j][self.i]
        else:
            self.checkStatus = True
            self.color=self.maze[self.j][self.i - 1]

    def move_right(self):
        #print self.j, self.i
        if self.maze[self.j][self.i + 1] == 0:
            self.x += 50
            pygame.time.wait(200)
            self.i += 1
            #print 'RIGHT'
            #print self.maze[self.j][self.i]
        else:
            self.checkStatus = True
            self.color=self.maze[self.j][self.i + 1]

    def drawColor(self, surface, typeWall):
        for y in range(13):
            for x in range(10):
                if self.maze[y][x] == typeWall:
                    if typeWall == 1:
                        pygame.draw.rect(surface, RED, pygame.Rect(x*50, y*50, 50, 50), 0)
                    elif typeWall == 2:
                        pygame.draw.rect(surface, GREEN, pygame.Rect(x*50, y*50, 50, 50), 0)
                    elif typeWall == 3:
                        pygame.draw.rect(surface, YELLOW, pygame.Rect(x*50, y*50, 50, 50), 0)
                    elif typeWall == 4:
                        pygame.draw.rect(surface, BLUE, pygame.Rect(x*50, y*50, 50, 50), 0)

    def render(self, surface):
        pygame.draw.circle(surface, pygame.Color('purple'), (self.x,self.y), 20, 0)