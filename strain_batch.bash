#!/bin/bash

strain_batch.py

for dir in strain_*; do
    if [ -d "$dir" ]; then
		cp INCAR POTCAR KPOINTS $dir
        cd "$dir"
        pbs.pl
		qsub pbs
        cd ..
    fi
done
