#!/usr/bin/python
# This Python file uses the encoding: utf-8

import os

import localsettings as ls
from json_handling import JsonHandler

jHandle = JsonHandler()

def run():
	master = {}
	file_count = 0
	folder_count = 0
	initial_root = None
	for root, dirs, files in os.walk(ls.INPUT_STORE_DIRECTORY):
		folder_count += 1
		if initial_root is None:
			initial_root = root
		if ls.JSON_DATA_FILENAME in files:
			jsonfilepath = os.path.join(os.path.abspath(root), ls.JSON_DATA_FILENAME)
			data = jHandle.read_json_data(jsonfilepath)
			file_count += data['file_count']
			master[jsonfilepath] = data

	master['file_count'] = file_count
	master['folder_count'] = folder_count
	master_path = os.path.join(os.path.abspath(initial_root), ls.MASTER_JSON_FILENAME)

	jHandle.write_data_as_json(master_path, master)


if __name__ == "__main__":
    run()
    print('Done.')
