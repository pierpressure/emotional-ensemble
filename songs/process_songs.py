import csv
import os
import re
import os.path

pat_db = re.compile(r'([+\-]?\d+\.\d+) dB')

with open('songs.csv', 'r') as csvfile:
    songreader = csv.reader(csvfile, delimiter=',')
    for row in songreader:
        fname, start_time = row
        fname = fname.strip()
        start_time = start_time.strip()

        fname, start_time = row
        print(fname)

        new_name = os.path.splitext(fname)[0] + " Trimmed.wav"
        new_name_volume = os.path.splitext(fname)[0] + " Trimmed Volume.wav"

        if os.path.exists(new_name_volume):
            continue

        command = "ffmpeg -y -loglevel panic -i '{}' -ss {} -t 10 '{}'".format(
            fname, start_time, new_name)
        print(command)
        os.system(command)

        cmd = "ffmpeg -i '{}'  -af 'volumedetect' -f null /dev/null 2>&1 | grep max_volume".format(new_name)
        output = os.popen(cmd).read()
        groups = pat_db.search(output).groups()
        mean_volume = float(groups[0])
        diff = -5 - mean_volume


        command = "ffmpeg -y -loglevel panic -i '{}'  -af 'volume={:.1f}dB' '{}'".format(
            new_name, diff, new_name_volume)
        print(command)
        os.system(command)
