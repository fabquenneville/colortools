======
Manual
======

Name
----

colortools

Synopsis
--------

.. code-block:: bash

    colortools -tasks:cssfonts,cssbgs,csv

Description
-----------

colortools is a Python command line tool to generate lists of colors of various sources in various formats.

* css
* csv

Options
-------

-tasks:
=======
[cssfonts,cssbgs,csv]

* cssfonts: create a css file with all the text colors as classes
* cssbgs: create a css file with all the background colors as classes
* cssv: create a csv file with all colors

Examples
--------

.. code-block:: bash

    # Create a csv file with all colors
    ./colortools.py -tasks:csv
    # Create css files with all colors
    ./colortools.py -tasks:cssfonts,cssbgs

More examples in :doc:`use_cases`

See Also
--------

`Color Palette icon by Icons8 <https://icons8.com/icon/59484/color-palette>`_

Author
------

Fabrice Quenneville
