#!/usr/bin/env python3

import os
import glob
import json
import shutil

try:
    os.mkdir('./processed')
except OSError:
    print('Directory already exists')

subtotal = 0.0

for source in glob.iglob('./new/receipt-[0-9]*.json'):
    with open(source) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    destination = source.replace('new', 'processed')
    shutil.move(source, destination)
    print(f"Moved '{source}' to '{destination}'")

print(f'Receipt subtotal: ${round(subtotal, 2)}')
