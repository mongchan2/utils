#!/usr/bin/env python

from pymatgen.core.structure import Structure
import os 

a = Structure.from_file("POSCAR")
a.apply_strain(strain=-0.02)

list_temp = [-0.02, -0.015, -0.01, -0.005, 0, 0.005, 0.01, 0.015, 0.02]

for i in list_temp:
    temp = Structure.from_file("POSCAR")
    temp.apply_strain(strain=i)
    str_temp = "strain_" + str(i)
    os.mkdir(str_temp) 
    os.chdir(str_temp)   
    temp.to(filename="POSCAR", fmt="poscar") 
    os.chdir('..')
    

