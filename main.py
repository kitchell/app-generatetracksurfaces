
import glob
import os
import json
from niftiMask2Surface import niftiMask2Surface

os.chdir("/N/dc2/projects/lifebid/wm_morphology/HCP_3T_test/125525/major_tracts/volumes")

for file in glob.glob("*Vol.nii.gz"):
    filename = file
    split_name = str.split(filename, '_')
    split_name[-1] = 'surf.ply'
    surfname = '_'.join(split_name)
    niftiMask2Surface(filename, surfname, 10)

