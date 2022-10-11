# -*- coding: utf-8 -*-
"""
:Module:            highspot.errors.exceptions
:Synopsis:          Collection of exception classes relating to the highspot library
:Created By:        Jeff Shurtliff
:Last Modified:     Jeff Shurtliff
:Modified Date:     11 Oct 2022
"""

#################
# Base Exception
#################


# Define base exception class
class HighspotError(Exception):
    """This is the base class for Highspot exceptions.

    .. versionadded:: 1.0.0
    """
    pass


############################
# Authentication Exceptions
############################


class MissingAuthDataError(HighspotError):
    """This exception is used when authentication data is not supplied and therefore a connection cannot occur.

    .. versionadded:: 1.0.0
    """
    def __init__(self, *args, **kwargs):
        """This method defines the default or custom message for the exception."""
        default_msg = "The authentication data was not provided and a connection cannot be established."
        if not (args or kwargs):
            args = (default_msg,)
        else:
            custom_msg = f'The {args[0]} {default_msg.split("data ")[1]}'
            args = (custom_msg,)
        super().__init__(*args)


#####################
# General Exceptions
#####################


class CurrentlyUnsupportedError(HighspotError):
    """This exception is used when a feature or functionality being used is currently unsupported.

    .. versionadded:: 1.0.0
    """
    def __init__(self, *args, **kwargs):
        """This method defines the default or custom message for the exception."""
        default_msg = "This feature is currently unsupported at this time."
        if not (args or kwargs):
            args = (default_msg,)
        else:
            custom_msg = f"The '{args[0]}' {default_msg.split('This ')[1]}"
            args = (custom_msg,)
        super().__init__(*args)


class DataMismatchError(HighspotError):
    """This exception is used when there is a mismatch between two data sources.

    .. versionadded:: 1.0.0
    """
    def __init__(self, *args, **kwargs):
        """This method defines the default or custom message for the exception."""
        default_msg = "A data mismatch was found with the data sources."
        if not (args or kwargs):
            args = (default_msg,)
        elif 'data' in kwargs:
            multi_types = [list, tuple, set]
            if type(kwargs['data']) == str:
                custom_msg = f"{default_msg.split('data')[0]}'{kwargs['val']}'{default_msg.split('with the')[1]}"
                custom_msg = custom_msg.replace('sources', 'source')
                args = (custom_msg,)
            elif type(kwargs['data']) in multi_types and len(kwargs['data']) == 2:
                custom_section = f"'{kwargs['data'][0]}' and '{kwargs['data'][1]}'"
                custom_msg = f"{default_msg.split('data sources')[0]}{custom_section}{default_msg.split('with the')[1]}"
                args = (custom_msg,)
        super().__init__(*args)


class InvalidFieldError(HighspotError):
    """This exception is used when an invalid field is provided.

    .. versionadded:: 1.0.0
    """
    def __init__(self, *args, **kwargs):
        """This method defines the default or custom message for the exception."""
        default_msg = "The field that was provided is invalid."
        if not (args or kwargs):
            args = (default_msg,)
        elif 'val' in kwargs:
            custom_msg = f"{default_msg.split('field ')[0]}'{kwargs['val']}'{default_msg.split('The')[1]}"
            args = (custom_msg,)
        super().__init__(*args)


class MissingRequiredDataError(HighspotError):
    """This exception is used when a function or method is missing one or more required arguments.

    .. versionadded:: 1.0.0
    """
    def __init__(self, *args, **kwargs):
        """This method defines the default or custom message for the exception."""
        default_msg = "Missing one or more required parameters"
        init_msg = "The object failed to initialize as it is missing one or more required arguments."
        param_msg = "The required parameter 'PARAMETER_NAME' is not defined"
        if not (args or kwargs):
            args = (default_msg,)
        elif 'init' in args or 'initialize' in args:
            if 'object' in kwargs:
                custom_msg = f"{init_msg.split('object')[0]}'{kwargs['object']}'{init_msg.split('The')[1]}"
                args = (custom_msg,)
            else:
                args = (init_msg,)
        elif 'param' in kwargs:
            args = (param_msg.replace('PARAMETER_NAME', kwargs['param']),)
        else:
            args = (default_msg,)
        super().__init__(*args)


#########################
# Generic API Exceptions
#########################


class APIConnectionError(HighspotError):
    """This exception is used when the API query could not be completed due to connection aborts and/or timeouts.

    .. versionadded:: 1.0.0
    """
    def __init__(self, *args, **kwargs):
        """This method defines the default or custom message for the exception."""
        default_msg = "The API query could not be completed due to connection aborts and/or timeouts."
        if not (args or kwargs):
            args = (default_msg,)
        super().__init__(*args)


class APIRequestError(HighspotError):
    """This exception is used for generic API request errors when there isn't a more specific exception.

    .. versionadded:: 1.0.0
    """
    def __init__(self, *args, **kwargs):
        """This method defines the default or custom message for the exception."""
        default_msg = "The API request did not return a successful response."
        if not (args or kwargs):
            args = (default_msg,)
        super().__init__(*args)
