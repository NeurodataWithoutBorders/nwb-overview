APIs
====

Two main APIs are supported for conveniently reading and writing NWB data: :pynwb-docs:`PyNWB <>` for Python and
:matnwb-src:`MatNWB <>` for MATLAB.

Like the NWB specification, the classes of these APIs
follow an object-oriented inheritance pattern, i.e., the PyNWB class :py:class:`~pynwb.base.TimeSeries`
serves as the base class for all other :py:class:`~pynwb.base.TimeSeries` types, such as,
:py:class:`~pynwb.ecephys.ElectricalSeries`, which itself may have further subtypes, e.g.,
:py:class:`~pynwb.ecephys.SpikeEventSeries`. The same is true for MatNWB.