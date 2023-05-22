#!/bin/bash

strain_batch.py

for dir in strain_*; do
    if [ -d "$dir" ]; then
		cp INCAR POSCAR POTCAR KPOINTS $dir
        cd "$dir"
        pbs.pl
		qsub pbs
        cd ..
    fi
done
