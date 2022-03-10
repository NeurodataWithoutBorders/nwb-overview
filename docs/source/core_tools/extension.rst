.. _core-extension:

Extending NWB
=============

Neurodata Extensions (NDX) are used to extend the NWB data standard, e.g., to integrate new data types with NWB or define standard for lab- or project-specific metadata. The collection of tools are used to create, document, publish extensions.

NDX Template
------------

.. ndxtemplate_short_description_start

The :ndx-template-docs:`NDX Template <>`  provides a template for creating Neurodata Extensions (NDX) for the NWB data standard. :bdg-link-primary:`Source <https://github.com/nwb-extensions/ndx-template>`

.. ndxtemplate_short_description_end

 When creating a new extension, the NDX-template will create a detailed NEXTSTEPS.md file describing how to create an extension and how to submit it to the NDX catalog.

NDX Catalog
-----------

.. ndxcatalog_short_description_start

The :ndx-catalog:`Neurodata Extensions Catalog (NDX Catalog) <>` is a community-led catalog of Neurodata Extensions (NDX) to the NWB data standard. The :ndx-catalog:`NDX Catalog <>` provides a central portal to search, publish, and review of NDX. :bdg-link-primary:`Catalog <https://nwb-extensions.github.io/>` :bdg-link-primary:`Source <https://github.com/nwb-extensions/>`



.. ndxcatalog_short_description_end

Publishing NDX
--------------

.. pubndx_short_description_start

The :nwb_extension_git:`staged-extensions` GitHub repository is used to register new extensions for publication in the :ndx-catalog:`Neurodata Extensions Catalog (NDX Catalog) <>`. :bdg-link-primary:`Source <https://github.com/nwb-extensions/staged-extensions>`

.. pubndx_short_description_end

:nwb_extension_git:`staged-extensions` is a special GitHub repository as part of the :ndx-catalog-github-org:`NDX Catalog Github Organization <>` where users can create pull requests to request the addition of an extension to the catalog.


Documentation Utilities
-----------------------

.. docutils_short_description_start

The :hdmf-docutils-docs:`HDMF Documentation Utilities (hdmf-docuils) <>` provides utility tools for creating documentation for extension schema defined using the :nwb-schema-language-docs:`NWB Schema Language <>`. :bdg-link-primary:`Source <https://github.com/hdmf-dev/hdmf-docutils>`


.. docutils_short_description_end

The :ndx-template-docs:`NDX Template <>` automatically sets up the documentation. As such, developers of extensions will commonly :hdmf-docutils-docs:`hdmf-docuils <>` as part of the standard setup of NDX code repositories without having to interact with the tool directly.

NWB Standard Schema
-------------------

.. nwbspec_short_description_start

The NWB data standard is governed by the :nwb-schema-docs:`NWB Format Specification <>`. :bdg-link-primary:`Docs <https://nwb-schema.readthedocs.io/en/latest/>` :bdg-link-primary:`Source <https://github.com/NeurodataWithoutBorders/nwb-schema>`

.. nwbspec_short_description_end

 When creating new extensions we typically build on and reuse existing ``neurodata_types`` already available in NWB. The :nwb-schema-docs:`NWB Format Specification <>` provides a reference definition for all types available in NWB. The NWB schema itself includes/builds on the :hdmf-common-schema-docs:`HDMF Common Schema <>`.

HDMF Common Schema
------------------

.. hdmfcommon_short_description_start

The :hdmf-common-schema-docs:`HDMF Common Schema <>` defines the schema of common, general data structures, which are used throughout the :nwb-schema-docs:`NWB Standard Schema <>` but which are not specific to neurophysiology. :bdg-link-primary:`Docs <https://hdmf-common-schema.readthedocs.io/en/stable/>` :bdg-link-primary:`Source <https://github.com/hdmf-dev/hdmf-common-schema>`

.. hdmfcommon_short_description_end

Example types defined in the HDMF common schema incude, e.g., all types related to :py:class:`~hdmf.common.table.DynamicTable` for defining data tables.




