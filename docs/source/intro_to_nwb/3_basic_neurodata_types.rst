Basic Neurodata Types
=====================

Containers
------------------
TODO

TimeSeries
------------------
)

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
