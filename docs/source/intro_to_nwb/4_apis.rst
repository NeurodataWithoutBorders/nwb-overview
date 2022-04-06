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

To learn more about how to install the NWB APIs and use them to read and write NWB data, please
see their respective documentation:

* :pynwb-docs:`PyNWB <>` for Python
* :matnwb-src:`MatNWB <>` for MATLAB

To learn more about the NWB schema, please see the :nwb-schema-docs:`NWB Schema <>` documentation.

To learn how to convert your data to NWB, See :ref:`conversion_home`.
