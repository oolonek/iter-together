iter-together
================

A package to iterate over multiple iterables together


Installation
------------

To download this code and install it in development mode, run the following:

.. code-block:: bash

    $ git clone https://github.com/oolonek/iter-together
    $ cd iter-together
    $ python install -e .


Testing
-------

.. code-block:: bash

    $ pip install tox
    $ tox

Documentation
-------------

.. image:: https://readthedocs.org/projects/iter-together-pma/badge/?version=latest
    :target: https://iter-together-pma.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


Usage
-----

.. code-block:: python

    >>> from iter_together_pma import iter_together
    >>> for a, b in iter_together([1, 2, 3], [4, 5, 6]):
    ...     print(a, b)
    ...
    1 4
    2 5
    3 6