# -*- coding: utf-8 -*-

import os
import sys

# add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from src.container.FacadeProcess import FacadeProcess

try:
    FacadeProcess().run()
except Exception as ex:
    sys.stderr.write(str(ex))
