.. _untyped_types:

Utility Types in MatNWB
=======================

"Untyped" Utility types are tools which allow for both flexibility as well as limiting certain constraints that are imposed by the NWB schema. These types are commonly stored in the ``+types/+untyped/`` package directories in your MatNWB installation.

Sets and Anons
~~~~~~~~~~~~~~

The **Set** (``types.untyped.Set`` or Constrained Sets) is used to capture a dynamic number of particular NWB-typed objects. They may contain certain type constraints on what types are allowable to be set. Set keys and values can be set and retrieved using their ``set`` and ``get`` methods:

.. code-block:: MATLAB

    value = someSet.get('key name');

.. code-block:: MATLAB
    
    someSet.set('key name', value);

.. note::
    
    Sets also borrow ``containers.Map``'s ``keys`` and ``values`` methods to retrieve cell arrays of either.

The **Anon** type (``types.untyped.Anon``) can be understood as a Set type with only a single key-value entry. This rarer type is only used for cases where the name of the type can be set by the user. Anon types may also hold NWB type constraints like Set.


DataStubs and DataPipes
~~~~~~~~~~~~~~~~~~~~~~~

**DataStubs** serves as a read-only link to your data. It allows for MATLAB-style indexing to retrieve the data stored on disk.

.. image:: /img/datastub.png

**DataPipes** are similar to DataStubs but also allow you to write your data to disk. The DataPipe is an advanced type and users looking to leverage DataPipe's capabilities to stream/iteratively write or compress data should read the `Advanced Data Write Tutorial <https://neurodatawithoutborders.github.io/matnwb/tutorials/html/dataPipe.html>`_.


Links and Views
~~~~~~~~~~~~~~~

**Links** (either ``types.untyped.SoftLink`` or ``types.untyped.ExternalLink``) are views either back into the read NWB file or some other NWB file outside of the currently read one. *SoftLinks* contain a path into the same NWB file while *ExternalLinks* additionally hold a ``filename`` field to point to an external NWB file. Both types use their ``deref`` methods to retrieve the NWB object that they point to though *SoftLinks* require the NwbFile object that was read in.

.. code-block:: MATLAB

    referencedObject = softLink.deref(rootNwbFile);

.. code-block:: MATLAB

    referencedObject = externalLink.deref();

.. note::

    Links are not resolved on write, so it is possible that dereferencing links may fail.

**Views** (either ``types.untyped.ObjectView`` or ``types.untyped.RegionView``) are more advanced references strictly pointing to NWB types or segments of data in some NWB type within the same NWB file. *ObjectViews* will point to NWB types while *RegionViews* will point to some subset of data stored in the ``data`` field of NWB types. Both types use ``refresh`` to retrieve their referenced data.

.. code-block:: MATLAB

    referencedObject = objectView.refresh(rootNwbFile);

.. code-block:: MATLAB

    dataSubset = regionView.refresh(rootNwbFile);
