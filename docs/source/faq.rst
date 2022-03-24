Frequently Asked Questions
--------------------------

Is NWB 2 stable?
================

Yes! NWB 2.0 was officially released in January 2019, and the schema is now stable. Any changes that will be made now will be backwards compatible.

I would like to use NWB. How do I get started?
==============================================

See the :ref:`user-guide` page for more information.

How do I cite NWB 2 in my research?
===================================

O. Rübel, A. J. Tritt, B. Dichter, T. Braun, N. Cain, N. Clack, T. J. Davidson, M. Dougherty, J.-C. Fillion-Robin, N. Graddis, M. Grauer, J. T. Kiggins, L. Niu, D. Ozturk, W. Schroeder, I. Soltesz, F. T. Sommer, K. Svoboda, L. Ng, L. M. Frank, K. Bouchard. NWB:N 2.0: An Accessible Data Standard for Neurophysiology. January 18, 2019. doi: https://doi.org/10.1101/523035 (preprint)
(:nwb2-biorxiv:`Online Abstract <>`)
(:nwb2-biorxiv-pdf:`PDF <>`)

What is the difference between NWB and NWB:N?
=============================================

Neurodata Without Borders (NWB) started as a project by the Kavli Foundation with the goal to enhance accessibility of neuroscience data across the community. The intent was to have a broad range of projects under the NWB umbrella. The Neurodata Without Borders: Neurophysiology (NWB:N) data standard was intended to be the first among many such projects. As NWB:N is currently the only project under the NWB umbrella, the terms “NWB” and “NWB:N” are often used interchangeably.

What is the difference between PyNWB, nwb-schema, and api-python?
=================================================================

:pynwb-docs:`PyNWB <>` is the current Python reference read/write API for the NWB:N 2.x format. The nwb-schema repo is used to
manage development on the data standard schema. End-users who want to use NWB:N typically do not need to worry about
the nwb-schema repo as the current schema is always installed with the corresponding API (whether it is :pynwb-docs:`PyNWB <>` for Python
or :matnwb-docs:`MatNWB <>` for Matlab). :api-python:`api-python <>` is a deprecated write-only API designed for
NWB:N 1.0.xfiles. :pynwb-docs:`PyNWB <>` also provides support for reading some NWB:N 1.0.x files from popular data
repositories, such as the :allen-cell-type-atlas:`Allen Cell Types Atlas <>` via the
pynwb/legacy module.

Does PyNWB support NWB:N 1.0.x files?
=====================================

:pynwb-docs:`PyNWB <>` includes the pynwb/legacy module which supports reading of NWB:N 1.0.x files from popular data
repositories, such as the :allen-cell-type-atlas:`Allen Cell Types Atlas <>`. For NWB:N 1.0.x files from other sources the millage may vary in
particular when files are not fully format compliant, e.g., include arbitrary custom data or are missing required data fields.

What has changed between NWB:N 1 and 2?
=======================================

See the :nwb-schema-release-notes:`release notes of the NWB format schema <>` for details about changes to the format
schema. For details about changes to the specification language see the specification language release notes. With
regard to software, NWB 2 marks a full reboot and introduced with :pynwb-docs:`PyNWB <>`, :matnwb-docs:`MatNWB <>`,
:hdmf-docutils-docs:`HDMF docutils <>`, :nwb-schema-docs:`nwb-schema <>` etc. several
new packages and repositories while tools, e.g., :api-python:`api-python <>`, that were created for NWB:N 1.x have been deprecated.

How do I install PyNWB?
=======================

See the :ref:`install_users` for details.

How do I install MatNWB?
========================
See the :matnwb-docs:`MatNWB documentation <#setup>` for details.

Who can I contact for questions?
================================

For details, please review our Contributing Guidelines.

* For general questions, use the :nwb-helpdesk:`NWB Helpdesk <>`.
* To contribute, or to report a bug, create an issue on the appropriate GitHub repository.
* To receive updates about NWB at large, sign up for the :nwb-mailing-list:`NWB mailing list <>`.

Why use HDF5 as the primary backend for NWB?
============================================
See page: :ref:`why_hdf5`

Are you aware of the Rossant blog posts about moving away from HDF5?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Yes. See above for our motivations for using HDF5. Note that this blog post was not peer reviewed and at several points was either incorrect or is now outdated.

Why not just use HDF5?
======================
The goal of NWB is to package neurophysiology data with metadata sufficient for reuse and reanalysis of the data by other researchers. HDF5 enables users to provide very rich metadata, sufficient for describing neuroscience data for this purpose. The problem with HDF5 on its own is that it is just too flexible. Without a schema, files could be missing key metadata like the sampling rate of a time series. Furthermore, different labs that use HDF5 would use completely different methods for organizing and annotating experiment data. It would be quite difficult to aggregate data across labs or build common tools without imposing structure on the HDF5 file. This is the purpose of the NWB schema- to provide requirements that ensure reusability of the data, and to provide a common structure that enables interoperability across the global neurophysiology community. Users can use extensions to build from schema and describe new types of neurophysiology data.

How does NWB 2.0 compare to other standards?
============================================
See page: :ref:`comparison-to-other-standards`

Where should I publish my NWB files?
====================================
You can publish NWB files in many different archives. Funding or publishing  requirements may require you to publish
your data in a particular archive. Many such archives already support NWB. If not, please let us know and we will be happy to assist you and the archive developers with supporting the NWB standard.

If you are free to publish data wherever, we would recommend :dandi:`DANDI <>`. DANDI has built-in support for NWB that
validates NWB files, automatically extracts key metadata to enable search, and provides tools for interactively
exploring and analyzing NWB files. Furthermore, it provides an efficient interface for publishing neuroscience datasets on the TB scale, and can do so for free.

How do I read NWB files in different programming languages?
===========================================================
NWB files are usually just HDF5 files with a particular structure. If using a language that has a supported NWB API
(Python, MATLAB), this API will leverage the structure to provide a more intuitive interface to the data. If using
Python, we recommend using PyNWB, and if using MATLAB we recommend using MatNWB. You can also use the HDF5 readers
available in Python and MATLAB, but that will likely be less convenient. If you are using other programming languages,
such as R, C, C++, Julia, Java, or Javascript, each of these languages has an HDF5 API that can be used to read all of
the data in an NWB file. Writing valid NWB files in languages other than PyNWB and MatNWB is possible, but tricky.