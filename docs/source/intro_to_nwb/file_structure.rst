Anatomy of an NWB File
======================

First, we need to understand a few basic concepts of how an NWB is structured.

The goal of NWB is to package all of the data and metadata of a particular session
into a single file in a standardized way.
This includes the neurophysiology data itself, but also includes other data such
as information about the data acquisition, experiment design, experimental subject,
and behavior of that subject. The NWB schema defines data structures for
the most common types of data in neurophysiology. NWB currently covers
the following experiment types:

* extracellular electrophysiology (e.g., Neuropixel probes)
* intracellular electrophysiology (e.g., patch clamping)
* optical physiology (e.g., two-photon imaging)

.. image:: /img/nwb_overview.png

File hierarchy
--------------

An NWB file consists of four basic types:

* groups, which are like folders or directories in a filesystem and can contain any of the basic types
* datasets, which are N-dimensional arrays
* attributes, which are small metadata values attached to a group or dataset, like folder/file properties in a
  filesystem
* links, which point to a group or dataset, like shortcuts or aliases in a filesystem

TODO: add image

Raw data
--------

Raw data are stored in NWB in containers placed in the ``acquisition`` group.
In PyNWB, you can add raw data to an NWB file using NWBFile.add_acquisition.
In MatNWB, you can add raw data to an NWB file using

See [TODO link] for more details.

Processed data
--------------

Processed data, for example, the extracted fluorescence time series
from ROIs in calcium imaging data, are stored in NWB in containers
within a ``ProcessingModule`` container placed in the ``processing`` group.
Any scripts or software that process raw data and generate processed
data should store the results within a ``ProcessingModule``.

The name of the ``ProcessingModule`` reflects the type of processed data
within it.

.. list-table::
    :header-rows: 1

    * - Type of processed data
      - Name of ``ProcessingModule``
    * - extracellular electrophysiology
      - "ecephys"
    * - intracellular electrophysiology
      - "icephys"
    * - optical physiology
      - "ophys"
    * - behavior
      - "behavior"

Containers
------------------

TimeSeries
------------------

DynamicTable
------------------

Data values in NWB
------------------

Time values
^^^^^^^^^^^
All time values must be stored in seconds relative to the
``timestamp_reference_time`` value, a datetime value stored at the root
of the NWB file.

Units of measurement
^^^^^^^^^^^^^^^^^^^^
All measurement data (e.g., electrical recordings, distances, frequencies)
must be stored in SI units (e.g., volts, meters, hertz).






NWB is faced with the challenge
of supporting a large variety of different experiment types, so the data types and relationships
can get quite complex. For this reason the NWB development team provides APIs to help users easily
and efficiently read and write NWB files. These APIs are described in the next section.
