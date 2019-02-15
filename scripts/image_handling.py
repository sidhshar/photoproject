#!/usr/bin/python
# This Python file uses the encoding: utf-8

import os

from PIL import Image, ExifTags

import localsettings as ls

def get_jpg_exif(filepath):
    img = Image.open(filepath)
    return img._getexif()

def handle_jpg(filepath):
    print('Handle jpg data: %s' % (filepath,))
    jpg_data = {}
    exifdata = get_jpg_exif(filepath)
    if exifdata:
        jpg_data['exifdata'] = exifdata
        jpg_data['status'] = True
    else:
        jpg_data['comments'] = 'Could not extract EXIF data'
        jpg_data['status'] = False
    return jpg_data

