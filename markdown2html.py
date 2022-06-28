#!/usr/bin/python3
"""
Module markdown2html
script takes two arguments
"""

import os
import sys


if __name__ == '__main__':

    if len(sys.argv[1:]) != 2:
        print('Usage: ./markdown2html.py README.md README.html',
        file=sys.stderr)
        sys.exit(1)
    
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]

    if not (os.path.exists(inputFile) and os.path.isfile(inputFile)):
        print(f'missing {inputFile}', file=sys.stderr)
        sys.exit(1)
    else:
        sys.exit(0)