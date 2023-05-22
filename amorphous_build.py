#!/usr/bin/env python

import numpy as np  
from pymatgen.core.structure import Structure
from pymatgen.core.composition import Composition
from pymatgen.core.units import Length, Mass
import random
import os 

# input : density, unit_cell information of POSCAR(is No POSCAR, input lattice vector) 
# output : amorphous unit cell! 

t_formula = input("input Formula : ") 
density = float(input("input Density : ")) 

lattice_const = 1
lattice_vectors = []

V = 0 

if os.path.exists("POSCAR"):
    V = Structure.from_file("POSCAR").volume  
    # constructre unit cell vector 
    lines = []
    with open("POSCAR", "r") as file:
        for i in range(1, 6):  
            line = file.readline()
            if i >= 2 and i <= 5:
                lines.append(line.strip())


    for i in lines: 
        if i == lines[0]:
            lattice_const = float(i)
        else: 
            float_numbers = [lattice_const*float(num) for num in i.split()]
            lattice_vectors.append(float_numbers)

else:
    for i in range(3):
        vector = input("input vector : ")
        vector = list(map(float, vector.split()))
        lattice_vectors.append(vector)
    matrix = np.array(lattice_vectors)  
    V = abs(np.linalg.det(matrix))  
        # need to get V         


# unit formula => mass of unit formula => density
random.seed() 
Comp = Composition(t_formula)
m = Mass(Comp.weight, "amu")
temp_density = m.to("g") / (V * Length(1, "ang").to("cm") ** 3) 
a = round(density / temp_density) 
b = Comp.as_dict()
# generate species for Structure

species_list = [] 
for key, value in b.items():
    for i in range(a * int(value)):
        species_list.append(key)

# get random lattice coordinate 
coord_list = []
for i in range(len(species_list)): 
    v = [random.random() for _ in range(3)]
    coord_list.append(v)


unit_cell = Structure(species=species_list, lattice=lattice_vectors, coords=coord_list)
unit_cell.to(filename="Amorphous.vasp", fmt="poscar")

