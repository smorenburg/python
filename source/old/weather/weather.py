#!/usr/bin/env python3

import os
import requests
import sys

from argparse import ArgumentParser

parser = ArgumentParser(
    description=(
        'weather: Get the current weather information'
        'for your zipcode.'
    )
)
parser.add_argument(
    'zip',
    help='zip code to get the weather for'
)
parser.add_argument(
    '--country',
    '-c',
    default='NL',
    help='country zipcode belongs to, default is NL'
)
parser.add_argument(
    '--version',
    '-v',
    action='version',
    version='%(prog)s 1.0'
)

args = parser.parse_args()

api_key = os.getenv('OWM_API_KEY')

if not api_key:
    print("Error: no 'OWM_API_KEY' provided")
    sys.exit(1)

url = (
    f'http://api.openweathermap.org/data/2.5/weather?'
    f'zip={args.zip},{args.country}&appid={api_key}'
)

req = requests.get(url)

if req.status_code != 200:
    print(f'Error: talking to weather provider: {req.status_code}')
    sys.exit(1)

print(req.json())
