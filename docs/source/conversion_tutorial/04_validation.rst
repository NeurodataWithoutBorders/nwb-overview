4. Validation of NWB files
---------------------------------

After you create NWB files, it is a good idea to inspect them to ensure that they are representing your data correctly.
There are several complementary tools that can help you ensure you are utilizing NWB optimally.

NWB Validation
==============

Once you create an NWB file, it is a good idea to validate it against the NWB schema. PyNWB comes
with a validator that you can run from the command line:

.. code-block:: bash

    python -m pynwb.validate test.nwb

see :ref:`validating` for details

NWB Inspector
=============

:nwbinspector-docs:`NWB Inspector` inspects NWB files for compliance with NWB Best Practices and
attempts to find mistakes in conversion. This inspector is
meant as a companion to the pynwb validator, which checks for strict schema
compliance. In contrast, this tool attempts to apply some common sense to
find components of the file that are technically compliant, but probably
incorrect, or suboptimal, or deviate from best practices. This tool is meant
simply as a data review aid. It does not catch all best practice violations,
and any warnings it does produce should be checked by a knowledgeable reviewer.

HDFView
=======
`HDFView <https://www.hdfgroup.org/downloads/hdfview/>`_ is a visual tool written by the HDF Group in Java for browsing and editing HDF (HDF5 and HDF4) files. With
HDFView, you can open NWB files and inspect their contents manually. HDFView can show you detailed information such
as chunking and comrpession settings ratio achieved for each dataset.

NWB Widgets
===========
`NWB Widgets <https://github.com/NeurodataWithoutBorders/nwb-jupyter-widgets>`_ is a library of widgets for
visualization NWB data in a Jupyter notebook (or lab). The widgets allow you to navigate through the hierarchical
structure of the NWB file and visualize specific data elements. It is designed to work out-of-the-box with NWB 2.0
files. Using NWB Widgets, you can explore the data in your NWB file and generate simple figures to ensure that your
data is represented correctly.


