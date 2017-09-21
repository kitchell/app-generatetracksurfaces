#!/bin/bash

#mainly to debug locally
if [ -z $SERVICE_DIR ]; then export SERVICE_DIR=`pwd`; fi

#clean up previous job (just in case)
rm -f finished


if [ $ENV == "IUHPC" ]; then
	module unload python
	if [ $HPC == "KARST" ]; then
		module load anaconda2
	fi
	if [ $HPC == "CARBONATE" ]; then
		module load anaconda/python2.7/4.3.1
	fi
	
fi
	
	#module unload python/2.7.3


# remove surface directory
rm -rf surfaces

echo "starting main"

(

nohup time python $SERVICE_DIR/main.py > stdout.log 2> stderr.log

#check for output files
#if [ -s Right_Uncinate_surf.vtk ];

count=$(ls surfaces/* | wc -l)
echo "$NUMFILES"
if [ "$count" == "$NUMFILES" ] 
then
	echo 0 > finished
else
	echo "files missing"
	echo 1 > finished
	exit 1
fi
) &
