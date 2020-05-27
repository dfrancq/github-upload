#!/usr/bin/python
import taglib
rootpath = "/Users/dagmar/Downloads/Albums/"

song = taglib.File(rootpath+"Hammerhead.mp3")
mytags = song.tags
for key in mytags:
    print key,": ",mytags[key]