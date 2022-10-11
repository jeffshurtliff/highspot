# -*- coding: utf-8 -*-
"""
:Module:            highspot.core
:Synopsis:          Defines the core highspot object used to interface with the Highspot API
:Created By:        Jeff Shurtliff
:Last Modified:     Jeff Shurtliff
:Modified Date:     11 Oct 2022
"""

from . import api
from .errors import exceptions
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

        # Configure the authentication
        if not any((username, password)):
            raise exceptions.MissingAuthDataError()
        elif not username:
            raise exceptions.MissingAuthDataError('username')
        elif not password:
            raise exceptions.MissingAuthDataError('password')
        self.auth = (username, password)

    # Define the basic GET request method
    def get(self, endpoint, return_json=True, verify_ssl=True):
        """This function performs a GET request and will retry several times if a failure occurs.

        .. versionadded:: 1.0.0

        :param endpoint: The endpoint URI to query
        :type endpoint: string
        :param return_json: Determines if JSON data should be returned
        :type return_json: bool
        :param verify_ssl: Determines if SSL verification should occur (``True`` by default)
        :type verify_ssl: bool
        :returns: The JSON data from the response or the raw :py:mod:`requests` response.
        :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
        """
        return api.get_request_with_retries(self, endpoint, return_json, verify_ssl)
