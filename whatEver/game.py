import pygame,sys
from pygame.locals import *
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
i = 1
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            if(i==255):
                i=1
            i=i+1
            pygame.draw.line(DISPLAYSURF, (255,i,0), (60, 60), (120, 60), 4)
            pygame.display.update()
    pygame.display.update()