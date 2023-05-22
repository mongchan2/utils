# for utils

---
- strain_batch.bash : 작업 디렉토리 내부에 INCAR, POSCAR, POTCAR, KPOINTS파일이 존재하는 경우에 대해서 -2% ~ 2% strain 범위에 대해서 작업 병렬제출 

- amorphous_build.py : 작업 디렉토리에 POSCAR가 존재하는 경우에는 Lattice 정보를 받아서 amorphous 생성, 그렇지 않은 경우는 Lattice를 설정해서 진행
