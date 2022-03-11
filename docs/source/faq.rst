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
:hdmf-docutils:`HDMF docutils <>`, :nwb-schema:`nwb-schema <>` etc. several
new packages and repositories while tools, e.g., :api-python:`api-python <>`, that were created for NWB:N 1.x have been deprecated.

How do I install PyNWB?
=======================

See the :ref:`install_users` for details.

