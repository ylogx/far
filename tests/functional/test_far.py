""" Functional Tests for find and replace feature
"""
import os
import sys

try:
    import unittest
except ImportError:
    import unittest2 as unittest

from shutil import rmtree
from tempfile import mkdtemp

from far import main


class TestFunctionalFindAndReplace(unittest.TestCase):
    def setUp(self):
        self.tempdir = mkdtemp()
        subdirs = ['a/b/c/d.cpp', 'd/e/f/g.c', 'h/i/j.py']
        self.paths = [os.path.join(self.tempdir, p) for p in subdirs]
        for path in self.paths:
            create(path)
            jibber_in = write_jibber(path)
        os.chdir(self.tempdir)
        self.old = 'lorem'
        self.new = 'merol'

    def tearDown(self):
        rmtree(self.tempdir)


    def test_should_find_and_replace_in_files(self):
        sys.argv = ['dummy', '-o', self.old, '-n', self.new]

        main.main()

        for path in self.paths:
            with open(path) as fhan:
                jibber_out = fhan.read()
                self.assertFalse(self.old in jibber_out)

    def test_should_not_edit_in_dry_run_mode(self):
            sys.argv = ['dummy', '-d', '-o', self.old]

            main.main()

            for path in self.paths:
                with open(path) as fhan:
                    jibber_out = fhan.read()
                    self.assertFalse(self.new in jibber_out)



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
