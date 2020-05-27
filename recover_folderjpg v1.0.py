#!/usr/bin/python
import os
import re
import taglib
import shutil
rootpath = "/Volumes/Ultra_Downloads/Albums"
recoverpath="/Users/dagmar/Downloads/Albums/covers/"
#print rootpath

def copyFile(src, dest):
    try:
        shutil.copyfile(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror)

def recover_cover(folder_dir, filename):
    print "cover picture found in "+ (os.path.join(folder_dir,filename))
    list_dir=os.listdir(folder_dir)
    for files in list_dir:
        mp3 = re.search(r'mp3|m4a',files,re.I)
        if mp3:
            song = taglib.File(folder_dir+'/'+files)
            mytag = song.tags
            if "ALBUMARTIST" in mytag:
                albumartist= mytag["ALBUMARTIST"]
            else:
                albumartist= mytag["ARTIST"]
            album=mytag["ALBUM"]
            newfile= recoverpath+albumartist[0]+" - "+ album[0]+".jpg"
            break
    copyFile(os.path.join(folder_dir,filename),newfile)
    
    
for root, dirs, files in os.walk(rootpath, topdown=True):
    sema = True
    print "searching in " + root
    for filename in files:
        searchObj = re.search(r'folder.jpg|cover.jpg',filename,re.I)
        if searchObj and (sema == True):
            recover_cover(root,filename)
            sema = False
