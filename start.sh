#!/bin/bash

#mainly to debug locally
if [ -z $SCA_WORKFLOW_DIR ]; then export SCA_WORKFLOW_DIR=`pwd`; fi
if [ -z $SCA_TASK_DIR ]; then export SCA_TASK_DIR=`pwd`; fi
if [ -z $SCA_SERVICE_DIR ]; then export SCA_SERVICE_DIR=`pwd`; fi

#clean up previous job (just in case)
rm -f finished
module unload python/2.7.3
module load anaconda2


echo "starting main"

(

nohup time python main.py

#check for output files
if [ -s Right_Uncinate_surf.ply ];
then
	echo 0 > finished
else
	echo "files missing"
	echo 1 > finished
	exit 1
fi
) &