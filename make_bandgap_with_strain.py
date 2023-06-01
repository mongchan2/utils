#!/usr/bin/env python 

def read_results(filename, strain):
    with open(filename, 'r') as file:
        results = []
        start_reading = False

        for line in file:
            if line.strip() == f'strain_{strain}':
                start_reading = True
                continue

            if start_reading:
                if line.strip() == '':
                    break
                else:
                    if "Gap" in line:
                        continue
                    else:
                        gap_value = float(line.split()[0])
                        print(gap_value)
                        results.append(gap_value)
                        start_reading = False

    return results

file1 = 'temp.txt'

strain_m0005_results = read_results(file1, "-0.005")
strain_0_results = read_results(file1, "0")
strain_0005_results = read_results(file1, "0.005")
strain_001_results = read_results(file1, "0.01")
strain_m001_results = read_results(file1, "-0.01")
strain_0015_results = read_results(file1, "0.015")
strain_m0015_results = read_results(file1, "-0.015")
strain_002_results = read_results(file1, "0.02")
strain_m002_results = read_results(file1, "-0.02")

# now, we have list of this gap value, and need to plot it 


