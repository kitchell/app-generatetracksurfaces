#!/usr/bin/env python

import os
import fnmatch
import json



with open('config.json') as config_json:
    config = json.load(config_json)

fname = config["maskdir"]+'/color.json'
if os.path.isfile(fname):
    numfiles = len(fnmatch.filter(os.listdir(config["maskdir"]), '*.nii.gz')) + 1
else: 
    numfiles = len(fnmatch.filter(os.listdir(config["maskdir"]), '*.nii.gz'))
print numfiles
