:orphan:

.. _why_hdf5:

Why use HDF5 as the primary backend for NWB?
--------------------------------------------

:hdf5:`HDF5 <>` has three main features that make it ideal as our primary backend:

**1. HDF5 has sophisticated structures for organizing complex hierarchical data and metadata, which is critical for handling the complexity and diversity of neurophysiology metadata.**

HDF5 is one of the few standards that supports the four data primitives of the HDMF schema language: Group, Dataset, Attribute and Link. Each of these structures are essential in the full representation of critical metadata. Groups allow NWB to organize information hierarchically. Datasets allow NWB to store the large data blocks of measurement time series data. Attributes allow those datasets to be annotated with metadata necessary for reanalysis such as the units of measurement of that data and conversion factor. Links allow us to store data efficiently and avoid data duplication, and they allow us to create formal links between data elements.

**2. HDF5 is a mature standard with support in a plethora of programming languages and multiple storage backends.**

We have chosen HDF5 to maximize the accessibility of data stored in NWB. In order for NWB to support the diverse needs of the community (i.e., to truly be “without borders”) we need to support a variety of access patterns. HDF5 has well-established APIs in many scientific programming languages, including C, Python, MATLAB, R, Julia, Java, and JavaScript. This list includes not only the major programming languages currently used by most neuroscientists (Python, MATLAB, and in some cases C and R) but also newer programming languages like Julia. By leveraging the robust community and support infrastructure behind HDF5, we can continue to achieve readability in diverse languages, far more than would be practical if we were to develop custom data access APIs in each language ourselves. Furthermore, HDF5 prioritizes long-term support, which includes technical support for any bugs, and backwards compatibility of the HDF5 API.

Another important feature of HDF5 is the ability to store it in different backends. A new driver, “ros3”, allows HDF5 files to be opened, read, and streamed directly from an S3 bucket, which is a common format for cloud storage.

**3. HDF5 supports random access of chunked and compressed datasets, which is critical for handling the volume of data.**

As recordings enter the TB scale, it is essential that we use a backend storage solution that supports both compression and random access. When large datasets are saved to disk, it is best to use lossless compression, which leverages patterns in the data to reduce the file size without changing the data values. HDF5 natively supports compressing datasets on write and decompressing datasets on read using GZIP (like “unarchiving” a file downloaded from the internet). Another important feature for large datasets is random access, which means that you can access any value within the datasets without reading all the values. If you were to apply GZIP to the entire dataset all at once, then it would require you to decompress the entire dataset and remove the capability for random access. HDF5 solves this problem by first splitting large datasets into “chunks” and compressing each of these chunks individually. This way when values of a particular region of the dataset are requested, only the chunks that contain requested data need to be decompressed. HDF5 has a sophisticated infrastructure for managing chunks of datasets and applying compression/decompression, removing these lower-level concerns from a data user who is reading the data.

These features have proven to be very important for archiving large datasets. For instance, in raw data from Neuropixel recordings, it has been found to reduce the file size by up to 60%. As datasets grow in volume and in number, it will become increasingly important to utilize good data engineering principles to manage them at scale.

Alternative backends
---------------------
Below, we briefly explain the pros and cons of alternative storage formats. Depending on the particular application and storage needs, different backends are often preferable. In particular as part of :hdmf-docs:`HDMF <>`, teams are exploring the use of alternate storage solutions with NWB. For the broader NWB community, we have found that HDF5 provides a good standard solution for most common use cases.

Zarr
^^^^

:zarr:`Zarr <>` supports compression and chunking like HDF5. Zarr is the standard we have found that comes closest to HDF5’s level of support for complex hierarchical data structures. The :bdg-link-primary:`HDMF Zarr<https://hdmf-zarr.readthedocs.io>` library implements a Zarr backend for HDMF and provides convenience classes for integrating Zarr with the  :bdg-link-primary:`PyNWB <https://pynwb.readthedocs.io/en/stable/>` Python API for NWB to support writing of NWB files to Zarr. Using Zarr, the NWB file is not stored as a single file, but as a collection many files organized into folders. This storage scheme has some key advantageous when using object-based storage solutions, e.g., cloud-based storage in AWS. Some main limitations of Zarr for NWB are: 1) Zarr only supports Python and the neuroscience community requires APIs in MATLAB and other languages, 2) HDF5 is a much more mature standard with a track record for long-term accessibility but the Zarr community is growing, 3) transferring Zarr files requires moving lots of small files, 4) Zarr does not support Links and References so that :hdmf-z-docs:`HDMF Zarr <>` must implement custom solutions to support this important feature for NWB. Whether HDF5 or Zarr is the right solution for you depends heavily on your use case.

LINDI
^^^^^

The :lindi-src:`Linked Data Interface (LINDI) <>` provides a JSON representation of NWB data where the large data chunks are stored separately from the main metadata. This enables efficient storage, composition, and sharing of NWB files on cloud systems such as DANDI without duplicating the large data blobs. LINDI can be used to index existing NWB HDF5 files to help speed-up remote access to HDF5 files stored in the cloud. LINDI provides dropin `LindiH5pyFile` feature such that LINDI files can be read via `PyNWB` using the standard `NWBHDF5IO` backend. LINDI is currently under development and should not yet be used in practice.


Other alternative storage formats
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following alternative formats are not currently supported by NWB.

Binary files (.dat)
~~~~~~~~~~~~~~~~~~~

Binary files do not allow for complex hierarchical data including Groups, Attributes, and Links. They also do not allow for chunking and compression, which makes them poorly suited for efficient handling of large data files. Furthermore, there is metadata needed to interpret binary files that can be missing, including shape, data type, and endianness. Zarr is an approach that uses binary files and deals with these limitations, using folders and json files to create a hierarchical structure that can manage data chunks and specify the essential parameters of binary files. See our response to Zarr.

Relational database (e.g. SQL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :hdmf-specification-language:`HDMF specification language <>` is inherently hierarchical, not tabular, and we
need a storage layer that can express the hierarchical nature of the data as well. There are some approaches for
mapping between relational tables and hierarchical structures such as object relational mappers, but this is not as
good of a solution as using a storage layer that is hierarchical by nature.

While we think relational databases are not ideal as an NWB backend, we do recognize that they can be a powerful
choice for storing scientific data because they enforce formal relationships between data and enable flexible,
complex queries. If you are interested in using relational databases for neuroscience research, we would recommend
exploring :datajoint:`DataJoint <>`, an open-source framework for programming scientific databases with computational
workflows with APIs in MATLAB and Python. :datajoint-elements:`DataJoint Elements <>` is a collection of curated
modules for assembling workflows for the major modalities of neurophysiology experiments. The NWB team is
collaborating with DataJoint to build import/export functionality between DataJoint Elements and NWB files. For labs
interested in leveraging the benefits of relational databases and NWB, using DataJoint internally and using NWB to
archive and share data could provide the best of both worlds.


