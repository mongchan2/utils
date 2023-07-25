#!/usr/bin/env python
from pymatgen.core.composition import Composition
from pymatgen.core.structure import IStructure, Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.analysis.diffraction.xrd import XRDCalculator
from tqdm import tqdm
import matplotlib.pyplot as plt 
import numpy as np 
import os 
import pandas as pd 

# dir 내부를 모두 탐색해서 리스트에 적용한다는거고 
original_dir = os.getcwd() # 현재위치  
root_dir = original_dir # 현재위치를 root로 두고 
dir_list = []
for path, dirs, files in os.walk(root_dir):   
    if len(dirs) != 0:
        dir_list = dir_list + [dirs]
    else:
        continue
dir_list = dir_list[0]


# Definition Gaussian broadening function
def spectrum(theta, intensity, sigma, x):
    gE = []
    for Ei in x:
        tot = 0
        for Ej, I in zip(theta, intensity):
            tot += I*np.exp(-(((Ej - Ei)/sigma)**2))
        gE.append(tot)
    return gE 

xrd_dir = 'XRD_image'
print(os.system(f'mkdir {xrd_dir}'))

for mp in tqdm(dir_list):
    os.chdir(mp)
    print(mp)
    #####################################################
    # Codes for retrieving reduced formula
    #####################################################
    formula = []
    contcar = open('CONTCAR', 'r')
    full_formula = contcar.readline()
    reduced_formula = Composition(full_formula).reduced_formula
    formula = [reduced_formula]

    #####################################################
    # Codes for finding space group symbol 
    #####################################################
    space_group = []
    struct2 = IStructure.from_file('CONTCAR')
    sg_symbol, international_num = struct2.get_space_group_info(symprec = 1e-3)
    space_group = [sg_symbol]

    #####################################################
    # Codes for get XRD Pattern.
    #####################################################
    # Use conventional structure to ensure that peaks are labelled with the conventional Miller indices. 
    struct = Structure.from_file('CONTCAR')
    sg_analyzer = SpacegroupAnalyzer(struct)
#     conventional_struct = sg_analyzer.get_conventional_standard_structure()

    calculator = XRDCalculator(wavelength= 'CuKa', symprec= 1e-3)
    pattern = calculator.get_pattern(struct, two_theta_range= (10, 50)).as_dict()

    two_theta = pattern['x']
    intensity = pattern['y']

    x = np.linspace(10, 50, 500, endpoint= True)
    
    # Gaussian broadening
    sigma = 0.1 
    gE = spectrum(two_theta, intensity, sigma, x)

    # Plot XRD Diffraction
    fig, ax = plt.subplots(figsize= (10, 3))
    # Simulated pattern
    line_1 = ax.plot(x, gE, color= 'C0', lw= 3, label= 'Simulated data')
    
    
    fig_name = str('(' + mp + ')' + '_' + formula[0] + '_XRD.png')

    # Plot params
    ax.set_yticks(np.arange(0, 1), labels= (' '))
    ax.tick_params(axis= 'y', length= 0)
    ax.tick_params(axis= 'x', labelsize= 12, width= 3)
    ax.set_xlabel(r'$2\theta$ $(\degree)$', fontsize= 15, fontweight= 'bold')
    ax.set_ylabel('Normalized intensity', fontsize= 12, fontweight= 'bold')
#     ax.set_ylim(0, 110)
    ax.set_xlim(10, 50)
    ax.set_title(str('(' + mp + ')' + '_' + formula[0] + '_' + space_group[0]), fontsize= 15, fontweight= 'bold', pad= 15)
    
    ax.legend()

    for axis in ['top', 'bottom', 'left', 'right']:
        ax.spines[axis].set_linewidth(3)

    plt.tight_layout()
    plt.tight_layout()

#     plt.show()
    plt.savefig(fig_name, dpi= 200)
    plt.close()

    print(os.system(f'mv *.png ../{xrd_dir}/'))
    os.chdir(original_dir)


