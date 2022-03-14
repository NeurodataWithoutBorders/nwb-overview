Reading NWB Files
==================

Reading With PyNWB
~~~~~~~~~~~~~~~~~~

You can!


Reading with MatNWB
~~~~~~~~~~~~~~~~~~~

For most files, MatNWB only requires the ``nwbRead`` call:

.. code-block:: MATLAB

    nwb = nwbRead('path/to/filename.nwb');

This call will read the file, create the necessary NWB schema class files, as well as any extension schemata that is needed for the file itself. This is because both PyNWB and MatNWB embed a copy of the schema environment into the NWB file when it is written.


The returned object above is an NwbFile which serves as the root object with which you can use to browse the contents of the file. More detail about the NwbFile class can be found here: :ref:`nwbfile_info`.

.. toctree::
    :maxdepth: 2

    matnwb/nwbfile
    matnwb/dynamictable
    matnwb/untyped
    matnwb/troubleshooting
