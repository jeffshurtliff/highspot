# -*- coding: utf-8 -*-
"""
:Module:            highspot.core
:Synopsis:          Defines the core highspot object used to interface with the Highspot API
:Created By:        Jeff Shurtliff
:Last Modified:     Jeff Shurtliff
:Modified Date:     11 Oct 2022
"""

from . import api
from . import users as users_module
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

        # Import inner object classes so their methods can be called from the primary object
        self.users = self._import_users_class()

    def _import_users_class(self):
        """This method allows the :py:class:`highspot.core.Highspot.Users` class to be utilized in the core object.

        .. versionadded:: 1.0.0
        """
        return Highspot.User(self)

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

    class User(object):
        """This class includes methods associated with Freshservice tickets."""
        def __init__(self, hs_object):
            """This method initializes the :py:class:`highspot.core.Highspot.Tickets` inner class object.

            .. versionadded:: 1.0.0

            :param hs_object: The core :py:class:`highspot.Highspot` object
            :type hs_object: class[highspot.Highspot]
            """
            self.hs_object = hs_object

        def me(self):
            """This function returns the information about the user making the API call.

            .. versionadded:: 1.0.0

            :returns: A dictionary with the user data
            :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
            """
            return users_module.me(self.hs_object)

        def get_users(self, email=None, list_type=None, with_fields=None, exclude_fields=None, start=0, limit=100):
            """This function retrieves a list of users.

            .. versionadded:: 1.0.0

            :param email: An email address by which to filter the users
            :type email: str, None
            :param list_type: Allows filtering by ``all`` or ``unverified`` users (filters by ``verified`` users by default)
            :type list_type: str, None
            :param with_fields: Additional field(s) to include in the response
            :type with_fields: str, tuple, list, set, None
            :param exclude_fields: Additional field(s) to exclude in the response
            :type exclude_fields: str, tuple, list, set, None
            :param start: The start position of a paged request (``0`` by default)
            :type start: int, str
            :param limit: Maximum number of users returned (``100`` by default)
            :type limit: int, str
            :returns: A list of dictionaries containing the user data
            :raises: :py:exc:`highspot.errors.exceptions.InvalidFieldError`,
                     :py:exc:`highspot.errors.exceptions.APIConnectionError`
            """
            return users_module.get_users(self.hs_object, email=email, list_type=list_type, with_fields=with_fields,
                                          exclude_fields=exclude_fields, start=start, limit=limit)

