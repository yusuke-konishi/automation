#!/usr/bin/env python3
#
# Usage:
#   ./generate_bookmark_html.py <js_path>

import sys
import os
import re

# exit if no argument
if len(sys.argv) < 2:
    print('Usage: ./generate_bookmark_html.py <js_path>')
    sys.exit()

js_path = sys.argv[1]
js_dir = os.path.dirname(js_path)
js_file = os.path.basename(js_path)

bookmark_name = js_file[:-3]
html_file = f'bookmark_{bookmark_name}.html'
html_path = os.path.join(js_dir, html_file)

# convert JavaScript code into one-line string
js_str = ''

with open(js_path) as js_obj:
    print('----- checking/replacing double quotes -----')
    for i, line in enumerate(js_obj):
        if re.match(r'.*"', line):
            print(f'(before) {i + 1}: {line[:-1]}')
            line = line.replace('"', '&quot;')
            print(f'(after)  {i + 1}: {line[:-1]}')
        js_str += line[:-1]

# generate html file with JavaScript string and bookmark name
html_str = f"""<!DOCTYPE NETSCAPE-Bookmark-file-1>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>
    <DT><A HREF="{js_str}">{bookmark_name}</A>
</DL><p>
"""

with open(html_path, 'w') as html_obj:
    html_obj.write(html_str)

print('----- path summary -----')
print(f'js_path: {js_path}')
print(f'js_dir: {js_dir}')
print(f'js_file: {js_file}')
print(f'bookmark_name: {bookmark_name}')
print(f'html_file: {html_file}')
print(f'html_path: {html_path}')
