========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |
        |
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/pokego-evol-maximizer/badge/?style=flat
    :target: https://readthedocs.org/projects/pokego-evol-maximizer
    :alt: Documentation Status

.. |version| image:: https://img.shields.io/pypi/v/pokego-evol-maximizer.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pokego-evol-maximizer

.. |downloads| image:: https://img.shields.io/pypi/dm/pokego-evol-maximizer.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/pokego-evol-maximizer

.. |wheel| image:: https://img.shields.io/pypi/wheel/pokego-evol-maximizer.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/pokego-evol-maximizer

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pokego-evol-maximizer.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/pokego-evol-maximizer

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pokego-evol-maximizer.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/pokego-evol-maximizer


.. end-badges

A web services for maximizing the number of pokemon you should return before you evolve them.

* Free software: BSD license

Installation
============

::

    pip install pokego-evol-maximizer

Documentation
=============

https://pokego-evol-maximizer.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
