.. _analysistools-neurosift:

Neurosift
---------

.. short_description_start

:ref:`analysistools-neurosift` provides interactive neuroscience visualizations in the browser. Neurosift caters to both individual users through its local mode, allowing the visualization of views directly from your device, as well as a remote access function for presenting your findings to other users on different machines.
:bdg-link-primary:`Source <https://github.com/flatironinstitute/neurosift>`

.. image:: https://img.shields.io/github/stars/flatironinstitute/neurosift?style=social
    :alt: GitHub Repo stars for neurosift
    :target: https://github.com/flatironinstitute/neurosift

.. short_description_end

With Neurosift, you have the ability to construct a multitude of synchronized visuals such as spike raster plots, audio spectrograms, videos, video annotations, position decode fields, timeseries graphs, and more.

Neurosift is also integrated with DANDI Archive for visualizing NWB files directly in your browser. You can browse the contents of a dandiset directly in your browser, and visualize the items using Neurosift views. Here is an example:

.. code-block::

    https://flatironinstitute.github.io/neurosift/#/nwb?url=https://dandiarchive.s3.amazonaws.com/blobs/c86/cdf/c86cdfba-e1af-45a7-8dfd-d243adc20ced

Replace the url query parameter with the appropriate URL for your NWB file on DANDI or anywhere else on the web.