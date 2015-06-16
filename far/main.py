#!/usr/bin/env python3

from __future__ import print_function

import sys
import os
import argparse

from . import __version__
from .far import Far


def print_version():    # pragma: no cover
    print('Far version %s' % __version__)
    print('Copyright (c) 2015 by Shubham Chaudhary.')
    print('License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>')
    print('This is free software: you are free to change and redistribute it.')
    print('There is NO WARRANTY, to the extent permitted by law.')


def parse_known_args():
    """ Parse command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-V', '--version',
                        action='store_true',
                        dest='version',
                        help='Print the version number and exit')
    mutually_exclusive_group = parser.add_mutually_exclusive_group()
    mutually_exclusive_group.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show verbose information.'
        ' Higher verbosity can be selected by --verbosity flag')
    parser.add_argument('-o', '--old',
                        type=str,
                        help='Old word to be replaced')
    parser.add_argument('-n', '--new', type=str, help='New replacement word')
    parser.add_argument('-d', '--dry-run', action='store_true', help='Dry Run')

    args, otherthings = parser.parse_known_args()
    return args, otherthings


def main():
    """ Main
    """
    args, otherthings = parse_known_args()

    if args.version:
        print_version()
        return 0

    verbosity = 0
    if args.verbose:
        verbosity = 1

    far = Far(verbosity=verbosity)

    if args.dry_run:
        far.dry_run(old=args.old)
    else:
        far.find_and_replace(old=args.old, new=args.new)


if __name__ == '__main__':
    sys.exit(main())
