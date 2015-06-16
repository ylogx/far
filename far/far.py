from __future__ import print_function

import os
import logging


class Far:
    """ Far class
    """

    def __init__(self, verbosity=0):
        self.verbosity = verbosity

    def find_and_replace(self, old=None, new=None):
        if not old or not new:
            return
        cmd = "find . -type f -not -path '*/\.git*' -exec sed -i 's/" + old + "/" + new + "/g' {} +  "
        os.system(cmd)
