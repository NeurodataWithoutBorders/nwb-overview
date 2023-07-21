# 2. Automatic NWB Conversions using NeuroConv

[NeuroConv](https://neuroconv.readthedocs.io/) is a library for automatic conversions from proprietary formats to NWB.
A gallery of all supported formats can be found
[here](https://neuroconv.readthedocs.io/en/main/conversion_examples_gallery/conversion_example_gallery.html).
If NeuroConv supports your source data format, this is the recommended approach, because it is easiest to
implement and automatically helps you adhere to best practices. For advanced usage of NeuroConv, including creating
conversions of ensembles of multiple data streams, see the
[NeuroConv User Guide](https://neuroconv.readthedocs.io/en/main/user_guide/user_guide.html).

Although NeuroConv supports many common formats, it may not support every type of source data you need.
If your source format is likely to be a common need in the community, for example the output of an acquisition
system or a popular data processing package, please use
[this form](https://github.com/catalystneuro/neuroconv/issues/new?assignees=&labels=enhancement%2Cdata+interfaces&template=format_request.yml&title=%5BNew+Format%5D%3A+)
to request support for this format. On the other hand, some data formats can be ad-hoc, particularly data about task and
behavior. In this case, proceed to the next section for detailed tutorials on using the PyNWB API to manually add this
data to the NWB file.