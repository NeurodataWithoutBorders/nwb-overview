Neurodata Types
===============

The precise rules for how to store different types of data and the associated metadata are defined using **neurodata
types**. Different types of data have different neurodata types. Together, these neurodata type definitions
form the `NWB schema <https://nwb-schema.readthedocs.io/en/latest/>`_. The NWB schema defines over 60 different
neurodata types, which cover the most common data types in extracellular electrophysiology, intracellular
electrophysiology, optical physiology, and behavior.

Neurodata types act like classes in Object-Oriented Programming in that they can use inheritance (a neurodata type can
be a specialized child of another neurodata type) and composition (a neurodata type can contain other neurodata
types).

TimeSeries
-----------
The :ref:`nwb-schema:sec-TimeSeries` neurodata type defines how generic data values that change over time should be
stored. In particular, the `TimeSeries` type must contain a description,
an N-dimensional "data" dataset (array) where the first dimension is time, and either a 1-dimensional "timestamps"
dataset or both a sampling rate and starting time.

The :ref:`nwb-schema:sec-TimeSeries` neurodata type is the base type for many other neurodata types, such as the
:ref:`nwb-schema:sec-ElectricalSeries` for extracellular electrophysiology. `ElectricalSeries` inherits all of the
properties of `TimeSeries` but additionally specifies that the "data" dataset must be 2-dimensional, where the second
dimension is electrode, and it must contain an additional "electrodes" dataset with row indices into the "electrodes"
table of the NWB file to indicate which electrodes correspond to the second dimension of the "data" dataset.

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

All time values in a `TimeSeries` and other neurodata types must be stored in seconds relative to the
``timestamps_reference_time`` value, a datetime value stored at the root of the NWB file.
By default, this is the same as the ``session_start_time``,
another datetime value stored at the root of the NWB file.

DynamicTable
-------------
Tabular (table-like) data are stored in :ref:`hdmf-common-schema:sec-DynamicTable` objects,
which are column-based tables to which you can add custom columns.

Similar to `TimeSeries`, several neurodata types inherit from `DynamicTable` that are specialized
for particular types of data and specify particular required or optional columns.

.. seealso::
    For your reference, NWB defines the following main :ref:`hdmf-common-schema:sec-DynamicTable` subtypes:

    * :ref:`nwb-schema:sec-TimeIntervals`: stores trials, epochs, and associated metadata.
    * :ref:`nwb-schema:sec-Units`: stores spike times of sorted units and associated metadata.
    * :ref:`nwb-schema:sec-PlaneSegmentation`: stores regions of interest for optical imaging with associated
      metadata.



NWB is faced with the challenge
of supporting a large variety of different experiment types, so the data types and relationships
can get quite complex. For this reason, the NWB development team provides software to help users easily
and efficiently read and write NWB files. These software packages are described in the next section.
