Software for reading and writing NWB data
=========================================

NWB provides two APIs for conveniently reading and writing NWB data: :pynwb-docs:`PyNWB <>` for Python and
:matnwb-src:`MatNWB <>` for MATLAB.

Like the NWB specification, the classes of these APIs
follow an object-oriented inheritance pattern, i.e., the PyNWB class :py:class:`~pynwb.base.TimeSeries`
serves as the base class for all other :py:class:`~pynwb.base.TimeSeries` types, such as,
:py:class:`~pynwb.ecephys.ElectricalSeries`. The same is true for MatNWB.

Next, follow the :ref:`NWB Conversion Tutorial <conversion_home>` to learn how to convert your
data to NWB.
