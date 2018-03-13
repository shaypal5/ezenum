ezenum
######
|PyPI-Status| |PyPI-Versions| |Build-Status| |Codecov| |LICENCE|

Easy enums for Python.

.. code-block:: python

  >>> RGB = StringEnum(['Red', 'Green', 'Blue'])
  >>> RGB.Red
      'Red'

.. contents::

.. section-numbering::

Installation
============

Install ``ezenum`` with:

.. code-block:: bash

  pip install ezenum


Features
========

* Pure Python.
* Compatible with Python 3.5+.
* Easy creation of usefull enum objects.
* String enums with unified value and name attributes.


Use
===

StringEnum
----------

Easilly get a string enum from a string list.



Contributing
============

Package author and current maintainer is Shay Palachy (shay.palachy@gmail.com); You are more than welcome to approach him for help.


Installing for development
--------------------------

Clone:

.. code-block:: bash

  git clone git@github.com:shaypal5/ezenum.git


Install in development mode with test dependencies:

.. code-block:: bash

  cd ezenum
  pip install -e ".[test]"


Running the tests
-----------------

To run the tests, use:

.. code-block:: bash

  python -m pytest --cov=ezenum


Adding documentation
--------------------

This project is documented using the `numpy docstring conventions`_, which were chosen as they are perhaps the most widely-spread conventions that are both supported by common tools such as Sphinx and result in human-readable docstrings (in my personal opinion, of course). When documenting code you add to this project, please follow `these conventions`_.

.. _`numpy docstring conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
.. _`these conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt


Credits
=======
Created by Shay Palachy (shay.palachy@gmail.com).


.. |PyPI-Status| image:: https://img.shields.io/pypi/v/ezenum.svg
  :target: https://pypi.python.org/pypi/ezenum

.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/ezenum.svg
   :target: https://pypi.python.org/pypi/ezenum

.. |Build-Status| image:: https://travis-ci.org/shaypal5/ezenum.svg?branch=master
  :target: https://travis-ci.org/shaypal5/ezenum

.. |LICENCE| image:: https://img.shields.io/pypi/l/ezenum.svg
  :target: https://pypi.python.org/pypi/ezenum

.. |Codecov| image:: https://codecov.io/github/shaypal5/ezenum/coverage.svg?branch=master
   :target: https://codecov.io/github/shaypal5/ezenum?branch=master
