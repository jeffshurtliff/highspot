# -*- coding: utf-8 -*-
"""
:Module:            highspot.domain
:Synopsis:          Defines the domain-related functions associated with the Highspot API
:Created By:        Jeff Shurtliff
:Last Modified:     Jeff Shurtliff
:Modified Date:     17 Oct 2022
"""

from . import api
from .errors import exceptions


def get_custom_usage_labels(hs_object):
    """This function returns the custom usage labels in the user's domain.

    :param hs_object: The core :py:class:`highspot.Highspot` object
    :type hs_object: class[highspot.Highspot]
    :returns: The custom usage labels data in JSON format
    :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
    """
    endpoint = '/domain/custom-usage-labels'
    return api.get_request_with_retries(hs_object, endpoint)


def get_promoted_search_results(hs_object, start=None, limit=None):
    """This function retrieves the existing promoted search terms and their associated items.

    :param hs_object: The core :py:class:`highspot.Highspot` object
    :type hs_object: class[highspot.Highspot]
    :param start: The start position of a paged request (``0`` by default)
    :type start: int, str, None
    :param limit: Maximum number of users returned (``100`` by default)
    :type limit: int, str, None
    :returns: The promoted search data in JSON format
    :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
    """
    endpoint = '/domain/search/promoted'
    endpoint += '?' if any((start, limit)) else endpoint
    if start:
        endpoint += f'start={start}'
    if limit:
        endpoint += f'&limit={limit}' if '=' in endpoint else f'limit={limit}'
    return api.get_request_with_retries(hs_object, endpoint)
