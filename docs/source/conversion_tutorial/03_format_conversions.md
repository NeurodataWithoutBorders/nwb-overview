# 3. Automated Conversions using NWB Conversion Tools

To make converting to NWB faster and less laborious (for our own team and for others),
and manage the volume and variety of neurophysiology data, we have developed 
a system of conversion tools for converting different proprietary data formats
to NWB. NWB Conversion Tools relies on two tiers
of structure, represented by the two main classes in the package: ``DataInterface``
and ``NWBConverter``. 

``DataInterface`` provides a unified API for converting data from
any one data format, such as raw data from an acquisition system or processed
data from spike sorting or image segmentation software. ``DataInterface``s load the
raw data in an efficient way, extract metadata, and contain logic for how to write
this information properly into NWB. ``DataInterfaces`` cover a large variety of
different source formats (TODO: create list of supported types of nwb conversion tools docs).

Users often need to write data from multiple sources. An example would be an 
extracellular electrophysiology experiment where the user needs to write raw
electrophysiology, processed spike sorting results, and behavioral data, all to
the same NWB file. The ``NWBConverter`` class was created to aggregate data between
``DataInterface``s, managing the aggregation of metadata, and the synchronization
of different data sources.