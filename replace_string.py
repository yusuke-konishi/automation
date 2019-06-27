#!/usr/bin/env python3
# a tentative script to replace string by pattern like "(Running /health_checks/.*?) .*(\[ .* \])"
# ex: replace_string.py ncc.log "(Running /health_checks/.*?) .*(\[ .* \])"

import sys, re

if len(sys.argv) < 3:
    sys.exit('Usage: replace_string.py <filepath> <pattern>')

src_file = open(sys.argv[1], 'r')
src_list = src_file.readlines()
src_file.close()

pattern = re.compile(sys.argv[2])

for line in src_list:
    mo = pattern.search(line)

    if not mo:
        continue

    line = re.sub(pattern, mo.group(1) + ' ' + mo.group(2), line)
    print(line, end='')