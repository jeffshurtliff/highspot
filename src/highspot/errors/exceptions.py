# -*- coding: utf-8 -*-
"""
:Module:            highspot.errors.exceptions
:Synopsis:          Collection of exception classes relating to the highspot library
:Created By:        Jeff Shurtliff
:Last Modified:     Jeff Shurtliff
:Modified Date:     10 Oct 2022
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