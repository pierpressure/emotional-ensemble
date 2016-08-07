import csv
import os

with open('songs.csv', 'rb') as csvfile:
	songreader = csv.reader(csvfile, delimiter=',')
	for row in songreader:
		new_name = os.path.splitext(row[0])[0] + " Trimmed.mp3"
		command = "ffmpeg -y -loglevel panic -i '{}' -ss {} -t 10 '{}'".format(row[0], row[1].strip(), new_name) 
		print command
		os.system(command)
		