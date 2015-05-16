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

    def find_and_replace(self, old=None, new=None):
        if old is None or new is None:
            return
        cmd = "find . -type f -not -path '*/\.git*' -exec sed -i 's/" + old + "/" + new + "/g' {} +  "
        os.system(cmd)
