import argparse

from certifi import what, where

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--what", action="store_true")
args = parser.parse_args()

if args.what:
    print(what())
else:
    print(where())
