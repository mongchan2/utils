#!/bin/bash

keyworda="MACRO"
keywordb="MICRO"
output_filea="macro.txt"
output_fileb="micro.txt"

init_dir=$(pwd)

for i in strain_*
do
    cd "$i" || { echo "no dir"; exit 1; }

    # 행 번호를 저장할 변수 초기화
    line_numbera=""

    # OUTCAR 파일에서 keyworda를 찾아서 행 번호 저장
    while read -r line
    do
        if [[ "$line" == *"$keyworda"* ]]; then
    	line_numbera=$(grep -n "$keywordb" OUTCAR | cut -d ":" -f 1)
            break
        fi
    done < OUTCAR


    line_numberb=$(grep -n "$keywordb" OUTCAR | cut -d ":" -f 1)

    if [[ -n "$line_numbera" ]]; then
        echo "$i" >> "$init_dir/$output_filea"
        sed -n "${line_numbera},$((line_numbera + 5))p" OUTCAR >> "$init_dir/$output_filea"
    else
        echo "cannot get MACRO"
    fi

    if [[ -n "$line_numberb" ]]; then
        echo "$i" >> "$init_dir/$output_fileb"
        sed -n "${line_numberb},$((line_numberb + 5))p" OUTCAR >> "$init_dir/$output_fileb"
    else
        echo "cannot get MICRO"
    fi

    cd ..
done
