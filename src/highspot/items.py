# -*- coding: utf-8 -*-
"""
:Module:            highspot.items
:Synopsis:          Defines the item-related functions associated with the Highspot API
:Created By:        Jeff Shurtliff
:Last Modified:     Jeff Shurtliff
:Modified Date:     12 Oct 2022
"""

from . import api
from .errors import exceptions


def get_items(hs_object, spot_id, list_id=None, start=0, limit=100):
    """This function retrieves the items for a specific Spot.

    .. versionadded:: 1.0.0

    :param hs_object: The core :py:class:`highspot.Highspot` object
    :type hs_object: class[highspot.Highspot]
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
    endpoint = f'/items?spot={spot_id}&start={start}&limit={limit}'
    if list_id and isinstance(list_id, str):
        endpoint += f'&list={list_id}'
    return api.get_request_with_retries(hs_object, endpoint)


def get_item(hs_object, item_id):
    """This function retrieves the metadata for a specific item.

    .. versionadded:: 1.0.0

    :param hs_object: The core :py:class:`highspot.Highspot` object
    :type hs_object: class[highspot.Highspot]
    :param item_id: The unique identifier for the specific item
    :type item_id: str
    :returns: The item metadata as a dictionary
    :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
    """
    endpoint = f'/items/{item_id}'
    return api.get_request_with_retries(hs_object, endpoint)


def get_item_bookmarks(hs_object, item_id):
    """This function retrieves the bookmarks for a specific item.

    .. versionadded:: 1.0.0

    :param hs_object: The core :py:class:`highspot.Highspot` object
    :type hs_object: class[highspot.Highspot]
    :param item_id: The unique identifier for the specific item
    :type item_id: str
    :returns: The item bookmarks as a dictionary
    :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
    """
    endpoint = f'/items/{item_id}/bookmarks'
    return api.get_request_with_retries(hs_object, endpoint)


def get_item_content(hs_object, item_id, report=False):
    """This function retrieves the content for a specific item.

    .. versionadded:: 1.0.0

    :param hs_object: The core :py:class:`highspot.Highspot` object
    :type hs_object: class[highspot.Highspot]
    :param item_id: The unique identifier for the specific item
    :type item_id: str
    :param report: Indicates that the content is a report and should be returned in CSV format (False by default)
    :type report: bool
    :returns: The item content or an error in plain text or as a dictionary (JSON format)
    :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
    """
    # TODO: Add support for the start parameter
    endpoint = f'/items/{item_id}/content'
    if report:
        endpoint += '?format=text/csv'
    response = api.get_request_with_retries(hs_object, endpoint, return_json=False)
    if response.status_code == 404 or response.status_code == 410:
        response = response.json()
    else:
        response = response.text
    return response


def get_item_report(hs_object, item_id):
    """This function retrieves a CSV report for a specific item.

    .. versionadded:: 1.0.0

    :param hs_object: The core :py:class:`highspot.Highspot` object
    :type hs_object: class[highspot.Highspot]
    :param item_id: The unique identifier for the specific item
    :type item_id: str
    :returns: The item content or an error in plain text or as a dictionary (JSON format)
    :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
    """
    # TODO: Add support for the start parameter
    return get_item_content(hs_object, item_id, report=True)

