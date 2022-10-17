####################
Highspot Core Object
####################
This section provides details around the core module and the methods used
within the core object for the **highspot** package, which are listed below.

* `Init Module (highspot)`_
* `Core Module (highspot.core)`_
    * `Core Functionality Subclasses (highspot.core.Highspot)`_
        * `Domain Subclass (highspot.core.Highspot.Domain)`_
        * `Groups Subclass (highspot.core.Highspot.Group)`_
        * `Items Subclass (highspot.core.Highspot.Item)`_
        * `Pitches Subclass (highspot.core.Highspot.Pitch)`_
        * `Request Subclass (highspot.core.Highspot.Request)`_
        * `Spots Subclass (highspot.core.Highspot.Spot)`_
        * `Users Subclass (highspot.core.Highspot.User)`_

|

**********************
Init Module (highspot)
**********************
This module (being the primary ``__init__.py`` file for the library) provides a
"jumping-off-point" to initialize the primary :py:class:`highspot.core.Highspot` object.

.. automodule:: highspot
   :members: Highspot
   :special-members: __init__

:doc:`Return to Top <core-object-methods>`

|

***************************
Core Module (highspot.core)
***************************
This module contains the core object and functions to establish the connection to the API
and leverage it to perform various actions.

.. automodule:: highspot.core
   :members:
   :special-members: __init__

:doc:`Return to Top <core-object-methods>`

|

Core Functionality Subclasses (highspot.core.Highspot)
======================================================
These classes below are inner/nested classes within the core :py:class:`highspot.core.Highspot` class.

.. note:: The classes themselves are *PascalCase* format and singular (e.g. ``Item``, ``User``, etc.) whereas
          the names used to call the inner class methods are all *lowercase* (or *snake_case*) and plural.
          (e.g. ``core_object.items.get_item()``, ``core_object.users.get_user()``, etc.)

Domain Subclass (highspot.core.Highspot.Domain)
-----------------------------------------------
.. autoclass:: highspot.core::Highspot.Domain
   :members:
   :noindex:

:doc:`Return to Top <core-object-methods>`

Groups Subclass (highspot.core.Highspot.Group)
----------------------------------------------
.. autoclass:: highspot.core::Highspot.Group
   :members:
   :noindex:

:doc:`Return to Top <core-object-methods>`

Items Subclass (highspot.core.Highspot.Item)
--------------------------------------------
.. autoclass:: highspot.core::Highspot.Item
   :members:
   :noindex:

:doc:`Return to Top <core-object-methods>`

Pitches Subclass (highspot.core.Highspot.Pitch)
-----------------------------------------------
.. autoclass:: highspot.core::Highspot.Pitch
   :members:
   :noindex:

:doc:`Return to Top <core-object-methods>`

Request Subclass (highspot.core.Highspot.Request)
-------------------------------------------------
.. autoclass:: highspot.core::Highspot.Request
   :members:
   :noindex:

:doc:`Return to Top <core-object-methods>`

Spots Subclass (highspot.core.Highspot.Spot)
--------------------------------------------
.. autoclass:: highspot.core::Highspot.Spot
   :members:
   :noindex:

:doc:`Return to Top <core-object-methods>`

Users Subclass (highspot.core.Highspot.User)
--------------------------------------------
.. autoclass:: highspot.core::Highspot.User
   :members:
   :noindex:

:doc:`Return to Top <core-object-methods>`

|
