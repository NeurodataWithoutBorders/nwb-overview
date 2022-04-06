Neurodata Types
===============

The precise rules for how to store different types of data and the associated metadata are defined using **neurodata
types**. Different types of data get different neurodata types, which are defined in the `NWB specification
<https://nwb-schema.readthedocs.io/en/latest/>`_.
Neurodata types act like classes in Object-Oriented Programming in that they can use inheritance (a neurodata type can
be a specialized child of another neurodata type) and composition (a neurodata type can contain other neurodata
types).

TimeSeries
-----------
:ref:`nwb-schema:sec-TimeSeries` objects store time series data and correspond to the *TimeSeries* specification
provided by the NWB schema.

Like the NWB specification, PyNWB :py:class:`~pynwb.base.TimeSeries` objects
follow an object-oriented inheritance pattern, i.e., the PyNWB class :py:class:`~pynwb.base.TimeSeries`
serves as the base class for all other PyNWB :py:class:`~pynwb.base.TimeSeries` types, such as,
:py:class:`~pynwb.ecephys.ElectricalSeries`, which itself may have further subtypes, e.g.,
:py:class:`~pynwb.ecephys.SpikeEventSeries`. The same is true for MatNWB.

.. seealso::
    For your reference, NWB defines the following main :ref:`nwb-schema:sec-TimeSeries` subtypes:

    * **Extracellular electrophysiology:**
      :ref:`nwb-schema:sec-ElectricalSeries`, :ref:`nwb-schema:sec-SpikeEventSeries`
    * **Intracellular electrophysiology:**
      :ref:`nwb-schema:sec-PatchClampSeries` is the base type for all intracellular time series, which
      is further refined into subtypes depending on the type of recording:
      :ref:`nwb-schema:sec-CurrentClampSeries`,
      :ref:`nwb-schema:sec-IZeroClampSeries`,
      :ref:`nwb-schema:sec-CurrentClampStimulusSeries`,
      :ref:`nwb-schema:sec-VoltageClampSeries`,
      :ref:`nwb-schema:sec-VoltageClampStimulusSeries`.
    * **Optical physiology and imaging:** :ref:`nwb-schema:sec-ImageSeries` is the base type
      for image recordings and is further refined by the
      :ref:`nwb-schema:sec-ImageMaskSeries`,
      :ref:`nwb-schema:sec-OpticalSeries`, and
      :ref:`nwb-schema:sec-TwoPhotonSeries` types.
      Other related time series types are:
      :ref:`nwb-schema:sec-IndexSeries` and
      :ref:`nwb-schema:sec-RoiResponseSeries`.
    * **Others:** :ref:`nwb-schema:sec-OptogeneticSeries`,
      :ref:`nwb-schema:sec-SpatialSeries`,
      :ref:`nwb-schema:sec-DecompositionSeries`,
      :ref:`nwb-schema:sec-AnnotationSeries`,
      :ref:`nwb-schema:sec-AbstractFeatureSeries`, and
      :ref:`nwb-schema:sec-IntervalSeries`.

DynamicTable
-------------
Tabular (table-like) data are stored in :ref:`hdmf-common-schema:sec-DynamicTable` objects,
which are column-based tables to which you can add custom columns.

.. seealso::
    For your reference, NWB defines the following main :ref:`hdmf-common-schema:sec-DynamicTable` subtypes:

    * :ref:`nwb-schema:sec-TimeIntervals`: stores trials, epochs, and associated metadata.
    * :ref:`nwb-schema:sec-Units`: stores spike times of sorted units and associated metadata.
    * :ref:`nwb-schema:sec-PlaneSegmentation`: stores regions of interest for optical imaging with associated
      metadata.

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
