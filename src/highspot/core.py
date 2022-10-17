# -*- coding: utf-8 -*-
"""
:Module:            highspot.core
:Synopsis:          Defines the core highspot object used to interface with the Highspot API
:Created By:        Jeff Shurtliff
:Last Modified:     Jeff Shurtliff
:Modified Date:     16 Oct 2022
"""

from . import api
from . import domain as domain_module
from . import groups as groups_module
from . import items as items_module
from . import pitches as pitches_module
from . import request as request_module
from . import spots as spots_module
from . import users as users_module
from .errors import exceptions
from .utils import log_utils, version

# Initialize logging
logger = log_utils.initialize_logging(__name__)


class Highspot(object):
    """This is the class for the core object leveraged in this library."""
    # Define the function that initializes the object instance (i.e. instantiates the object)
    def __init__(self, username=None, password=None, helper=None, api_version='0.5'):
        """This method instantiates the core Fresh object."""
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
        self.domain = self._import_domain_class()
        self.groups = self._import_groups_class()
        self.items = self._import_items_class()
        self.pitches = self._import_pitches_class()
        self.requests = self._import_request_class()
        self.spots = self._import_spots_class()
        self.users = self._import_users_class()

    def _import_domain_class(self):
        """This method allows the :py:class:`highspot.core.Highspot.Domain` class to be utilized in the core object."""
        return Highspot.Domain(self)

    def _import_groups_class(self):
        """This method allows the :py:class:`highspot.core.Highspot.Group` class to be utilized in the core object."""
        return Highspot.Group(self)

    def _import_items_class(self):
        """This method allows the :py:class:`highspot.core.Highspot.Item` class to be utilized in the core object."""
        return Highspot.Item(self)

    def _import_pitches_class(self):
        """This method allows the :py:class:`highspot.core.Highspot.Pitch` class to be utilized in the core object."""
        return Highspot.Pitch(self)

    def _import_request_class(self):
        """This method allows the :py:class:`highspot.core.Highspot.Request` class to be utilized in the core object."""
        return Highspot.Request(self)

    def _import_spots_class(self):
        """This method allows the :py:class:`highspot.core.Highspot.Spot` class to be utilized in the core object."""
        return Highspot.Spot(self)

    def _import_users_class(self):
        """This method allows the :py:class:`highspot.core.Highspot.User` class to be utilized in the core object."""
        return Highspot.User(self)

    # Define the basic GET request method
    def get(self, endpoint, return_json=True, verify_ssl=True):
        """This function performs a GET request and will retry several times if a failure occurs.

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

    class Domain(object):
        """This class includes methods associated with Highspot domains."""
        def __init__(self, hs_object):
            """This method initializes the :py:class:`highspot.core.Highspot.Domain` inner class object.

            :param hs_object: The core :py:class:`highspot.Highspot` object
            :type hs_object: class[highspot.Highspot]
            """
            self.hs_object = hs_object

    class Group(object):
        """This class includes methods associated with Highspot groups."""
        def __init__(self, hs_object):
            """This method initializes the :py:class:`highspot.core.Highspot.Group` inner class object.

            :param hs_object: The core :py:class:`highspot.Highspot` object
            :type hs_object: class[highspot.Highspot]
            """
            self.hs_object = hs_object

    class Item(object):
        """This class includes methods associated with Highspot items."""
        def __init__(self, hs_object):
            """This method initializes the :py:class:`highspot.core.Highspot.Item` inner class object.

            :param hs_object: The core :py:class:`highspot.Highspot` object
            :type hs_object: class[highspot.Highspot]
            """
            self.hs_object = hs_object

        def get_items(self, spot_id, list_id=None, start=0, limit=100):
            """This function retrieves the items for a specific Spot.

            :param spot_id: The unique identifier for the Spot (**required**)
            :type spot_id: str
            :param list_id: The unique identifier for a list by which to filter the results
            :type list_id: str, None
            :param start: The start position of a paged request (``0`` by default)
            :type start: int, str
            :param limit: Maximum number of users returned (``100`` by default)
            :type limit: int, str
            :returns: A dictionary containing the items
            :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
            """
            return items_module.get_items(self.hs_object, spot_id=spot_id, list_id=list_id, start=start, limit=limit)

        def get_item(self, item_id):
            """This function retrieves the metadata for a specific item.

            :param item_id: The unique identifier for the specific item
            :type item_id: str
            :returns: The item metadata as a dictionary
            :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
            """
            return items_module.get_item(self.hs_object, item_id=item_id)

        def get_item_bookmarks(self, item_id):
            """This function retrieves the bookmarks for a specific item.

            :param item_id: The unique identifier for the specific item
            :type item_id: str
            :returns: The item bookmarks as a dictionary
            :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
            """
            return items_module.get_item_bookmarks(self.hs_object, item_id=item_id)

        def get_item_content(self, item_id, report=False):
            """This function retrieves the content for a specific item.

            :param item_id: The unique identifier for the specific item
            :type item_id: str
            :param report: Indicates that the content is a report and should be returned in CSV format (False by default)
            :type report: bool
            :returns: The item content or an error in plain text or as a dictionary (JSON format)
            :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
            """
            # TODO: Add support for the start parameter
            return items_module.get_item_content(self.hs_object, item_id=item_id, report=report)

        def get_item_report(self, item_id):
            """This function retrieves a CSV report for a specific item.

            :param item_id: The unique identifier for the specific item
            :type item_id: str
            :returns: The item content or an error in plain text or as a dictionary (JSON format)
            :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
            """
            # TODO: Add support for the start parameter
            return items_module.get_item_report(self.hs_object, item_id=item_id)

        def get_cms_metadata(self, item_id):
            """This function retrieves item metadata when the item was imported through an external CMS.

            :param item_id: The unique identifier for the specific item
            :type item_id: str
            :returns: The CMS metadata
            :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
            """
            return items_module.get_cms_metadata(self.hs_object, item_id=item_id)

        def get_item_thumbnails(self, item_id):
            """This function retrieves the thumbnail(s) for a given item.

            :param item_id: The unique identifier for the specific item
            :type item_id: str
            :returns: The thumbnail data
            :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
            """
            return items_module.get_item_thumbnails(self.hs_object, item_id=item_id)

        def get_item_properties(self, item_id):
            """This function retrieves the properties for a given item.

            :param item_id: The unique identifier for the specific item
            :type item_id: str
            :returns: The properties data
            :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
            """
            return items_module.get_item_properties(self.hs_object, item_id=item_id)

        def get_item_property(self, item_id, property_name):
            """This function retrieves a specific property for a given item.

            :param item_id: The unique identifier for the specific item
            :type item_id: str
            :param property_name: The name of the property to retrieve
            :type property_name: str
            :returns: The value of the property in JSON format
            :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
            """
            return items_module.get_item_property(self.hs_object, item_id=item_id, property_name=property_name)

    class Pitch(object):
        """This class includes methods associated with Highspot pitches."""
        def __init__(self, hs_object):
            """This method initializes the :py:class:`highspot.core.Highspot.Pitch` inner class object.

            :param hs_object: The core :py:class:`highspot.Highspot` object
            :type hs_object: class[highspot.Highspot]
            """
            self.hs_object = hs_object

        def get_pitches(self, start=0, limit=25, sort_by='recent_activity'):
            """This method retrieves a list of the user's pitches.

            :param start: The start position of a paged request (``0`` by default)
            :type start: int, str
            :param limit: Maximum number of users returned (``100`` by default)
            :type limit: int, str
            :param sort_by: Determines how the data is sorted (``recent_activity``, ``alphabetical``, or ``date_created``)
            :type sort_by: str
            :returns: The pitch data in JSON format
            :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`,
                     :py:exc:`highspot.errors.exceptions.InvalidFieldError`
            """
            return pitches_module.get_pitches(self.hs_object, start=start, limit=limit, sort_by=sort_by)

    class Request(object):
        """This class includes methods associated with Highspot asynchronous requests."""
        def __init__(self, hs_object):
            """This method initializes the :py:class:`highspot.core.Highspot.Request` inner class object.

            :param hs_object: The core :py:class:`highspot.Highspot` object
            :type hs_object: class[highspot.Highspot]
            """
            self.hs_object = hs_object

    class Spot(object):
        """This class includes methods associated with Highspot spots and lists."""
        def __init__(self, hs_object):
            """This method initializes the :py:class:`highspot.core.Highspot.Spot` inner class object.

            :param hs_object: The core :py:class:`highspot.Highspot` object
            :type hs_object: class[highspot.Highspot]
            """
            self.hs_object = hs_object

    class User(object):
        """This class includes methods associated with Highspot users."""
        def __init__(self, hs_object):
            """This method initializes the :py:class:`highspot.core.Highspot.User` inner class object.

            :param hs_object: The core :py:class:`highspot.Highspot` object
            :type hs_object: class[highspot.Highspot]
            """
            self.hs_object = hs_object

        def me(self):
            """This function returns the information about the user making the API call.

            :returns: A dictionary with the user data
            :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
            """
            return users_module.me(self.hs_object)

        def get_users(self, email=None, list_type=None, with_fields=None, exclude_fields=None, start=0, limit=100):
            """This function retrieves a list of users.

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
            :returns: A dictionary containing the user data
            :raises: :py:exc:`highspot.errors.exceptions.InvalidFieldError`,
                     :py:exc:`highspot.errors.exceptions.APIConnectionError`
            """
            return users_module.get_users(self.hs_object, email=email, list_type=list_type, with_fields=with_fields,
                                          exclude_fields=exclude_fields, start=start, limit=limit)

        def get_user(self, user_id):
            """This function retrieves the metadata for a specific user.

            :param user_id: The unique identifier for the user
            :type user_id: str
            :returns: The user metadata as a dictionary
            :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
            """
            return users_module.get_user(self.hs_object, user_id=user_id)

        def get_user_properties(self, user_id):
            """This function retrieves the properties for a specific user.

            :param user_id: The unique identifier for the user
            :type user_id: str
            :returns: The user properties as a dictionary
            :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
            """
            return users_module.get_user_properties(self.hs_object, user_id=user_id)

        def get_user_property(self, user_id, property_name):
            """This function retrieves a given property for a specific user.

            :param user_id: The unique identifier for the user
            :type user_id: str
            :param property_name: The name of the property value to return
            :type property_name: str
            :returns: The user properties as a dictionary
            :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
            """
            return users_module.get_user_property(self.hs_object, user_id=user_id, property_name=property_name)
