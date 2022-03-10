.. _coretools-develop:

NWB Core Development
====================

.. _coretools-hdmf:

HDMF
----

.. hdmf_short_description_start

The :hdmf-docs:`Hierarchical Data Modeling Framework (HDMF) <>` is a python package for working with hierarchical data. It provides APIs for specifying data models, reading and writing data to different storage backends, and representing data with Python object. HDMF builds the foundation for the :pynwb-docs:`PyNWB <>` Python API for NWB. :bdg-link-primary:`Docs <https://hdmf.readthedocs.io/en/stable/>` :bdg-link-primary:`Source <https://github.com/hdmf-dev/hdmf>`


.. hdmf_short_description_end

Understanding HDMF is useful in particular when we need to dive deeper into the core data infrastructure for NWB, e.g., when changing or creating new storage methods or when developing features for common data types (e.g., :py:class:`~hdmf.common.DynamicTable`) that are defined in HDMF and used in NWB.
