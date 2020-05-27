#!/usr/bin/python
import os
import re
import piexif
import shutil

exif_dict = piexif.load("/Users/dagmar/Pictures/test/DSCF4890-6.JPG")
for ifd in ("0th","GPS","Exif"):
    for tag in exif_dict[ifd]:
        print(piexif.TAGS[ifd][tag]["name"], exif_dict[ifd][tag])

#print (exif_dict["GPS"]["GPSDateStamp"])
