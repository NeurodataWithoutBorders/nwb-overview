Anatomy of an NWB File
----------------------

NWB organizes data into different groups depending on the type of data. Groups can be thought of
as folders within the file. Here are some of the groups within an :py:class:`~pynwb.file.NWBFile` and the types of data
they are intended to store:

* **acquisition**: raw, acquired data that should never change
* **processing**: processed data, typically the results of preprocessing algorithms and could change
* **analysis**: results of data analysis
* **stimuli**: stimuli used in the experiment (e.g., images, videos, light pulses)