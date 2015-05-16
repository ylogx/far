#!/usr/bin/env python3

from __future__ import print_function

import sys
import os
import argparse

from .far import Far

def parse_known_args():
    """ Parse command line arguments
    """
    parser = argparse.ArgumentParser()
    mutually_exclusive_group = parser.add_mutually_exclusive_group()
    mutually_exclusive_group.add_argument('-v', '--verbose',
                         action='store_true', help='Show verbose information.'
                        ' Higher verbosity can be selected by --verbosity '
                        'flag')
    mutually_exclusive_group.add_argument('-l', '--verbosity', type=int,
                        help='Set higher verbosity level for more detailed '
                        'information: 1. Critical, 2. Error, 3. Warning, '
                        '4. Info, 5. Debug', choices=range(1, 6))

    args, otherthings = parser.parse_known_args()
    return args, otherthings


def main():
    """ Main
    """
    args, otherthings = parse_known_args()

    verbosity = 0
    if args.verbose:
        verbosity = 1
    elif args.verbosity:
        verbosity = args.verbosity

    far = Far(verbosity=verbosity)

if __name__ == '__main__':
    sys.exit(main())
