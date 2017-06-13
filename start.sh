#!/bin/bash

#mainly to debug locally
if [ -z $SERVICE_DIR ]; then export SERVICE_DIR=`pwd`; fi

#clean up previous job (just in case)
rm -f finished
module unload python/2.7.3
module load anaconda2

# remove surface directory
rm -rf surfaces

echo "starting main"

(

nohup time python $SERVICE_DIR/main.py > stdout.log 2> stderr.log

#check for output files
#if [ -s Right_Uncinate_surf.vtk ];

count=$(ls *.vtk | wc -l)
if [ $count -eq 20 ] 
then
	echo 0 > finished
else
	echo "files missing"
	echo 1 > finished
	exit 1
fi
) &
