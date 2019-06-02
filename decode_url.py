#!/usr/bin/env python3
# How do I decode a rewritten URL? - Proofpoint, Inc.
# https://help.proofpoint.com/Threat_Insight_Dashboard/Concepts/How_do_I_decode_a_rewritten_URL%3F

import pyperclip
import re
import urllib.parse
import html.parser

def main():
	rewrittenurl = pyperclip.paste()
	match = re.search(r'https://urldefense.proofpoint.com/(v[0-9])/', rewrittenurl)
	if match:
		if match.group(1) == 'v1':
			decodev1(rewrittenurl)
		elif match.group(1) == 'v2':
			decodev2(rewrittenurl)
		else:
			print('Unrecognized version in: ', rewrittenurl)

	else:
		print('No valid URL found in input: ', rewrittenurl)

def decodev1 (rewrittenurl):
	match = re.search(r'u=(.+?)&k=',rewrittenurl)
	if match:
		urlencodedurl = match.group(1)
		htmlencodedurl = urllib.parse.unquote(urlencodedurl)
		url = html.unescape(htmlencodedurl)
		print(url)
	else:
		print('Error parsing URL')

def decodev2 (rewrittenurl):
	match = re.search(r'u=(.+?)&[dc]=',rewrittenurl)
	if match:
		specialencodedurl = match.group(1)
		trans = str.maketrans('-_', '%/')
		urlencodedurl = specialencodedurl.translate(trans)
		htmlencodedurl = urllib.parse.unquote(urlencodedurl)
		url = html.unescape(htmlencodedurl)
		print(url)
	else:
		print('Error parsing URL')

if __name__ == '__main__':
    main()