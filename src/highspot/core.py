# -*- coding: utf-8 -*-
"""
:Module:            highspot.core
:Synopsis:          Defines the core highspot object used to interface with the Highspot API
:Created By:        Jeff Shurtliff
:Last Modified:     Jeff Shurtliff
:Modified Date:     10 Oct 2022
"""

from .utils import log_utils, version

# Initialize logging
logger = log_utils.initialize_logging(__name__)


class Highspot(object):
    """This is the class for the core object leveraged in this library."""
    # Define the function that initializes the object instance (i.e. instantiates the object)
    def __init__(self, username=None, password=None, helper=None, api_version='0.5'):
        """This method instantiates the core Fresh object.

        .. versionadded:: 1.0.0
        """
        # Define the current version
        self.version = version.get_full_version()

        # Define the base URL
        self.base_url = f'https://api-su2.highspot.com/v{api_version}'
