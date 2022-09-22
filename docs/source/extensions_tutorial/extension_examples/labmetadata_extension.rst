.. _extension-example-labmetadata:

Extensions for lab-specific metadata using ``LabMetaData``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use Case
""""""""

.. short_description_start

Here we address the use case of adding lab-specific metadata to a file, e.g.,
lab-specific information about experimental protocols, lab-specific identifiers and so on.
This approach is intended for usually small metadata. This approach is **not** appropriate
for integrating new data modalities, acquired data, and processing results with NWB.

.. short_description_end

Approach
""""""""

To include lab-specific metadata, NWB provides :py:class:`pynwb.file.LabMetaData` as a
a convenient base type, which makes it easy to add your data to an :py:class:`pynwb.file.NWBFile`
without having to modify the :py:class:`pynwb.file.NWBFile` type itself
(since adding of :py:class:`pynwb.file.LabMetaData` is already implemented).

Creating the extension
""""""""""""""""""""""

**1.** Create a new repository for the extension using the :nwb_extension_git:`ndx-template`:

.. code-block:: bash

   cookiecutter gh:nwb-extensions/ndx-template

**2.** Answer a few simple question of the cookiecutter template. Many questions we can here simply confirm
with ``Enter`` to accept the default response (e.g., to start with ``version=0.1.0``):

.. code-block::

    namespace [ndx-my-namespace]: ndx-my-brainlab
    description [My NWB extension]: Extension describing lab-specific metadata for MyBrainLab
    author [My Name]: Peter Brain
    email [my_email@example.com]: peterbrain@brainlab.org
    github_username [myname]: peterbrain
    copyright [2021, Peter Brain]:
    version [0.1.0]:
    release [alpha]:
    Select license:
    1 - BSD-3
    2 - MIT
    3 - Apache Software License 2.0
    4 - Other
    Choose from 1, 2, 3, 4 [1]: 1
    py_pkg_name [ndx_my_brainlab]:

**3.** Edit ``ndx-my-brainlabsrc/spec/create_extension_spec.py`` that was generated for you to define the
schema of your extension.

* Add ``LabMetaData`` as an include type:

.. code-block:: python

    ns_builder.include_type('LabMetaData', namespace='core')

* Define your new ``LabMetaData`` type for your lab

.. code-block:: python

     labmetadata_ext = NWBGroupSpec(
        name='MyBrainLabMetaData',
        doc='type for storing lab metadata for MyBrainLab',
        neurodata_type_def='MyBrainLabMetaData',
        neurodata_type_inc='LabMetaData',
    )

* Add the ``Groups``, ``Datasets``, and ``Attributes`` with the metadata specific to our lab to
  our ``LabMetaData`` schema

.. code-block:: python

    labmetadata_ext.add_dataset(
        name="tissue_preparation",
        doc="Lab-specific description of the preparation of the tissue",
        dtype='text',
        quantity='?'
    )

* Add our new type definitions to the extension

.. code-block:: python

    new_data_types = [labmetadata_ext]

**4.** Generate the schema for the extension by running the ``create_extension_spec.py`` script

.. code-block:: bash

   cd ndx-my-brainlab
   python src/spec/create_extension_spec.py

**5.** Install your extension (Python only)(Optional)

.. code-block:: bash

   pip install .

Now our extension is ready to use!

Creating a Python API for the extension
"""""""""""""""""""""""""""""""""""""""

...

Writing data using the extension
""""""""""""""""""""""""""""""""

...

Reading an NWB file that uses the extension
"""""""""""""""""""""""""""""""""""""""""""

...


.. note::

     NWB uses dynamically extensible table structures based on :py:class:`~hdmf.common.table.DynamicTable`
     to describe metadata and derived results, e.g., :py:class:`~pynwb.epochs.TimeIntervals` for epochs or trials
     or :py:class:`~pynwb.file.ElectrodeTable` to describe extracellular electrodes. For additional information
     related to such existing table structures we can often avoid the need for custom extensions by including
     the data as additional, custom columns in these existing tables.

