.. _community-gallery:

***************************
Community Gallery
***************************

This page is a collection of community conversion and analysis projects cataloged here as a convenient reference for NWB users. This list is not comprehensive and many of the projects and resources are built and supported by other groups, and are in active development. If you would like to contribute a project or resources, please see the instructions :nwb-overview-src:`here <>`.


Data Conversion
---------------

.. image:: figures/neuroconv_gallery.png
    :class: align-left, no-scaled-link
    :width: 100

:neuroconv-docs:`NeuroConv Catalog <catalogue/catalogue.html>` is a collection of real-world examples of labs using :neuroconv-docs:`NeuroConv <>` to convert their data to NWB files. Each project listed contains a description and a link to an open GitHub repository. Many of the projects listed use advanced customization features beyond what is demonstrated in the core :neuroconv-docs:`NeuroConv conversion gallery <conversion_examples_gallery/conversion_example_gallery.html>`. :bdg-link-primary:`NeuroConv Catalog <https://neuroconv.readthedocs.io/en/main/catalogue/catalogue.html>`

.. image:: figures/bristol_neuroscience_data_guide.png
    :class: align-left, no-scaled-link
    :width: 100

The Bristol Neuroscience Data Guide includes tutorials for converting data to NWB for `extracellular electrophysiology data <https://dervinism.github.io/bristol-neuroscience-data-guide/tutorials/Bristol%20GIN%20for%20Silicon%20Probe%20Data.html>`_   and `optical physiology data <https://dervinism.github.io/bristol-neuroscience-data-guide/tutorials/Bristol%20GIN%20for%20Calcium%20Imaging%20Data.html>`_ using both the :pynwb-docs:`PyNWB <>` and :matnwb-docs:`MatNWB <>` APIs for NWB.


.. raw:: html

    <br/>
    <hr>

The DataJoint-NWB Showcase showcases a collection of published datasets with matching DataJoint pipelines and NWB 2.0 export capability. Each showcase comprises the following:

* Basic project summary
* The DataJoint pipeline to ingest the data
* Notebook demonstration of working with the data pipeline to query, extract data and recreate some representative figures
* Scripts to export the data from the DataJoint pipeline into NWB 2.0 files.

:bdg-link-primary:`GitHub <https://github.com/datajoint-company/DataJoint-NWB-showcase>`


.. raw:: html

    <br/>


Data Analysis and Reuse
-----------------------

.. image:: figures/dandi_example_notebooks.png
    :class: align-left, no-scaled-link
    :width: 100


:ref:`analysistools-dandi` (Distributed Archives for Neurophysiology Data Integration) maintains a `collection of example notebooks <https://github.com/dandi/example-notebooks>`_ associated with datasets, conference tools, or more generally notebooks that illustrate the use of data on DANDI. :bdg-link-primary:`Source <https://github.com/dandi/example-notebooks>`

.. raw:: html

    <br/>
    
In addition, the neuroscience community is creating examples demonstrating the reuse of NWB data published on DANDI. For example:

       * The `INCF working group on NWB <https://www.incf.org/sig/incf-working-group-nwb>`_ has created a `library of MATLAB examples <https://github.com/INCF/example-live-scripts>`_ using DANDI datasets authored as MATLAB live scripts. :bdg-link-primary:`Source <https://github.com/INCF/example-live-scripts>`
       * `Neuromatch-AJILE12 <https://github.com/neurovium/Neuromatch-AJILE12>`_ is a package for exploratory analysis of long-term naturalistic human intracranial neural recordings and pose data as part of `Dandiset 000055 <https://dandiarchive.org/dandiset/000055>`_. :bdg-link-primary:`Notebook <https://github.com/neurovium/Neuromatch-AJILE12/blob/master/Notebook/exploreAJILE12.ipynb>` :bdg-link-primary:`Source <https://github.com/neurovium/Neuromatch-AJILE12>` :bdg-link-primary:`Paper <https://www.nature.com/articles/s41597-022-01280-y>`

.. raw:: html

    <br/>

.. image:: figures/openscope_databook.png
    :class: align-left, no-scaled-link
    :width: 100

The :openscope-databook:`OpenScope Databook <>` provides scripts and documentation used for brain data analysis and visualization, primarily working with NWB files and the :ref:`analysistools-dandi` archive. Through :jupyter-book:`Jupyter Book <>`, this code is structured as a series of notebooks intended to explain and educate users on how to work with brain data. This resource is provided by the Allen Institute’s :openscope-project:`OpenScope Project <>`, an endeavor of The Allen Institute :mindscope-program:`Mindscope Program <>`. OpenScope is a platform for high-throughput and reproducible neurophysiology open to external scientists to test theories of brain function.  :bdg-link-primary:`Databook <https://alleninstitute.github.io/openscope_databook/>` :bdg-link-primary:`Source <https://github.com/AllenInstitute/openscope_databook>`




.. raw:: html

    <br/>

.. image:: figures/ibl_brainmap.png
    :class: align-left, no-scaled-link
    :width: 100


The :ibl-website:`International Brain Laboratory (IBL) <>` released a Brainwide Map of neural activity during decision-making, consisting of 547 Neuropixel recordings of 32,784 neurons across 194 regions of the mouse brain. At Cosyne 2023, the IBL team presented an `Introduction to IBL and the Brain-wide map dataset <https://colab.research.google.com/drive/1Ua-NlpYYZCIOF56xbsT9YR71Enkotd-b>`_ and tutorials on `Using IBL data with NWB <https://colab.research.google.com/drive/1zr6lP_zzRgPZuHs3nB5oGnFtPKrduQ3L>`_  and `Using IBL data with ONE <https://colab.research.google.com/drive/1y3sRI1wC7qbWqN6skvulzPOp6xw8tLm7>`_.


.. raw:: html

    <br/>


.. note::

        **Disclaimer:** Reference herein to any specific product, process, or service
        by its trade name, trademark, manufacturer, or otherwise, does not constitute or
        imply its endorsement, recommendation, or favoring by the NWB development team,
        United States Government or any agency thereof, or The Regents of the University
        of California. Use of the NeurodataWithoutBorders name for endorsements is prohibited.

