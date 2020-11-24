import argparse
import requests
import json

endpoint = "https://www.spaceflightnewsapi.net/api/v1"

parser = argparse.ArgumentParser(
    description="Get some API information",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

parser.add_argument(
    "-t",
    "--type",
    required=True,
    help="Supply the information"
)

args = vars(parser.parse_args())
