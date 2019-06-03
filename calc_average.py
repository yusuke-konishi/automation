#!/usr/bin/env python3
# a tentative script to calculate average from specific strings like:
# "real 0m18.669s 0m12.642s 0m6.164s 0m10.037s 0m12.003s"

import sys, re

if len(sys.argv) < 2:
    sys.exit('Usage: calc_average.py <filepath>')

src_file = open(sys.argv[1], 'r')
src_list = src_file.readlines()
src_file.close()

for line in src_list:
    if not line.startswith('real'):
        continue

    line = re.sub(r'real 0m', '', line)
    line = re.sub(r's 0m', ',', line)
    line = re.sub(r's$', '', line)
    list = line.split(',')

    total = 0
    for i in range(len(list)):
        list[i] = float(list[i])
        total += list[i]
    print(total / 5)