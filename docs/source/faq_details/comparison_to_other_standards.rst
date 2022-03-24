:orphan:

.. _comparison-to-other-standards:

How does NWB 2.0 compare to other neurodata standards?
------------------------------------------------------

What is the difference between NWB 2.0 and NWB 1.0?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While NWB 1.0 successfully created a comprehensive standard for neurophysiology, it lacked a reliable and rigorous software strategy and APIs, which made NWB(v1.0) hard to use and unreliable in practice. NWB 2.0 has been an effort to formalize and modularize the software components of NWB, and to build a sustainable software ecosystem that supports and accelerates collaboration between labs.

What is the difference between NWB and NIX?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:nix:`NIX <>` is another effort to standardize neurophysiology data. NIX defines a sophisticated, generic data model
for storage of annotated scientific datasets, with APIs in C++ and Python and bindings for Java and MATLAB. NIX uses HDF5, the same backend as NWB’s primary backend, and leverages its main advantages similar to NWB. As such, NIX provides important functionality towards building a FAIR data strategy, but the NIX data model by itself lacks specificity with regard to neurophysiology, leaving it up to the user to define appropriate schema to facilitate FAIR compliance. Due to this lack of specificity, NIX files can also be more varied in structure and naming conventions, which would make it difficult to aggregate across NIX datasets from different labs.

What is the difference between NWB and BIDS?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :bids:`Brain Imaging Data Standard (BIDS) <>` is a mature standard for representing neuroimaging data. Both NWB and BIDS emphasize building an ecosystem of tools for analyzing and visualization data. BIDS has quite a few impressive “BIDS apps,” which makes it a very powerful format that not only facilitates information exchange, but can also accelerate research. It differs from NWB in two main ways: approach and scope.

Approach
~~~~~~~~

NWB uses (primarily) HDF5 to represent hierarchical data within a single file, and concerns itself with organizing data for a single session. HDF5 is optimized for efficient handling of large data, but due to its efficient tooling, it usually requires specific HDF5 APIs to read this data, so there is some trade-off in accessibility for less technical users. In contrast, BIDS makes use of directory structure and naming conventions as a central part of the standard. It is used to organize data across an entire study including multiple subjects and recording sessions, and separates data sources and metadata into different files. Metadata is stored as JSON and TSV files, which are easily opened and edited using standard text editors.

Scope
~~~~~

:bids:`BIDS <>` handles neuroimaging (structural MRI, fMRI, PET, CT, DTI, etc.) and NWB handles neurophysiology (extracellular and intracellular electrophysiology, optical physiology, animal behavior, optogenetics, etc.). Both BIDS and NWB have mechanisms to extend the standard, so each has a well defined scope of its core and a less well defined scope of what types of extensions would be appropriate for the format. There are some cases where data could go in either, for instance with ECoG. In this case, we have worked with the development team of the corresponding BIDS extension (iEEG-BIDS) to make it possible to be mutually compatible with both BIDS and NWB by including NWB files in the BIDS directory and naming structure. This results in some duplication of metadata, but has the advantage of allowing a user to leverage both BIDS and NWB tools.

