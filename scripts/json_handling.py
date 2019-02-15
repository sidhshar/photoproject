#!/usr/bin/python
# This Python file uses the encoding: utf-8

import json

class JsonHandler(object):
    def write_data_as_json(self, jsonfilepath, data):
        print('Write json file %s' % (jsonfilepath,))
        with open(jsonfilepath, 'w') as outfile:
            json.dump(data, outfile)

    def read_json_data(self, jsonfilepath):
        with open(jsonfilepath, 'r') as f:
            return json.load(f)
