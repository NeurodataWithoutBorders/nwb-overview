Neurodata Types
===============

The precise rules for how to store different types of data and the associated metadata are defined using *neurodata
types*. Different types of data get different *neurodata types*, which are defined in the `NWB specification
<https://nwb-schema.readthedocs.io/en/latest/>`_.
*neurodata types* act like classes in Object Oriented Programming in that use inheritance (a *neurodata type* can
be a child of another, which is more specialized), and composition (a *neurodata type* can contain other *neurodata
types*.)

TimeSeries
-----------
:nwb-schema:ref:`sec-TimeSeries` objects store time series data and correspond to the *TimeSeries* specifications
provided by the NWB schema. All

Like the NWB specification, :py:class:`~pynwb.base.TimeSeries` PyNWB objects
follow an object-oriented inheritance pattern, i.e., the class :py:class:`~pynwb.base.TimeSeries`
serves as the base class for all other :py:class:`~pynwb.base.TimeSeries` types, such as,
:py:class:`~pynwb.ecephys.ElectricalSeries`, which itself may have further subtypes, e.g.,
:py:class:`~pynwb.ecephys.SpikeEventSeries` (the same is true for MatNWB).

.. seealso::
    For your reference, NWB defines the following main :nwb-schema:ref:`sec-TimeSeries` subtypes:

    * **Extracellular electrophysiology:**
      :nwb-schema:ref:`sec-ElectricalSeries`, :nwb-schema:ref:`sec-SpikeEventSeries`
    * **Intracellular electrophysiology:**
      :nwb-schema:ref:`sec-PatchClampSeries` is the base type for all intracellular time series, which
      is further refined into subtypes depending on the type of recording:
      :nwb-schema:ref:`sec-CurrentClampSeries`,
      :nwb-schema:ref:`sec-IZeroClampSeries`,
      :nwb-schema:ref:`sec-CurrentClampStimulusSeries`,
      :nwb-schema:ref:`sec-VoltageClampSeries`,
      :nwb-schema:ref:`sec-VoltageClampStimulusSeries`.
    * **Optical physiology and imaging:** :nwb-schema:ref:`sec-ImageSeries` is the base type
      for image recordings and is further refined by the
      :nwb-schema:ref:`sec-ImageMaskSeries`,
      :nwb-schema:ref:`sec-OpticalSeries`, and
      :nwb-schema:ref:`sec-TwoPhotonSeries` types.
      Other related time series types are:
      :nwb-schema:ref:`sec-IndexSeries` and
      :nwb-schema:ref:`sec-RoiResponseSeries`.
    * **Others:** :nwb-schema:ref:`sec-OptogeneticSeries`,
      :nwb-schema:ref:`sec-SpatialSeries`,
      :nwb-schema:ref:`sec-DecompositionSeries`,
      :nwb-schema:ref:`sec-AnnotationSeries`,
      :nwb-schema:ref:`sec-AbstractFeatureSeries`, and
      :nwb-schema:ref:`sec-IntervalSeries`.

DynamicTable
------------------
TODOO

Data values in NWB
------------------

Time values
^^^^^^^^^^^
All time values must be stored in seconds relative to the
``timestamps_reference_time`` value, a datetime value stored at the root
of the NWB file. By default, this is the same as the ``session_start_time``,
a datetime value also stored at the root of the NWB file.

Units of measurement
^^^^^^^^^^^^^^^^^^^^
All measurement data (e.g., electrical recordings, distances, frequencies)
must be stored in SI units (e.g., volts, meters, hertz).






NWB is faced with the challenge
of supporting a large variety of different experiment types, so the data types and relationships
can get quite complex. For this reason the NWB development team provides APIs to help users easily
and efficiently read and write NWB files. These APIs are described in the next section.
