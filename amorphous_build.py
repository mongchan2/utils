#!/usr/bin/env python

import numpy as np  
from pymatgen.core.structure import Structure
from pymatgen.core.composition import Composition
from pymatgen.core.units import Length, Mass
import random
import os 
import math
# input : density, unit_cell information of POSCAR(is No POSCAR, input lattice vector) 
# output : amorphous unit cell! 

def distance(p1, p2):
    # Calculate the distance between two points
    # input : 3D vectors 
    # output : distance 
    x1, y1, z1 = p1
    x2, y2, z2 = p2
   
    a1 = min(abs(x1 - x2), 1 - abs(x1 - x2))
    a2 = min(abs(y1 - y2), 1 - abs(y1 - y2))
    a3 = min(abs(z1 - z2), 1 - abs(z1 - z2))

    return math.sqrt(a1 ** 2 + a2 ** 2 + a3 ** 2)

def generate_positions(num_particles, min_distance):
    # Generate structure with particles maintaining minimum distance 
    # use direct method, return cartesian coordinates  
    particles = []
    while len(particles) < num_particles: # for all particles 
        x1 = random.uniform(0, 1)
        x2 = random.uniform(0, 1)
        x3 = random.uniform(0, 1)
        
        dp = [x1,x2,x3]

        if all(distance(dp, p) >= min_distance for p in particles):
            # get each distance  
            particles.append(dp)
    return particles


iter_num = int(input("Number of structure to create: ")) 
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

# min_distance 
min_distance = 0.15

current_dir = os.getcwd() 
for i in range(iter_num):
    directory_name = f"{i}_a"
    dir_path = os.path.join(current_dir, directory_name) 
    os.makedirs(dir_path) 
    coord_list = generate_positions(len(species_list), min_distance)
    os.chdir(dir_path)
    unit_cell = Structure(species=species_list, lattice=lattice_vectors, coords=coord_list)
    unit_cell.to(filename="POSCAR", fmt="poscar")
    os.chdir(current_dir) 
# Print the coordinates of the particles

print("COMPLETE!!")

