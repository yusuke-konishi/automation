#!/usr/bin/env python3
#
# usage:
#     1. copy the source text to clipboard
#     2. run this script without any argument
#     3. paste the target text from clipboard

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