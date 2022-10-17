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
