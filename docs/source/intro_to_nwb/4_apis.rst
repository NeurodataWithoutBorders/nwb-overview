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
----------
See the :pynwb-docs:`PyNWB <>` and  :matnwb-src:`MatNWB <>` documentation to learn more about the tools and how to install the APIs.

To learn more about the broad range of core tools available for NWB see the :ref:`core-tools-home` and
:ref:`analysistools-home` sections

To learn more about the NWB schema, please see the :nwb-schema-docs:`NWB Schema <>` documentation.

To learn how to convert your data to NWB, See :ref:`conversion_home`.
