import pygame
from pygame.locals import *

import gamelib
from elements import Player

class DarkMaze(gamelib.SimpleGame):

    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    checkKey = "K_tmp"
    key="K_tmp"
    def __init__(self):
        self.total =0
        self.start_time=0
        self.endgame = False
        super(DarkMaze, self).__init__('darkMaze', DarkMaze.BLACK)
        self.player = Player(x = 225, #pixel x-axis
                             y = 425, #pixel y-axis
                             cols = 4, #cols
                             rows = 8, #rows
                             color = DarkMaze.WHITE,
                             radius = 20,
                             maze = [[10,10,10,10,10, 0,10,10,10,10],
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
                                     [10,10,10,10,10,10,10,10,10,10]])

    def init(self):
        #pygame.time.Clock().tick()
        #print self.start_time
        super(DarkMaze, self).init()
        self.start_time=self.clock.get_time()/1000.0

    def update(self):
        if self.is_key_pressed(K_UP) and self.endgame==False:
            self.player.move_up()
            self.key="K_UP"
        elif self.is_key_pressed(K_DOWN) and self.endgame==False:
            self.player.move_down()
            self.key="K_DOWN"
        elif self.is_key_pressed(K_LEFT) and self.endgame==False:
            self.player.move_left()
            self.key="K_LEFT"
        elif self.is_key_pressed(K_RIGHT) and self.endgame==False:
            self.player.move_right()
            self.key="K_RIGHT"
        self.total += self.clock.get_time()/1000.0
        if self.player.i == 5 and self.player.j == 0 and self.endgame==False :
            #pygame.time.Clock().tick()
            #self.end_time=pygame.time.Clock().get_time()
            #print self.start_time,self.end_time
            self.show_time = self.total - self.start_time
            self.time_image = self.font.render("Time = %d" % self.show_time, 0,DarkMaze.WHITE)
            self.endgame = True

    def render(self, surface):
        self.player.render(surface)
        status,color = self.player.getStatus()
        if status==True and self.key != self.checkKey:
            self.checkKey = self.key
            self.player.drawColor(surface,color)
            self.player.setStatus(False,0)
        if self.endgame == True:
            surface.blit(self.time_image,(0,0))

def main():
    game = DarkMaze()
    game.run()

if __name__ == '__main__':
    main()