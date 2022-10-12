# -*- coding: utf-8 -*-
"""
:Module:            highspot.users
:Synopsis:          Defines the users-related functions associated with the Highspot API
:Created By:        Jeff Shurtliff
:Last Modified:     Jeff Shurtliff
:Modified Date:     12 Oct 2022
"""

from . import api
from .errors import exceptions


def me(hs_object):
    """This function returns the information about the user making the API call.

    .. versionadded:: 1.0.0

    :param hs_object: The core :py:class:`highspot.Highspot` object
    :type hs_object: class[highspot.Highspot]
    :returns: A dictionary with the user data
    :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
    """
    return api.get_request_with_retries(hs_object, '/me')


def get_users(hs_object, email=None, list_type=None, with_fields=None, exclude_fields=None, start=0, limit=100):
    """This function retrieves a list of users.

    .. versionadded:: 1.0.0

    :param hs_object: The core :py:class:`highspot.Highspot` object
    :type hs_object: class[highspot.Highspot]
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
    endpoint = '/users?'
    if email and isinstance(email, str):
        endpoint += f'email={email}'
    if list_type:
        if list_type == 'all' or list_type == 'unverified' or list_type == 'verified':
            endpoint += f'list={list_type}' if endpoint.endswith('?') else f'&list={list_type}'
        else:
            raise exceptions.InvalidFieldError(val='list_type')
    if with_fields:
        # TODO: Raise an exception if with_fields is not a str, tuple, list, or set
        if not isinstance(with_fields, str):
            with_fields = ",".join(with_fields)
        segment = f'with-fields={with_fields}'
        endpoint += segment if endpoint.endswith('?') else f'&{segment}'
    if exclude_fields:
        # TODO: Raise an exception if exclude_fields is not a str, tuple, list, or set
        if not isinstance(exclude_fields, str):
            exclude_fields = ",".join(exclude_fields)
        segment = f'exclude-fields={exclude_fields}'
        endpoint += segment if endpoint.endswith('?') else f'&{segment}'
    start_limit_segment = f'start={start}&limit={limit}'
    endpoint += start_limit_segment if endpoint.endswith('?') else f'&{start_limit_segment}'
    return api.get_request_with_retries(hs_object, endpoint)


def get_user(hs_object, user_id):
    """This function retrieves the metadata for a specific user.

    .. versionadded:: 1.0.0

    :param hs_object: The core :py:class:`highspot.Highspot` object
    :type hs_object: class[highspot.Highspot]
    :param user_id: The unique identifier for the user
    :type user_id: str
    :returns: The user metadata as a dictionary
    :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
    """
    endpoint = f'/users/{user_id}'
    return api.get_request_with_retries(hs_object, endpoint)


def get_user_properties(hs_object, user_id):
    """This function retrieves the properties for a specific user.

    .. versionadded:: 1.0.0

    :param hs_object: The core :py:class:`highspot.Highspot` object
    :type hs_object: class[highspot.Highspot]
    :param user_id: The unique identifier for the user
    :type user_id: str
    :returns: The user properties as a dictionary
    :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
    """
    endpoint = f'/users/{user_id}/properties'
    return api.get_request_with_retries(hs_object, endpoint)


def get_user_property(hs_object, user_id, property_name):
    """This function retrieves a given property for a specific user.

    .. versionadded:: 1.0.0

    :param hs_object: The core :py:class:`highspot.Highspot` object
    :type hs_object: class[highspot.Highspot]
    :param user_id: The unique identifier for the user
    :type user_id: str
    :param property_name: The name of the property value to return
    :type property_name: str
    :returns: The user properties as a dictionary
    :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
    """
    endpoint = f'/users/{user_id}/properties/{property_name}'
    return api.get_request_with_retries(hs_object, endpoint)
