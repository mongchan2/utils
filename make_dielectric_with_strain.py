#!/usr/bin/env python 
import numpy as np 
import matplotlib.pyplot as plt 
import sys
import woong_util
import statistics as st

sys.path.append('/home/mongchan2/bin')

m20,m15,m10,m5,z,p5,p10,p15,p20 = [], [], [], [], [], [], [], [], []
options = {
    'strain_-0.02': 1,
    'strain_-0.015': 2,
    'strain_-0.01': 3,
    'strain_-0.005': 4,
    'strain_0': 5,
    'strain_0.005': 6,
    'strain_0.01': 7,
    'strain_0.015': 8,
    'strain_0.02': 9
}
results = {
    1 : m20,
    2 : m15,
    3 : m10,
    4 : m5,
    5 : z,
    6 : p5,
    7 : p10,
    8 : p15,
    9 : p20,

}



filename = "macro.txt"
with open(filename, 'r') as file:
    opt = 0
    start_point = False
    count = 0 
    t1,t2,t3 = 0, 0, 0
    for line in file:
        # opt value select by start point 
        if start_point == False: 
            opt = options.get(line.strip(), None)
            if opt is not None:
                start_point = True
            continue
            
        if start_point == True:
            if '-----' in line.strip():
                continue 
            elif 'S' in line.strip():
                continue
            else:
                if count == 0:
                    t1 = float(line.split()[0])
                    count += 1
                elif count == 1:
                    t2 = float(line.split()[1])
                    count += 1
                else:
                    t3 = float(line.split()[2])
                    max_val = max(t1,t2,t3) 
                    t1, t2, t3 = 0,0,0
                    count = 0 
                    if opt in results:
                        results[opt].append(max_val) 
                    start_point = False

temp_list = [st.median(m20), st.median(m15),st.median(m10),st.median(m5),st.median(z),st.median(p5),st.median(p10),st.median(p15),st.median(p20)] 
plt.plot([-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2], temp_list, color="C0", linestyle='--')


plt.vlines(-2.0, min(m20), max(m20))
plt.vlines(-1.5, min(m15), max(m15))
plt.vlines(-1.0, min(m10), max(m10))
plt.vlines(-0.5, min(m5), max(m5))
plt.vlines(0.0, min(z), max(z))
plt.vlines(0.5, min(p5), max(p5))
plt.vlines(1.0, min(p10), max(p10))
plt.vlines(1.5, min(p15), max(p15))
plt.vlines(2.0, min(p20), max(p20))


plt.ylim([2, 3]) 
plt.title("Dielectric constant of a-SiO2 with strain")
plt.xlabel("Strain(%)")
plt.ylabel("Dielectric constant")

plt.savefig("temp.png", dpi=200, transparent=True) 
plt.show()
