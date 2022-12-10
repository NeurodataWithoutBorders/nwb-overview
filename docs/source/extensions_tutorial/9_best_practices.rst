.. _extension-nwb-best-practices:

NWB Extension Best Practices
----------------------------


Define new ``neurodata_types`` at the top-level (a.k.a., do not nest type definitions)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Rather than nesting definitions of ``neurodata_types``, all new types should be defined
at the top-level of the schema. To include a specific ``neurodata_type`` in another type
use the ``neurodata_type_inc`` key instead. For example:

.. tabs::

    .. tab:: Do This

       .. tabs::

            .. code-tab:: py Python

                from pynwb.spec import NWBGroupSpec

                # Define the first type
                type1_ext = NWBGroupSpec(
                    name='custom_type1',
                    doc='Example extension type 1',
                    neurodata_type_def='MyNewType1',
                    neurodata_type_inc='LabMetaData',
                )

                # Then define the second type and include the first type
                type2_ext = NWBGroupSpec(
                    name='custom_type2',
                    doc='Example extension type 2',
                    neurodata_type_def='MyNewType2',
                    groups=[NWBGroupSpec(neurodata_type_inc='MyNewType1',
                                         doc='Included group of ype MyNewType1')]
                )

            .. code-tab:: yaml YAML

                groups:
                - neurodata_type_def: MyNewType1
                  neurodata_type_inc: LabMetaData
                  name: custom_type1
                  doc: Example extension type 1
                - neurodata_type_def: MyNewType2
                  neurodata_type_inc: NWBContainer
                  name: custom_type2
                  doc: Example extension type 2
                  groups:
                  - neurodata_type_inc: MyNewType1
                    doc: Included group of ype MyNewType1

    .. tab:: DON'T do this

        .. tabs::

            .. code-tab:: py Python

                from pynwb.spec import NWBGroupSpec

                # Do NOT define a new type via ``neurodata_type_def`` within the
                # definition of another type. Always define the types separately
                # and use ``neurodata_type_inc`` to include the type
                type2_ext = NWBGroupSpec(
                    name='custom_type2',
                    doc='Example extension type 2',
                    neurodata_type_def='MyNewType2',
                    groups=[NWBGroupSpec(
                        name='custom_type1',
                        doc='Example extension type 1',
                        neurodata_type_def='MyNewType1',
                        neurodata_type_inc='LabMetaData',
                    )]
                )

            .. code-tab:: yaml YAML

                groups:
                - neurodata_type_def: MyNewType2
                  neurodata_type_inc: NWBContainer
                  name: custom_type2
                  doc: Example extension type 2
                  groups:
                  - neurodata_type_def: MyNewType1
                    neurodata_type_inc: LabMetaData
                    name: custom_type1
                    doc: Example extension type 1


Build on and Reuse Existing ``neurodata_types``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Extend ``TimeSeries`` for storing timeseries data. NWB provides main types of ``TimeSeries``
  and you should identify the most specific type of ``TimeSeries`` relevant for your use case
  (e.g., extend ``ElectricalSeries`` to define a new kind of electrical recording).
* Extend ``DynamicTable`` to store tabular data
* Extend ``TimeIntervals`` to store specific annotations of intervals in time
* ..

Use Attributes for small metadata related to a particular data object (Group or Dataset)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Attributes should be used mainly to store small metadata (usually less than 64 Kbytes) that
is associated with a particular Group or Dataset. Typical uses of attributes are, e.g., to
define the ``unit`` of measurement of a dataset or to store a short ``description`` of
a group or dataset. For larger data, datasets should be used instead.

Link data to relevant metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Often metadata relevant to a particular type of data is stored elsewhere, e.g., information
about the ``Device`` used. To ensure relevant metadata can be uniquely identified, the data
should include links to the relevant metadata. NWB provides a few key mechanisms for linking:

* Use ``links`` (defined via ``NWBLinkSpec``) to link to a particular dataset or group
* Use ``DynamicTableRegion`` to link to a set of rows in a ``DynamicTable``
* Use a ``dataset`` with an object reference data type to store collections of links
  to other objects, e.g., the following dtype to define a dataset of links to ``TimeSeries``

  .. code-block:: yaml

        dtype:
            target_type: TimeSeries
            reftype: object

Best practices for object names
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Names for groups, datasets, attributes, or links should typically:

* **Use lowercase letters only**
* **Use ``_`` instead of `` `` to separate parts in names**. E.g., use the name
  ``starting_time`` instead of ``starting time``
* **Explicit**. E.g., avoid the use of ambiguous abbreviation in names.

Best practices for naming ``neurodata_types``:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For defining new types via ``neurodata_type_def`` use:

* **Use camelcase:**  notation, i.e., names of types should NOT include spaces,
  always start with an uppercase letter, and use a single capitalized letter to
  separate parts of the name. E.g,. ``neurodata_type_def: LaserMeasurement``
* **Use the postfix ``Series`` when extending a ``TimeSeries`` type.** E.g., when
  creating a new ``TimeSeries`` for laser measurements then add ``Series`` to
  the type name, e.g,. ``neurodata_type_def: LaserMeasurementSeries``
* **Use the postfix ``Table`` when extending a ``DynamicTable`` type.** e.g.,
  ``neurodata_type_def: LaserSettingsTable``
* **Explicit**. E.g., avoid the use of ambiguous abbreviation in names.


Always use the ``ndx-template`` to create new extensions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By using the :nwb_extension_git:`ndx-template` to create new extensions helps ensure
that extensions can be easily shared and reused and published via the :ndx-catalog:`NDX Catalog <>`.
