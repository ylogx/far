#!/usr/bin/env python3

import sys
import far.main

try:
    sys.exit(far.main.main())
except KeyboardInterrupt:
    sys.exit(1)
