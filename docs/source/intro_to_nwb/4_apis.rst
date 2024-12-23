Software for reading and writing NWB data
=========================================

NWB provides two APIs for easily reading and writing NWB data: :pynwb-docs:`PyNWB <>` for Python and
:matnwb-src:`MatNWB <>` for MATLAB.

Each neurodata type defined in the NWB schema has a corresponding class in both PyNWB and MatNWB.
Like neurodata types, these classes relate to each other through inheritance and composition.
For example, the PyNWB class :py:class:`~pynwb.base.TimeSeries`
serves as the base class (superclass) for more specialized time series classes, such as,
:py:class:`~pynwb.ecephys.ElectricalSeries`, and a :py:class:`~pynwb.ecephys.LFP` object can contain one or more
:py:class:`~pynwb.ecephys.ElectricalSeries` objects, just like how the corresponding neurodata types
are defined in the NWB schema.

Next steps
==========

To learn more about:

* how to install and use the APIs, see the :pynwb-docs:`PyNWB <>` and  :matnwb-src:`MatNWB <>` documentation
* how to convert your data to NWB, see :ref:`conversion_home`.
* the broad range of core tools available for NWB see the :ref:`core-tools-home`
* community tools available for NWB see the :ref:`analysistools-home` section.
* the NWB schema, please see the :nwb-schema-docs:`NWB Schema <>` documentation.

Navigating the NWB Documentation
--------------------------------

NWB defines a large software ecosystem and as such there are many different documentation resources available depending
on what aspect of NWB and what type of information you want to learn more about. The following sketch provides an
overview of the main areas of the NWB documentation. As we navigate from the top of the pyramid to the
bottom, the level of detail and depth of the documentation increases. Most end-users will typically only interact with
the top half of the pyramid. If you are new to NWB and want to learn more; good news you are at the right place!

.. image:: ../img/nwb_documentation_overview.png
    :class: align-center
    :width: 600

At the top (dark blue), we have the :nwb-main:`NWB.org <>` website, which focuses on the NWB project at large and provides
information about the overall organization, goals, community, and policies of the NWB project and provides a first
entry point to NWB.

Next we have the :ref:`NWB Overview <main-home>` (i.e., this website) (black), which serves as an entry point for
researchers and developers interested in using NWB and in learning more about the NWB software ecosystem.

A growing collection of :ref:`analysistools-home` (gray) developed by the neurophysiology community along with a
broad range of :ref:`core tools <core-tools-home>` (red) help users with conversion, extension, validation and use of
NWB data files. Commonly, these tools build on the :pynwb-docs:`PyNWB (Python) <>` and :matnwb-docs:`MatNWB (MATLAB) <>`
reference APIs (lilac) to read and write NWB files. Each of the APIs and tools provides their own in-depth
tutorials and documentation to help guide users in adopting and using the software.

Underlying all of this, is the :nwb-schema-docs:`NWB Format Specification <>`, which formally
defines and governs the NWB data standard.

Last but not least, NWB provides and builds on a broad range of data modeling tools and technologies (light blue),
e.g., :hdmf-docs:`HDMF <>` and the :hdmf-docs:`HDMF Common Schema<>`, the :ndx-catalog:`Neurodata Extension Catalog <>`,
as well as the :nwb-schema-language-docs:`specification language <>` and :nwb-storage-docs:`data storage <>`
specifications.
