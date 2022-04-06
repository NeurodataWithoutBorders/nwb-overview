Software for reading and writing NWB data
=========================================

NWB provides two APIs for conveniently reading and writing NWB data: :pynwb-docs:`PyNWB <>` for Python and
:matnwb-src:`MatNWB <>` for MATLAB.

Like the NWB specification, the classes of these APIs
follow an object-oriented inheritance pattern, i.e., the PyNWB class :py:class:`~pynwb.base.TimeSeries`
serves as the base class for all other :py:class:`~pynwb.base.TimeSeries` types, such as,
:py:class:`~pynwb.ecephys.ElectricalSeries`. The same is true for MatNWB.

To learn more about how to install one of the NWB APIs and use it to read and write NWB data, please
see their respective documentation:

* :pynwb-docs:`PyNWB <>` for Python
* :matnwb-src:`MatNWB <>` for MATLAB

To learn more about the NWB specification, please see the :nwb-schema-docs:`NWB Schema <>` documentation.

To learn how to convert your data to NWB, continue onto the next section.
