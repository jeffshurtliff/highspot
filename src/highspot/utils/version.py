# -*- coding: utf-8 -*-
"""
:Module:            highspot.utils.version
:Synopsis:          This simple script contains the package version
:Created By:        Jeff Shurtliff
:Last Modified:     Jeff Shurtliff
:Modified Date:     16 Oct 2022
"""

from . import log_utils

# Initialize logging
logger = log_utils.initialize_logging(__name__)

# Define special and global variables
__version__ = "1.0.0"


def get_full_version():
    """This function returns the current full version of the ``highspot`` package."""
    return __version__


def get_major_minor_version():
    """This function returns the current major.minor (i.e. X.Y) version of the ``highspot`` package."""
    return ".".join(__version__.split(".")[:2])
