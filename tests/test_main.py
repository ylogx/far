#!/usr/bin/env python

from __future__ import print_function

import os
import sys

try:
    import unittest
    import unittest.mock
    from unittest.mock import patch
    from unittest.mock import call
except ImportError as e:
    import mock
    from mock import patch
    from mock import call

from far.main import main


class TestMain(unittest.TestCase):
    def setUp(self):
        self.argv_backup = sys.argv

    def tearDown(self):
        sys.argv = self.argv_backup

    @patch('far.main.print_version')
    def test_should_print_version_and_exit_with_short_flag(self, mock_print_version):
        sys.argv = ['dummy', '-V']
        out = main()
        mock_print_version.assert_called_once_with()
        self.assertEqual(out, 0)

    @patch('far.main.print_version')
    def test_should_print_version_and_exit_with_long_flag(self, mock_print_version):
        sys.argv = ['dummy', '--version']
        out = main()
        mock_print_version.assert_called_once_with()
        self.assertEqual(out, 0)


    @patch('far.main.Far')
    def test_should_set_verbosity_1_if_short_flag_passed(self, mock_far):
        sys.argv = ['dummy', '-v']
        main()
        mock_far.assert_called_once_with(verbosity=1)

    @patch('far.main.Far')
    def test_should_set_verbosity_1_if_long_flag_passed(self, mock_far):
        sys.argv = ['dummy', '--verbose']
        main()
        mock_far.assert_called_once_with(verbosity=1)


class AnyStringContaining(str):
    def __eq__(self, other):
        return self in other


if __name__ == '__main__':
    unittest.main()
