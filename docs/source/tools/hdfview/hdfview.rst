.. _analysistools-hdfview:

HDFView
--------

.. short_description_start

:ref:`analysistools-hdfview` is a general visual tool written in Java for
browsing and editing HDF5 files. HDFView does not provide
NWB-specific functionality but is useful (mainly for developers)
to debug and browse NWB HDF5 files. HDFView supports
viewing the HDF5 file hierarchy in a tree structure and editing of groups,
datasets, and attributes in HDF5 files. In addition, the HDF5 library
ships with range of `HDF5 command line tools <https://portal.hdfgroup.org/display/HDF5/HDF5+Command-line+Tools>`_
that can be useful for developers (e.g., *h5ls* and *h5dump* to introspect,
*h5diff* to compare, or *h5copy* and *h5repack* to copy HDF5 files).
:bdg-link-primary:`Docs <https://www.hdfgroup.org/downloads/hdfview/>`
:bdg-link-primary:`Source <https://github.com/HDFGroup/hdfview>`.

.. short_description_end

.. image:: https://www.hdfgroup.org/wp-content/uploads/2017/07/hdfview-sample2.jpg
    :class: align-left
    :width: 400


Compatability with NWB
^^^^^^^^^^^^^^^^^^^^^^

HDFView and HDF5 command line tools are generic HDF5 tools and as such are
not aware of the NWB schema. Modifying NWB files using generic HDF5 tools
can result in invalid NWB files. Use of these tools is, hence, primarily
useful for developers, e.g., for debugging.

