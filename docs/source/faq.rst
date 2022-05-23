.. _faq-home:

***************************
Frequently Asked Questions
***************************

Using NWB
=========

Is NWB 2 stable?
----------------

Yes! NWB 2.0 was officially released in January 2019, and the schema is stable. A key goal of the NWB endavour is to ensure that NWB 2 remains accessible. As NWB evolves we strive to ensure that any changes we make do not break backwards compatiblility.

I would like to use NWB. How do I get started?
----------------------------------------------

See the :ref:`conversion_home` page for more information.

How do I cite NWB 2 in my research?
-----------------------------------

O. Rübel, A. J. Tritt, B. Dichter, T. Braun, N. Cain, N. Clack, T. J. Davidson, M. Dougherty, J.-C. Fillion-Robin, N. Graddis, M. Grauer, J. T. Kiggins, L. Niu, D. Ozturk, W. Schroeder, I. Soltesz, F. T. Sommer, K. Svoboda, L. Ng, L. M. Frank, K. Bouchard. NWB:N 2.0: An Accessible Data Standard for Neurophysiology. January 18, 2019. doi: https://doi.org/10.1101/523035 (preprint)
(:nwb2-biorxiv:`Online Abstract <>`)
(:nwb2-biorxiv-pdf:`PDF <>`)

How do I install PyNWB?
-----------------------

See the :ref:`install_users` for details.

How do I install MatNWB?
------------------------
See the :matnwb-docs:`MatNWB documentation <#setup>` for details.

What is the difference between PyNWB and nwb-schema?
----------------------------------------------------

:pynwb-docs:`PyNWB <>` is the Python reference read/write API for the current NWB 2.x format. The :nwb-schema-src:`nwb-schema-repo <>` is used to manage development of the data standard schema. End-users who want to use NWB typically do not need to worry about the nwb-schema repo as the current schema is always installed with the corresponding API (whether it is :pynwb-docs:`PyNWB <>` for Python or :matnwb-docs:`MatNWB <>` for Matlab).

How do I read NWB files in different programming languages?
-----------------------------------------------------------

For Python and Matlab we recommend using the :pynwb-docs:`PyNWB <>` and :matnwb-docs:`MatNWB <>` reference APIs. To get started see also the :ref:`reading_nwb` page.

If you are using other programming languages (such as R, C/C++, Julia, Java, or Javascript) you can use the standard HDF5 readers that are available for these languages. In contrast to the NWB native API (PyNWB, MatNWB), the HDF5 readers are not aware of NWB schema details. This can make writing valid NWB files in other languages (without  PyNWB and MatNWB) tricky, but for read they nonetheless provide access to the full data. For write, applications (e.g., MIES written in Igor) often chose to implement only the parts of the NWB standard that are relevant to the particular application.

Where should I publish my NWB files?
------------------------------------
You can publish NWB files in many different archives. Funding or publishing  requirements may require you to publish your data in a particular archive. Many such archives already support NWB. If not, please let us know and we will be happy to assist you and the archive developers with supporting the NWB standard.

If you are free to publish data wherever, we would recommend :dandi:`DANDI <>`. DANDI has built-in support for NWB that validates NWB files, automatically extracts key metadata to enable search, and provides tools for interactively exploring and analyzing NWB files. Furthermore, it provides an efficient interface for publishing neuroscience datasets on the TB scale, and can do so for free.

Who can I contact for questions?
--------------------------------

* **General questions:**  For general questions, use the :nwb-helpdesk:`NWB Helpdesk <>`.
* **Bugs and issues:** To contribute, or to report a bug, create an issue on the appropriate GitHub repository. To find relevant repositories see the :ref:`core-tools-home` and :ref:`dev_nwb_sources` pages.
* **Stay tuned:** To receive updates about NWB at large, sign up for the :nwb-mailing-list:`NWB mailing list <>`.

For details, please also review our Contributing Guidelines.

Alternative data standards and formats
======================================

How does NWB 2.0 compare to other standards?
--------------------------------------------
See page: :ref:`comparison-to-other-standards`

Why use HDF5 as the primary backend for NWB?
--------------------------------------------
See page: :ref:`why_hdf5`

Are you aware of the Rossant blog posts about moving away from HDF5?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Yes. See above for our motivations for using HDF5. Many of the technical issues raised in the blog post have been addressed and in our experience HDF5 is reliable and is performing well for NWB users.

Why not just use HDF5 on its own?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The goal of NWB is to package neurophysiology data with metadata sufficient for reuse and reanalysis of the data by other researchers. HDF5 enables users to provide very rich metadata, sufficient for describing neuroscience data for this purpose. The problem with HDF5 on its own is that it is just too flexible. Without a schema, files could be missing key metadata like the sampling rate of a time series. Furthermore, different labs that use HDF5 would use completely different methods for organizing and annotating experiment data. It would be quite difficult to aggregate data across labs or build common tools without imposing structure on the HDF5 file. This is the purpose of the NWB schema. The NWB schema formalizes requirements that ensure reusability of the data and provides a common structure that enables interoperability across the global neurophysiology community. Users can use extensions to build from schema and describe new types of neurophysiology data.

Why create the HDMF schema language instead of using an existing language?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
See page :ref:`why_hdmf_schema_language`

NWB 1 vs 2
==========

What has changed between NWB 1 and 2?
-------------------------------------

See the :nwb-schema-release-notes:`release notes of the NWB format schema <>` for details about changes to the format schema. For details about changes to the specification language see the specification language release notes. With regard to software, NWB 2 marks a full reboot and introduced with :pynwb-docs:`PyNWB <>`, :matnwb-docs:`MatNWB <>`, :hdmf-docutils-docs:`HDMF docutils <>`, :nwb-schema-docs:`nwb-schema <>` etc. several new packages and repositories while tools, e.g., :api-python:`api-python <>`, that were created for NWB:N 1.x have been deprecated.

Does PyNWB support NWB:N 1.0.x files?
-------------------------------------

:pynwb-docs:`PyNWB <>` includes the pynwb/legacy module which supports reading of NWB:N 1.0.x files from popular data repositories, such as the :allen-cell-type-atlas:`Allen Cell Types Atlas <>`. For NWB:N 1.0.x files from other sources the millage may vary in particular when files are not fully format compliant, e.g., include arbitrary custom data or are missing required data fields.

What is the difference between NWB and NWB:N?
---------------------------------------------

Neurodata Without Borders (NWB) started as a project by the Kavli Foundation with the goal to enhance accessibility of neuroscience data across the community. The intent was to have a broad range of projects under the NWB umbrella. The Neurodata Without Borders: Neurophysiology (NWB:N) data standard was intended to be the first among many such projects. As NWB:N is currently the only project under the NWB umbrella, the terms “NWB” and “NWB:N” are often used interchangeably.

What is the difference between PyNWB and api-python?
----------------------------------------------------

:pynwb-docs:`PyNWB <>` is the Python reference read/write API for the current NWB 2.x format. :api-python:`api-python <>` is a deprecated write-only API designed for NWB:N 1.0.x files. :pynwb-docs:`PyNWB <>` also provides support for reading some NWB:N 1.0.x files from popular data repositories, such as the :allen-cell-type-atlas:`Allen Cell Types Atlas <>` via the pynwb/legacy module.


