#This code imports the necessary modules.

import os
import datetime

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

srchstr = 'C:\\Users\\mysti\\Coding\\TotalPlaylistGenerator\\'

print("")

content = []

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".m3u"):

            infile = open(file, "r")

            plist = infile.readline()
            while plist:
                if "download" in plist:
                    content.append(plist.strip())
                plist = infile.readline()
            
            infile.close()

            print("")
            print(filepath)

oustr = "TotalPlayList" + tim + ".txt"

outfile = open(oustr, "w")   

for elem in content:

    outfile.write(elem + '\n')

outfile.close()

print("")

print("Your playlist may be found in the same folder as this code.")


## THE GHOST OF THE SHADOW ##
