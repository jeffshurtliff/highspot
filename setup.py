#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:Synopsis:          This script is the primary configuration file for the highspot project
:Created By:        Jeff Shurtliff
:Last Modified:     Jeff Shurtliff
:Modified Date:     17 Oct 2022
"""

import setuptools
import codecs
import os.path


def read(rel_path):
    """This function reads the ``version.py`` script in order to retrieve the version."""
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    """This function retrieves the current version of the package without needing to import the
       :py:mod:`highspot.utils.version` module in order to avoid dependency issues."""
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delimiter = '"' if '"' in line else "'"
            return line.split(delimiter)[1]
    raise RuntimeError("Unable to find the version string")


with open('README.md', 'r') as fh:
    long_description = fh.read()

version = get_version('src/highspot/utils/version.py')

setuptools.setup(
    name='highspot',
    version=version,
    author='Jeff Shurtliff',
    author_email='jeff.shurtliff@rsa.com',
    description='A Python toolset for utilizing the Highspot API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeffshurtliff/highspot",
    project_urls={
        'Issue Tracker': 'https://github.com/jeffshurtliff/highspot/issues',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Communications",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Content Management System",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Office/Business",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires='>=3.6',
    install_requires=[
        "urllib3>=1.26.7",
        "requests>=2.26.0",
        "setuptools~=52.0.0"
    ],
    extras_require={
        'sphinx': [
            'Sphinx>=3.4.0',
            'sphinxcontrib-applehelp>=1.0.2',
            'sphinxcontrib-devhelp>=1.0.2',
            'sphinxcontrib-htmlhelp>=1.0.3',
            'sphinxcontrib-jsmath>=1.0.1',
            'sphinxcontrib-qthelp>=1.0.3',
            'sphinxcontrib-serializinghtml>=1.1.4'
        ],
    }
)
