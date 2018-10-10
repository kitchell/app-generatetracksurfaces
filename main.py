#!/usr/bin/env python

import glob
import os
import shutil
import json
from niftiMask2Surface import niftiMask2Surface

with open('config.json') as config_json:
    config = json.load(config_json)

pwd = os.getcwd()
os.mkdir(pwd + "/surfaces")
#os.chdir(pwd + "/surfaces")
try:
    shutil.copyfile(config["maskdir"]+"/color.json", pwd + "/surfaces/color.json")
except:
    print('no color.json file')

print('looking for ' + config["maskdir"] + "/*.nii.gz")
filetype = config["filetype"]
smooth_iter = config["smooth_iter"]
for file in glob.glob(config["maskdir"] + "/*.nii.gz"):
    print(file)
    #split_name = os.path.basename(file).split('_')
    #split_name[-1] = 'surf.' + filetype
    #surfname = '_'.join(split_name)
    #trim .nii.gz
    split_name = os.path.basename(file).split('.nii.gz')
    surfname = split_name[0]+"."+filetype
    print(surfname)
    niftiMask2Surface(file, 'surfaces/'+surfname, smooth_iter, filetype)
