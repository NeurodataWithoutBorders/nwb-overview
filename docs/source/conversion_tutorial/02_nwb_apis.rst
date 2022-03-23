2. NWB APIs: PyNWB & MatNWB
===========================

The NWB team develops and supports APIs in Python
(`PyNWB <https://pynwb.readthedocs.io/en/stable/>`_)
and MATLAB (`MatNWB <https://github.com/NeurodataWithoutBorders/matnwb>`_),
which guide users in reading and writing NWB files.
The features of these two APIs are very similar to each other, so choose
whichever is more convenient. Note that most of the high-level conversion
tools use PyNWB, but the APIs are interchangeable and there should be no
problem with writing data using MatNWB even if you plan to read it using
PyNWB later (or vice versa). Below is a table of the available tutorials
illustrating the end-to-end conversion of common data types in each imaging
modality:

.. list-table::
    :header-rows: 1

    * -
      - PyNWB
      - MatNWB
    * - Reading NWB files
      - `Jupyter notebook <https://github.com/NeurodataWithoutBorders/nwb_tutorial/blob/master/HCK09/pynwb_read_demo.ipynb>`__
      - `15 min video <https://www.youtube.com/watch?v=ig_Xv2bTxjs&ab_channel=NeurodataWithoutBorders>`__

        `MATLAB Live Script <https://github.com/NeurodataWithoutBorders/nwb_tutorial/blob/master/HCK09/matnwb_read_demo.mlx?raw=true>`__
    * - Writing extracellular electrophysiology
      - `23 min video <https://www.youtube.com/watch?v=rlywed3ar-s&ab_channel=NeurodataWithoutBorders>`__

        `Jupyter notebook <https://github.com/NeurodataWithoutBorders/nwb_tutorial/blob/master/HCK08/ecephys_tutorial.ipynb>`__
      - `46 min video <https://www.youtube.com/watch?v=W8t4_quIl1k&ab_channel=NeurodataWithoutBorders>`__

        `Written tutorial <https://neurodatawithoutborders.github.io/matnwb/tutorials/html/ecephys.html>`__
    * - Writing intracellular electrophysiology
      - `Jupyter notebook <https://github.com/NeurodataWithoutBorders/nwb_tutorial/blob/master/HCK08/ICEphys_basic_hck8.ipynb>`__
      - `Written tutorial <https://neurodatawithoutborders.github.io/matnwb/tutorials/html/icephys.html>`__
    * - Writing optical physiology
      - `31 min video <https://www.youtube.com/watch?v=HPjSxBjdFpM&ab_channel=NeurodataWithoutBorders>`__

        `Jupyter notebook <https://github.com/NeurodataWithoutBorders/nwb_tutorial/blob/master/HCK08/ophys_tutorial.ipynb>`__
      - `39 min video <https://www.youtube.com/watch?v=OBidHdocnTc&ab_channel=NeurodataWithoutBorders>`__

        `Written tutorial <https://neurodatawithoutborders.github.io/matnwb/tutorials/html/ophys.html>`__
    * - Advanced write
      - `26 min video <https://www.youtube.com/watch?v=wduZHfNOaNg&ab_channel=NeurodataWithoutBorders>`__
      - `16 min video <https://www.youtube.com/watch?v=PIE_F4iVv98&ab_channel=NeurodataWithoutBorders>`__

        `Written tutorial <https://neurodatawithoutborders.github.io/matnwb/tutorials/html/dataPipe.html>`__

These tutorials walk you through the most common data types of each of the modalities.
With the tutorials for domain-specific conversion, extensions, advanced I/O,
and the documentation for proprietary formats, you have all of the tools to
create your own conversion. However, writing a full-fledged conversion script from
the ground up with MatNWB and PyNWB is time-intensive, error-prone, and requires
detailed knowledge of the source format. That is why, in the next section, we
will introduce automated conversion tools that work on a large number of supported
proprietary formats.
