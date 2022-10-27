# -*- coding: utf-8 -*-
"""
:Module:            highspot.groups
:Synopsis:          Defines the group-related functions associated with the Highspot API
:Created By:        Jeff Shurtliff
:Last Modified:     Jeff Shurtliff
:Modified Date:     16 Oct 2022
"""

from . import api
from .errors import exceptions


def get_groups(hs_object, role_filter=None, right_filter=None, start=None, limit=None):
    """This function retrieves the list of groups.

    :param hs_object: The core :py:class:`highspot.Highspot` object
    :type hs_object: class[highspot.Highspot]
    :param role_filter: Role by which to filter groups (``editor``, ``viewer``, ``manager``, or ``owner``)
    :type role_filter: str, None
    :param right_filter: Right by which to filter groups (``edit``, ``view``, or ``manage``)
    :type right_filter: str, None
    :param start: The start position of the paged request
    :type start: str, int, None
    :param limit: The maximum number of groups returned
    :type limit: str, int, None
    :returns: The group list data in JSON format
    :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`,
             :py:exc:`highspot.errors.exceptions.InvalidFieldError`
    """
    endpoint = '/groups?' if any((role_filter, right_filter, start, limit)) else '/groups'
    if role_filter:
        valid_role_filters = ['editor', 'viewer', 'manager', 'owner']
        if role_filter not in valid_role_filters:
            raise exceptions.InvalidFieldError('The role filter value must be a valid role.')
        endpoint += f'role={role_filter}'
    if right_filter:
        valid_right_filters = ['edit', 'view', 'manage']
        if right_filter not in valid_right_filters:
            raise exceptions.InvalidFieldError('The right filter value must be a valid right.')
        endpoint += f'&right={right_filter}' if '=' in endpoint else f'right={right_filter}'
    if start:
        endpoint += f'&start={start}' if '=' in endpoint else f'start={start}'
    if limit:
        endpoint += f'&limit={limit}' if '=' in endpoint else f'limit={limit}'
    return api.get_request_with_retries(hs_object, endpoint)


def get_group(hs_object, group_id):
    """This function returns the metadata for a specific group.

    :param hs_object: The core :py:class:`highspot.Highspot` object
    :type hs_object: class[highspot.Highspot]
    :param group_id: The unique identifier for the group
    :type group_id: str
    :returns: The group metadata in JSON format
    :raises: :py:exc:`highspot.errors.exceptions.APIConnectionError`
    """
    endpoint = f'/groups/{group_id}'
    return api.get_request_with_retries(hs_object, endpoint)
