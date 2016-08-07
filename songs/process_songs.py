import csv
import os

with open('songs.csv', 'rb') as csvfile:
    songreader = csv.reader(csvfile, delimiter=',')
    for row in songreader:
        fname, start_time = row
        new_name = os.path.splitext(fname)[0] + " Trimmed.mp3"
        command = "ffmpeg -y -loglevel panic -i '{}' -ss {} -t 10 '{}'".format(
                fname, start_time.strip(), new_name)
        print(command)
        os.system(command)
