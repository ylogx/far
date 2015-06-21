""" Functional Tests for find and replace feature
"""
import os
import sys

try:
    import unittest
except ImportError:
    import unittest2 as unittest

from tempfile import TemporaryDirectory

from far import main


class TestFunctionalFindAndReplace(unittest.TestCase):
    def test_find_and_replace(self):
        with TemporaryDirectory() as tempdir:
            subdirs = ['a/b/c/d.cpp', 'd/e/f/g.c', 'h/i/j.py']
            paths = [os.path.join(tempdir, p) for p in subdirs]
            for path in paths:
                create(path)
                jibber_in = write_jibber(path)
            os.chdir(tempdir)
            old = 'lorem'
            new = 'merol'

            sys.argv = ['dummy', '-o', old, '-n', new]
            main.main()

            for path in paths:
                with open(path) as fhan:
                    jibber_out = fhan.read()
                    self.assertFalse(old in jibber_out)


def write_jibber(path):
    """ Write jibberish content in file """
    jibber = 'Lorem ipsum lorem ipsum lorem ipsum'
    with open(path, 'w') as fhan:
        fhan.write(jibber)
    return jibber


def create(path):
    """ Create file and directory in given path """
    basedir = os.path.dirname(path)
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    touch(path)


def touch(fname, times=None):
    """ Touch a file with given name """
    with open(fname, 'a'):
        os.utime(fname, times)
