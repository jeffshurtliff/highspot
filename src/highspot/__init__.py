# -*- coding: utf-8 -*-
"""
:Module:            highspot
:Synopsis:          This is the ``__init__`` module for the highspot package
:Created By:        Jeff Shurtliff
:Last Modified:     Jeff Shurtliff
:Modified Date:     10 Oct 2022
"""

from .core import Highspot
from .utils import version

__all__ = ['core', 'Highspot']

# Define the package version by pulling from the highspot.utils.version module
__version__ = version.get_full_version()
