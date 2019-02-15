#!/usr/bin/python
# This Python file uses the encoding: utf-8

import os

from PIL import Image, ExifTags

import image_handling
import localsettings as ls

from json_handling import JsonHandler

jHandle = JsonHandler()


def handle_files(root, files):
	filedata = {}
	for eachfile in files:
		filedata[eachfile] = {}
		if eachfile.endswith(ls.TYPE_JPG_FAMILY):
			jpg_data = image_handling.handle_jpg(os.path.join(os.path.abspath(root), eachfile))
			filedata[eachfile]['jpg_data'] = jpg_data
		else:
			filedata[eachfile]['comments'] = 'Not in ALLOWED_EXTENSIONS'
			filedata[eachfile]['status'] = False
	return filedata


def run():
	for root, dirs, files in os.walk(ls.INPUT_STORE_DIRECTORY):
		print('----'*10)
		print(root, dirs, files)
		if ls.JSON_DATA_FILENAME in files:
			print('%s processed earlier.. Continue' % (root,))
			continue
		else:
			print('Processing %s -> %s' % (root, files))
			analysis = { 'root': root, 'dirs': dirs, 'files': files }
			#filedata = handle_files(root, files)
			#analysis['file_data'] = filedata
			analysis['file_count'] = len(files)
			jsonfilepath = os.path.join(os.path.abspath(root), ls.JSON_DATA_FILENAME)
			jHandle.write_data_as_json(jsonfilepath, analysis)
		#break

if __name__ == "__main__":
    run()
    print('Done.')
