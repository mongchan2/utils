#!/bin/bash 

touch temp.txt
for i in strain_*
do
	echo $i >> temp.txt
	cd $i
	bandgap.py >> ../temp.txt
	cd ..
done 
