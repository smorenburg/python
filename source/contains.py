#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(
    description='contains: Search for words including partial word.'
)
parser.add_argument(
    'snippet',
    help='partial (or complete) string to search for in words'
)
parser.add_argument(
    '--version',
    '-v',
    action='version',
    version='%(prog)s 1.0'
)

args = parser.parse_args()
snippet = args.snippet.lower()

with open('/usr/share/dict/words') as f:
    words = f.readlines()

print([word.strip() for word in words if snippet in word.lower()])
