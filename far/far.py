from __future__ import print_function

import os
import logging

from .logger import Logger

class Far:
    """ Far class
    """

    def __init__(self, verbosity=0):
        self.verbosity = verbosity
        self.logger = Logger(self.verbosity)
