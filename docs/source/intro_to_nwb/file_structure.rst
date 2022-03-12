Anatomy of an NWB File
======================

First, we need to understand a few basic concepts of how an NWB is structured.

The goal of NWB is to package all of the data and metadata of a particular session
into a single file in a standardized way.
This includes the neurophysiology data itself, but also includes other data such
as information about the data acquisition, experiment design, experimental subject,
and behavior of that subject. The NWB schema defines data structures for
the most common types of neurophysiology data. NWB currently supports
the following experiment types:

* extracellular electrophysiology (e.g., Neuropixel probes)
* intracellular electrophysiology (e.g., patch clamping)
* optical physiology (e.g., two-photon imaging)

.. image:: /img/nwb_overview.png

An NWB file is an HDF5 file that is structured in a particular way and has the `.nwb` file extension.
HDF5 files use a files-and-folders-like structure that allows you to organize data in a folder hierarchy,
as you might do with files on your computer. An HDF5 file can be thought of as a zipped folder that
contains subfolders and datasets within each subfolder. Metadata can be embedded within the file,
which allows the file to be self-describing and easy for humans and machines to process.

If you inspect an NWB file, you would see something like the following::

  └── sub-npI1_ses-20190413_behavior+ecephys.nwb
      ├── acquisition
      │   └── ElectricalSeries
      │       ├── data
      │       ├── electrodes
      │       └── starting_time
      ├── general
      │   ├── devices
      │   ├── extracellular_ephys
      │   │   ├── Shank1
      │   │   └── electrodes
      │   ├── institution
      │   ├── lab
      │   └── subject
      ├── intervals
      │   └── trials
      ├── processing
      │   ├── behavior
      │   │   ├── Position
      │   │   │   └── position
      │   │   │       ├── data
      │   │   │       ├── reference_frame
      │   │   │       └── timestamps
      │   │   └── licks
      │   │       └── timestamps
      │   └── ecephys
      │       └── LFP
      │           └── LFP
      │               ├── data
      │               ├── electrodes
      │               └── starting_time
      ├── session_description
      └── session_start_time

At a glance, you can see that there are datasets within the file that represent
acquired (raw) electrical data, processed position data, and processed LFP data.
There are also metadata fields that represent the institution and lab where the data was
collected, a description of the session, and the session start time.

An NWB file often consists of many different data and metadata so as to provide a complete
representation of the data that was collected in a session. This may seem overwhelming
at first, but NWB provides tools to make it easy for you to read and write data in the NWB format,
as well as inspect and visualize your NWB data. Community tools leverage the standardized
structure of an NWB file to find relevant data and metadata for data processing, analysis,
and visualization. And once you understand the structure of an NWB file, you can open any
NWB file and quickly make sense of its contents.

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

Raw data are stored in NWB in containers placed in the ``acquisition`` group
at the root of the NWB file.
In PyNWB, you can add raw data to an NWB file using NWBFile.add_acquisition.
In MatNWB, you can add raw data to an NWB file using

See [TODO link] for more details.

Processed data
--------------

Processed data, for example, the extracted fluorescence time series
from ROIs in calcium imaging data, are stored in NWB in containers
within a ``ProcessingModule`` container placed in the ``processing`` group
at the root of the NWB file.
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
