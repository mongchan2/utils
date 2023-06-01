# for utils

---
- strain_batch.bash : 작업 디렉토리 내부에 INCAR, POSCAR, POTCAR, KPOINTS파일이 존재하는 경우에 대해서 -2% ~ 2% strain 범위에 대해서 작업 병렬제출 

- amorphous_build.py : 작업 디렉토리에 POSCAR가 존재하는 경우에는 Lattice 정보를 받아서 amorphous 생성, 그렇지 않은 경우는 Lattice를 설정해서 진행

- make_dielectric_file.bash : strain이 존재하는 폴더 내에서 strain에 대한 정보만을 추출(OUTPUT : macro.txt, micro.txt)

- make_dielectric_with_strain : macro.txt를 통해서 strain에 대한 dielectric constant에 대한 함수를 그려준다.

- make_bandgap_with_strain : temp.txt를 통해서 얻어진 band gap을 통해서 strain에 대한 band gap 함수를 그려준다. 

- get_bandgap.bash : strain에 대한 bandgap을 구해서, 결과로 temp.txt파일을 생성한다. 
