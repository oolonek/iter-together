iter-together
================

A package to iterate over multiple iterables together


Installation
------------

To download this code and install it in development mode, run the following:

.. code-block:: bash

    $ git clone https://github.com/commons-research/iter-together.git
    $ cd iter-together
    $ python install -e .


Testing
-------

.. code-block:: bash

    $ pip install tox
    $ tox

Documentation
-------------

Usage
-----

.. code-block:: python

    >>> from iter_together import iter_together
    >>> for a, b in iter_together([1, 2, 3], [4, 5, 6]):
    ...     print(a, b)
    ...
    1 4
    2 5
    3 6