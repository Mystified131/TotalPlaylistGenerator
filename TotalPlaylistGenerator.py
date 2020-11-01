#This code imports the necessary modules.

import random
import os
import datetime

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

oustr = "TotalPlayList" + tim + ".m3u"

srchstr = 'E:\\OriginalAudio\\Songs'

outfile = open(oustr, "w")

print("")

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".mp3") or filepath.endswith(".wav") or filepath.endswith(".ogg") :
            outfile.write(filepath + '\n')
            print(filepath)

outfile.close()

print("")

print("Your playlist may be found in the same folder as this code.")


## THE GHOST OF THE SHADOW ##
