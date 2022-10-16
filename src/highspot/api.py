# -*- coding: utf-8 -*-
"""
:Module:            highspot.api
:Synopsis:          This module handles interactions with the Highspot REST API
:Created By:        Jeff Shurtliff
:Last Modified:     Jeff Shurtliff
:Modified Date:     16 Oct 2022
"""

import requests

from . import errors
from .utils import log_utils

# Initialize logging
logger = log_utils.initialize_logging(__name__)


def get_request_with_retries(hs_object, endpoint, return_json=True, verify_ssl=True):
    """This function performs a GET request and will retry several times if a failure occurs.

    :param hs_object: The Highspot object
    :param endpoint: The endpoint URI to query
    :type endpoint: string
    :param return_json: Determines if JSON data should be returned
    :type return_json: bool
    :param verify_ssl: Determines if SSL verification should occur (``True`` by default)
    :type verify_ssl: bool
    :returns: The JSON data from the response or the raw :py:mod:`requests` response.
    :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
    """
    # Construct the query URL
    endpoint = f'/{endpoint}' if not endpoint.startswith('/') else endpoint
    query_url = hs_object.base_url + endpoint

    # Perform the API call
    retries, response = 0, None
    while retries <= 5:
        try:
            response = requests.get(query_url, auth=hs_object.auth, verify=verify_ssl)
            break
        except Exception as exc_msg:
            _report_failed_attempt(exc_msg, 'get', retries)
            retries += 1
    if retries == 6:
        _raise_exception_for_repeated_timeouts()
    if return_json:
        response = response.json()
    return response


def _report_failed_attempt(_exc_msg, _request_type, _retries):
    """This function reports a failed API call that will be retried.

    :param _exc_msg: The exception that was raised within a try/except clause
    :param _request_type: The type of API request (e.g. ``post``, ``put`` or ``get``)
    :type _request_type: str
    :param _retries: The attempt number for the API request
    :type _retries: int
    :returns: None
    """
    _exc_name = type(_exc_msg).__name__
    if 'connect' not in _exc_name.lower():
        raise RuntimeError(f"{_exc_name}: {_exc_msg}")
    _current_attempt = f"(Attempt {_retries} of 5)"
    _error_msg = f"The {_request_type.upper()} request has failed with the following exception: " + \
                 f"{_exc_name}: {_exc_msg} {_current_attempt}"
    errors.handlers.eprint(f"{_error_msg}\n{_exc_name}: {_exc_msg}\n")


def _raise_exception_for_repeated_timeouts():
    """This function raises an exception when all API attempts (including) retries resulted in a timeout.

    :returns: None
    :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
    """
    _failure_msg = "The script was unable to complete successfully after five consecutive API timeouts. " + \
                   "Please run the script again or contact Highspot for further assistance."
    raise errors.exceptions.APIConnectionError(_failure_msg)
