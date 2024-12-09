.. _reading_nwb:

Reading NWB Files
==================

This section provides an introduction on how to read NWB files in Python using PyNWB and Matlab using MatNWB. If you are interested in converting your data to NWB, then please see the :neuroconv-docs:`NeuroConv User Guide <user_guide>` as well as for more in-depth tutorials visit the :pynwb-docs:`PyNWB  <tutorials>` and :matnwb-docs:`MatNWB <#tutorials>` tutorials and documentation.

Reading With PyNWB
~~~~~~~~~~~~~~~~~~

* See the PyNWB tutorial on :pynwb-docs:`Reading and Exploring an NWB File  <tutorials/general/plot_read_basics.html>`
  for an introduction to how to read, explore, and do basic visualizations with an NWB file in Python.
* The :pynwb-docs:`Query Intracellular Electrophysiology Metadata <tutorials/domain/plot_icephys_pandas.html>`
  PyNWB tutorial then focuses specifically on how to read and query metadata related to intracellular
  electrophysiology data.

.. _file_read_matnwb:

Reading with MatNWB
~~~~~~~~~~~~~~~~~~~

For most files, MatNWB only requires the ``nwbRead`` call:

.. code-block:: MATLAB

    nwb = nwbRead('path/to/filename.nwb');

This call will read the file, create the necessary NWB schema class files, as well as any extension schemata that is needed for the file itself. This is because both PyNWB and MatNWB embed a copy of the schema environment into the NWB file when it is written.


The returned object above is an NwbFile which serves as the root object with which you can use to browse the contents of the file. More detail about the NwbFile class can be found here: :ref:`matnwb-read-nwbfile-intro`.

.. toctree::
    :maxdepth: 2

    matnwb/nwbfile
    matnwb/dynamictable
    matnwb/untyped
    matnwb/troubleshooting
