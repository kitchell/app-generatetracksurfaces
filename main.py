
import glob
import os
import json
from niftiMask2Surface import niftiMask2Surface

with open('config.json') as config_json:
    config = json.load(config_json)

pwd = os.getcwd()
os.mkdir(pwd + "/surfaces")
os.chdir(pwd + "/surfaces")

print('looking for ' + config["maskdir"] + "/*Vol.nii.gz")

for file in glob.glob(config["maskdir"] + "/*Vol.nii.gz"):
    print(file)
    split_name = os.path.basename(file).split('_')
    split_name[-1] = 'surf.vtk'
    surfname = '_'.join(split_name)
    print(surfname)
    niftiMask2Surface(file, surfname, 10)
