#!/usr/bin/env sh

cd /mnt/c/work/src/project01
. venv/bin/activate
cd /mnt/c/work/src/project01

if [ ! -e kuku.npy ]; then
    python src/make_kuku.py -o kuku.npy
else
    echo 'kuku.npy already exists'
fi
if [ -e kuku.npy ] && [ ! double_kuku.npy -nt kuku.npy ]; then
    python src/calculate_double.py -i kuku.npy -o double_kuku.npy
else
    echo 'double_kuku.npy already exists'
fi
if [ -e double_kuku.npy ] && [ ! sum_result.txt -nt double_kuku.npy ]; then
    python src/calculate_sum.py -i double_kuku.npy -o sum_result.txt
else
    echo 'sum_result.txt already exists'
fi

deactivate