Troubleshooting File Reads in MatNWB
====================================

Outlined below are the most common issues reported by users when they read a NWB file as well as common troubleshooting approaches to resolve them.

Schema Version Conflicts
~~~~~~~~~~~~~~~~~~~~~~~~

If you run into an error where reading a file appears to expect the wrong properties, you should first check if your MATLAB path is not pointing to other environments with the same packages.

Missing Embedded Schemata
~~~~~~~~~~~~~~~~~~~~~~~~~

Some older NWB files do not have an embedded schema. To read from these files you will need the API generation functions ``generateCore`` and ``generateExtension`` to generate the class files before calling ``nwbRead`` on them. You can also use the utility function ``util.getSchemaVersion`` to retrieve the correct Core schema for the file you are trying to read:

.. code-block:: MATLAB

    schemaVersion = util.getSchemaVersion('/path/to/matnwb/file.nwb');
    generateCore(schemaVersion);
    generateExtension(path/to/extension/namespace.yaml);

Bottom of the Barrel
~~~~~~~~~~~~~~~~~~~~

If you're here, you've probably reached your wit's end and wish for more specific help. In such times, you can always contact the NWB team either as a message on Slack or as an issue on `<Github <https://github.com/NeurodataWithoutBorders/matnwb>`_.
