# Color Sort
# This program renames all png files in a folder to their average hue value
# (c)Thomas Beelen 2016

import numpy as np
import sys
import os
import matplotlib.image as mpimg
import colorsys

# welcome message
os.system('clear')
print "              __                              __ "
print "  _________  / /___  _____   _________  _____/ /_"
print " / ___/ __ \/ / __ \/ ___/  / ___/ __ \/ ___/ __/"
print "/ /__/ /_/ / / /_/ / /     (__  ) /_/ / /  / /_  "
print "\___/\____/_/\____/_/     /____/\____/_/   \__/  \n"

# list files, then remove files that are not jpg or png
images = os.listdir(".")
images = [img for img in images if (img.endswith('png')) or (img.endswith('jpg') ) or (img.endswith('jpeg'))]

# following loop loads the image files into a list structure
print "-----> started loading images"
loadedimg = []
for im in images:
    try:
        loadedimg.append(mpimg.imread(im))
        print "   loaded image: ", im
    except:
        print "error while loading: ", im, "\n"

# average the pixel values in the rgb spectrum, then convert to hsv and store
print "-----> started calculating average hue per image"
hueimg = []
for im in loadedimg:
    t1 = np.mean(im, axis=0)
    t2 = np.mean(t1, axis=0)
    try:
        t3 = colorsys.rgb_to_hsv(t2[0], t2[1], t2[2])
        hueimg.append(int(t3[0]*360))
        print u"\u2022",
    except:
        print "error while processing hsv value of image, possibly caused by black and white jpg"
        hueimg.append("error")
print "\n"

# rename files to the hsv value they have
print "-----> started renaming process"
for x in range(0,len(images)):
    try:
        ext = images[x].rsplit('.', 1)[1]
        os.rename(images[x], (str(hueimg[x]) + "." + ext) )
    except:
        print "Two exactly the same hue images were found... too bad, no fix is made yet"
print "-----> program finished"
