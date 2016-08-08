import pygame
from pygame.locals import *
from constants import *
import time
from csv_collector import CSVCollector
from generate import get_songs, write_songs

pygame.init()
pygame.mouse.set_visible(False)

from screen import screen
from drawstuff import *

study_time = int(time.time())
print(study_time)

eeg_fname='../data/eeg_{}.csv'.format(study_time)

songs = get_songs()
write_songs(songs, study_time)

collector = CSVCollector(port='/dev/ttyUSB0', fname=eeg_fname)

collector.start()
collector.tag(0)
time.sleep(4)

def check_for_escape():
    while True:
        event = pygame.event.poll()
        if event.type == 0:
            return False
        elif event.dict.get('key', -1) == K_ESCAPE:
            return True

def finish_stuff(early=False):
    return

collector.tag('focus')
focus_slide()
time.sleep(4)

for i, song in enumerate(songs):

    collector.tag(os.path.basename(song))
    length = audio_slide(song)
    # collector.tag(word)
    time.sleep(length)

    if check_for_escape():
        finish_stuff(early=True)
        # collector.stop()
        exit()

    collector.tag('focus')
    focus_slide()
    # collector.tag('focus')
    time.sleep(7)

    if check_for_escape():
        finish_stuff(early=True)
        # collector.stop()
        exit()
