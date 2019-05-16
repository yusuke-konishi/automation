#!/usr/bin/env python3
#
# prep:
#   1. echo 'export PATH="$PATH:/path/to/dir"' >> ~/.bash_profile
#   2. source ~/.bash_profile
#   3. chmod +x /path/to/dir/list_separated_values.py
#
# usage:
#   - list_separated_values.py "value1 value2 value3"
#   - list_separated_values.py "value1,value2,value3" ","

import sys

separated_values = sys.argv[1]
separater = sys.argv[2] if len(sys.argv) >= 3 else ' '

separated_list = separated_values.split(separater)
list_len = len(separated_list)

for i in range(list_len):
    print(str(i + 1).rjust(len(str(list_len))) + ':', separated_list[i])