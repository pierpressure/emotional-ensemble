#!/usr/bin/env python2

import glob
import random

SONGS = glob.glob('../songs/*Volume.wav')

def get_songs():
    songs = list(SONGS)
    random.shuffle(songs)
    return songs

def write_songs(songs, study_time):
    fname = '../data/songs_{}.csv'.format(study_time)
    with open(fname, 'w') as f:
        f.write('\n'.join(songs))
