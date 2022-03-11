Troubleshooting File Reads in MatNWB
====================================

Schema Version Collisions in MATLAB path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Missing Embedded Schemata
~~~~~~~~~~~~~~~~~~~~~~~~~

Using ``ignorecache`` and ``savedir``

Generating a MatNWB Extension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In MatNWB, simply call ``generateExtension("path/to/extension/namespace.yaml");``; The class files will be generated under the ``+types/+<extension>`` module and can be accessed via standard MATLAB class semantics:

.. code-block:: MATLAB

    ts = types.ndx_example.TetrodeSeries(<arguments>);

.. note::
    As seen above, MatNWB will convert namespace names if they are not valid identifiers in MATLAB. See `Variable Names <https://www.mathworks.com/help/matlab/matlab_prog/variable-names.html>`_ for more information. In most cases, the conversion conforms with MATLAB's approach with `matlab.lang.makeValidName() <https://www.mathworks.com/help/matlab/ref/matlab.lang.makevalidname.html>`_

