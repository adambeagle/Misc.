"""
scale_all_images.py
Author: Adam Beagle

Scales all images in a directory by a factor of SCALE as defined below.

Python Imaging Library (PIL) is required, and is available at
http://www.pythonware.com/products/pil/index.htm

** USAGE **
1) Place this script file in a directory containing images to resize.
2) Set constants below, if needed. (look to comments for more info).
3) Run. Note that depending on the number of files to resize and the
   filter chosen, execution could take several minutes.

** WARNINGS **
1) ALL images of formats matching EXTNS (defined below)
   in the same directory as this script will be resized.

2) If NEW_EXT matches an original image's format,
   and APPEND is empty, the original image will be overwritten.
"""

from os import listdir
from PIL import Image

#NOTE: See appendices of http://www.pythonware.com/library/pil/handbook/index.htm
#      for list of formats readable/writable by PIL.

SCALE   = 0.5               # Width and height multiplied by this
APPEND  = '_resized'        # Will be appended to end of new filename (can be empty)
NEW_EXT = 'png'             # Format to save resized file as
EXTNS   = ['jpg', 'jpeg',   # Only files of these types will be resized.
           'png', 'bmp']
FILTER  = Image.ANTIALIAS   # ANTIALIAS produces best quality for downsizing
                            #   Other options: NEAREST, BILINEAR, BICUBIC

imgs = [f for f in listdir('.') if f.split('.')[-1].lower() in EXTNS]

for filename in imgs:
    img = Image.open(filename)
    w, h = img.size

    w = int(w * SCALE)
    h = int(h * SCALE)

    img = img.resize((w, h), FILTER) 

    newFName = filename.split('.')
    newFName[-2] += APPEND
    newFName = ''.join(newFName[:-1]) + '.'*int(not NEW_EXT[0] == '.') + NEW_EXT
    print 'Saving %s...' % newFName
    img.save(newFName)

print 'Complete!'
