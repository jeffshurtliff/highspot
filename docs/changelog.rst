##########
Change Log
##########
This page documents the additions, changes, fixes, deprecations and removals made in each release.


*****
2.0.0
*****
**Release Date:** 2026-09-24

.. warning:: Version 2.0.0 and newer require Python 3.10 or newer. Version 1.0.0 is the final release that
             supports older Python versions.

Changed
=======
* The minimum supported Python version is now ``3.10`` (``>=3.10,<3.14``).
* The minimum versions of the ``requests``, ``urllib3``, ``idna`` and ``certifi`` dependencies were raised to
  address known security advisories.
* The project now uses ``poetry`` and ``pyproject.toml`` for packaging rather than ``setup.py`` and ``setuptools``.

Removed
=======
* The unused ``setuptools`` runtime dependency.
* The ``sphinx`` extras group, as the documentation dependencies are now defined as a Poetry development group.
