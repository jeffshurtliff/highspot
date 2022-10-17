# -*- coding: utf-8 -*-
"""
:Module:            highspot.pitches
:Synopsis:          Defines the pitch-related functions associated with the Highspot API
:Created By:        Jeff Shurtliff
:Last Modified:     Jeff Shurtliff
:Modified Date:     17 Oct 2022
"""

from . import api
from .errors import exceptions


def get_pitches(hs_object, start=0, limit=25, sort_by='recent_activity'):
    """This function retrieves a list of the user's pitches.

    :param hs_object: The core :py:class:`highspot.Highspot` object
    :type hs_object: class[highspot.Highspot]
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
    valid_sort_options = ['recent_activity', 'alphabetical', 'date_created']
    if sort_by not in valid_sort_options:
        raise exceptions.InvalidFieldError(f"The value '{sort_by}' is not a valid sort option.")
    endpoint = f'/pitches?start={start}&limit={limit}&sortby={sort_by}'
    return api.get_request_with_retries(hs_object, endpoint)

