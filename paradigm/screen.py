import pygame
from pygame.locals import *
from constants import *

infoObject = pygame.display.Info()
# pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
# if fullscreen_on:
#     screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN)
# else:
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
