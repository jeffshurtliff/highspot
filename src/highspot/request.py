# -*- coding: utf-8 -*-
"""
:Module:            highspot.domain
:Synopsis:          Defines the domain-related functions associated with the Highspot API
:Created By:        Jeff Shurtliff
:Last Modified:     Jeff Shurtliff
:Modified Date:     20 Oct 2022
"""

from . import api
from .errors import exceptions


def get_request_status(hs_object, request_id):
    """This function returns the status of an asynchronous request.

    :param hs_object: The core :py:class:`highspot.Highspot` object
    :type hs_object: class[highspot.Highspot]
    :param request_id: The ID of the request to check
    :type request_id: str
    :returns: The status of the request
    :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
    """
    endpoint = f'/requests/{request_id}'
    return api.get_request_with_retries(hs_object, endpoint)


def get_request_result(hs_object, request_id):
    """This function returns the result of an asynchronous request.

    :param hs_object: The core :py:class:`highspot.Highspot` object
    :type hs_object: class[highspot.Highspot]
    :param request_id: The ID of the request to check
    :type request_id: str
    :returns: The status of the request
    :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
    """
    endpoint = f'/requests/{request_id}/result'
    return api.get_request_with_retries(hs_object, endpoint)
