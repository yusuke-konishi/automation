#!/usr/bin/env python3
#
# prep:
#   1. chmod +x insert_greater_than.py
#   2. echo "alias igt='insert_greater_than.py && sleep 1 && exit'" >> ~/.bash_profile
#   3. source ~/.bash_profile
#
# usage:
#   1. copy the source text to clipboard
#   2. run "igt" without any argument
#   3. paste the target text from clipboard

import pyperclip

source_text = pyperclip.paste()
print('--- source text ---')
print(source_text)

source_list = source_text.split('\n')
for i in range(len(source_list)):
    source_list[i] = '> ' + source_list[i]
target_text = '\n'.join(source_list)

pyperclip.copy(target_text)
print('\n--- target text ---')
print(pyperclip.paste())