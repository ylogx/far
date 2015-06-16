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
        self.old = 'old-pattern'
        self.new = 'new-pattern'

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
    def test_should_set_verbosity_0_if_no_flag_passed(self, mock_far):
        sys.argv = ['dummy']
        main()
        mock_far.assert_called_once_with(verbosity=0)

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

    @patch('far.main.Far.dry_run')
    def test_should_call_dry_run_if_short_flag_passed(self, mock_far):
        mock_far.return_value = 0
        sys.argv = ['dummy', '-d', '-o', self.old]

        main()

        mock_far.assert_called_once_with(old=self.old)


    @patch('far.main.Far.find_and_replace')
    def test_should_call_find_and_replace(self, mock_far):
        mock_far.return_value = 0
        sys.argv = ['dummy', '-o', self.old, '-n', self.new]

        main()

        mock_far.assert_called_once_with(old=self.old, new=self.new)


class AnyStringContaining(str):
    def __eq__(self, other):
        return self in other


if __name__ == '__main__':
    unittest.main()
