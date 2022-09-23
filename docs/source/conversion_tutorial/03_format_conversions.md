# 3. Automated Conversions using NeuroConv

To make converting to NWB faster and less laborious (for our own team and for others),
and manage the volume and variety of neurophysiology data, we have developed 
a system of conversion tools for converting different proprietary data formats
to NWB. [NeuroConv](https://neuroconv.readthedocs.io/) relies on two tiers
of structure, represented by the two main classes in the package: [``DataInterface``](https://neuroconv.readthedocs.io/en/main/user_guide/datainterfaces.html)
and [``NWBConverter``](https://neuroconv.readthedocs.io/en/main/user_guide/nwbconverter.html). 

``DataInterface`` provides a unified API for converting data from
any one data format, such as raw data from an acquisition system or processed
data from spike sorting or image segmentation software. ``DataInterface``s load the
raw data in an efficient way, extract metadata, and write  this information properly 
into NWB. ``DataInterfaces``cover a 
[large variety of different source formats](https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/conversion_example_gallery.html).

Users often need to write data from multiple sources. An example would be an 
extracellular electrophysiology experiment where the user needs to write raw
electrophysiology, processed spike sorting results, and behavioral data, all to
the same NWB file. The ``NWBConverter`` class was created to aggregate data between
``DataInterface``s, managing the aggregation of metadata, and the synchronization
of different data sources.