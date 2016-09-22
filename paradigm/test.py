import pygame
import pygame.mixer
from time import sleep
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("../songs/test.wav")
# print ""
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
	sleep(1)
print "done"