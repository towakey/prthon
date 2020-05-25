from pygame.locals import *
import pygame
import sys

from PIL import ImageGrab

import datetime

pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("key event")

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_PRINT:
                now = datetime.datetime.now()
                print(now.strftime('%Y%m%d%H%M%S%f'))
                ImageGrab.grab().save(str(now.strftime('%Y%m%d%H%M%S%f'))+".png")
            else:
                print("押されたキー = " + pygame.key.name(event.key))