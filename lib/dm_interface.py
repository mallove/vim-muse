#!/usr/bin/env python3

# Interfaces with datamuse.py

import os
import argparse
import datamuse

parser = argparse.ArgumentParser()
parser.add_argument("words")
args = parser.parse_args()
print(datamuse.rhyme(args.words))
