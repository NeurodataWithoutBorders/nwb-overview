.. _extensions-catalog:

**********************************
NWB Enhancement Proposals (NWBEPs)
**********************************

The NWB data standard is not static but evolves to adapt to changing needs from the neuroscience community,
clarify ambiguities, and fix bugs, among others. Users can propose smaller changes, such as improvements to
documentation or addition of a new optional field to an existing data type, on the
:nwb-schema-src:`NWB Schema GitHub repository <>`. Users can propose larger changes, such as addition of
several new data types to support a new data modality, or a major restructuring of existing data types,
through NWB Enhancement Proposals (NWBEPs). NWBEPs are often collaborative and led by members of
the community to address a significant need by the
community.

.. note::

    The :ndx-catalog:`NDX Catalog website <>` contains published
    extensions created by the community. Before creating your own extension,
    we recommend that you explore the Catalog to make sure that someone has
    not already created an extension that suits your needs or that you could
    build off of. Also see :ref:`extension-publishing-ndxcatalog` for details
    on how to publish your own extension in the NDX Catalog.

Current NWBEPs
==============

.. list-table:: **NWBEPs**
   :widths: 15 45 25 15
   :header-rows: 1

   * - NWBEP
     - Title
     - Lead
     - URLs
   * - NWBEP001
     - Events and TTL Data
     - Ryan Ly
     - `Google Doc <https://docs.google.com/document/d/1qcsjyFVX9oI_746RdMoDdmQPu940s0YtDjb1en1Xtdw/edit?usp=sharing>`__
   * - NWBEP002
     - Probe devices and channel mapping in extracellular ephys
     - Alessio Buccino
     - `Google Doc <https://docs.google.com/document/d/1q-haFEEHEgZpRoCzzQsuSWCKN4QfMsTzLnlptLaf-yw/edit?usp=sharing>`__
   * - NWBEP003
     - Multichannel volumetric imaging
     - Daniel Sprague
     - `Google Doc <https://docs.google.com/document/d/1IhhKwpPoXzPZTNXH7zCU_At4Py17aNJ6lYP_XaGX0wo/edit?usp=sharing>`__


.. note::

    To add a new NWBEP to this list, please file an issue on the :nwb-overview-src:`NWB Overview GitHub repo <>`
    or create a pull request that modifies the table.

Related Policies
=================

The following list shows NWB policies related to community-driven development and integration
of new neuroscience technologies with NWB

- `Sharing Guidelines: requirements and strategy for sharing format extensions for NWB <https://docs.google.com/document/d/e/2PACX-1vRxbT-EEAyYbQL3P0TREpySJkMhV7ea2-aRO75_s4PhqzxnJa9p-s0SzVWrlkzEBaTw82bgzZBtxEuj/pub>`_
- `Sharing Strategies: standard practices and strategies for sharing format extensions for NWB <https://docs.google.com/document/d/e/2PACX-1vSpLLPQV2XlfT-Qnpi_aqLPJzRjCko6Ur0U5COCEAQg5uLIN0h5vej5EPtsf6UNx1qiAIKXPiIveSWo/pub>`_
- `Versioning Guidelines: requirements and strategy for versioning namespaces for the NWB core schema and extensions <https://docs.google.com/document/d/e/2PACX-1vSH72zNSUBToVcZDRI4gF7h15ImWRffvj-ju1oEbxggPrEFJd5L6GQc-fRiVmIi42U742tgjcRk65jv/pub>`_

NWBEP Submission and Review Process
===================================

Review of NWBEPs for acceptance to the NWB core data standard is led by the
:nwb-tab:`NWB Technical Advisory Board (TAB) <>`
and involves several phases. To submit a NWBEP for review and explore previous NWBEP reviews, see the
:nwbep-review:`NWBEP Review GitHub repo <>`. For more information on the NWBEP process, see the following links:

- `Proposal Review Process: process by which extensions to the NWB core standard are proposed, evaluated, reviewed, and accepted <https://docs.google.com/document/d/e/2PACX-1vR7v4ixgnaCsJSbKji5eGWxb5muzV1M82zA-D2IswZD_KOt7HiUjcXKpTko0lqcBAD-MTd44rqFCf-V/pub>`_
- `Working Groups for Evaluating NWBEPs Policy: process for evaluation and review of NWB Extension Proposals (NWBEPs) by a review working group (RWG) to provide guidance and a formal framework for RWG members. <https://docs.google.com/document/d/e/2PACX-1vTpDnWFpD2YDuYKXzd-6svH6ceXNBz4wOauoZivvZpQgLPYBz6yv7-eihJceBtgGTDV_TcMX9xboNsm/pub>`_
- `NWBEP Evaluation Form <https://docs.google.com/document/d/1g8NWD-5q8SBLvoedOm4jWBXvY6aOG7VSAZ0owjjTUkY/edit>`_
