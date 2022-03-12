.. _core-tools-home:

**************************
Glossary of Core NWB Tools
**************************

The glossary shown here provides a quick overview of the key software packages of the core NWB software stack. For a more general discussion of the overall organization of the core NWB software stack see the :nwb-main:`NWB Software Ecosystem <nwb-software>` page on the main NWB website.


:octicon:`tools;1.5em` Read/Write NWB File APIs
-----------------------------------------------

The NWB reference APIs provide full support for reading and writing all components of the NWB standard, including support for extensions. The APIs are interoperable, i.e., files created with PyNWB can be read in MatNWB and vice versa. Both PyNWB and MatNWB support advanced read/write for efficient interaction with very large data files (i.e., data too large for main memory), via lazy data loading, iterative data write, and data compression among others.

**PyNWB**:

 :pynwb-docs:`PyNWB <>` is the Python reference API for NWB. :bdg-link-primary:`Docs <https://pynwb.readthedocs.io/en/stable/>` :bdg-link-primary:`Source <https://github.com/NeurodataWithoutBorders/pynwb/>`

**MatNWB**

 :matnwb-docs:`MatNWB <>` is a MATLAB library for reading and writing NWB files. :bdg-link-primary:`Docs <https://neurodatawithoutborders.github.io/matnwb/>` :bdg-link-primary:`Source <https://github.com/NeurodataWithoutBorders/matnwb/>`

---------------------

.. raw:: html

    <br/


:octicon:`git-branch;1.5em` Converting Data to NWB
--------------------------------------------------

**NWB Conversion Tools**

 The :nwbconversiontool-docs:`NWB Conversion Tools <>` is a Python library for automatic conversion from proprietary data formats to NWB.  :bdg-link-primary:`Docs <'https://nwb-conversion-tools.readthedocs.io/en/main/>` :bdg-link-primary:`Source <https://github.com/catalystneuro/nwb-conversion-tools>`

---------------------

.. raw:: html

    <br/

:octicon:`code-review;1.5em` Validating NWB Files
-------------------------------------------------

NWB provides tools both to check that files comply with the NWB standard as well as to check whether the data complies with best NWB practices. Validating compliance with NWB schema ensures that files are structurally correct and can be read by NWB APIs. Validating compliance with best practices helps improve data quality and (re-)usability.

**PyNWB: Validate schema compliance**

 The :pynwb-docs:`PyNWB <>` reference Python API includes classes and command line tools for validating compliance of files with the core NWB schema and the schema of NWB Neurodata Extensions (NDX). :bdg-link-primary:`Validation Docs <https://pynwb.readthedocs.io/en/stable/validation.html>`


**NWB Inspector: Validate best practice**

 The :nwbinspector-docs:`NWB Inspector <>` is a python library and command-line tool for inspecting NWB files for adherence to :nwbinspector-docs:`NWB best practices <best_practices.html>` :bdg-link-primary:`Docs <https://nwbinspector.readthedocs.io/en/add_docs/>` :bdg-link-primary:`Source <https://github.com/NeurodataWithoutBorders/nwbinspector>`

---------------------

.. raw:: html

    <br/

:octicon:`diff-added;1.5em` Extending NWB
-----------------------------------------

Neurodata Extensions (NDX) are used to extend the NWB data standard, e.g., to integrate new data types with NWB or define standard for lab- or project-specific metadata. The collection of tools listed here are used to create, document, publish extensions. To learn more about how create extensions see the :ref:`extending-nwb` section.

**NDX Template**

 The :ndx-template-docs:`NDX Template <>`  provides a template for creating Neurodata Extensions (NDX) for the NWB data standard. :bdg-link-primary:`Source <https://github.com/nwb-extensions/ndx-template>`

 When creating a new extension, the NDX-template will create a detailed NEXTSTEPS.md file describing how to create an extension and how to submit it to the NDX catalog.

**NDX Catalog**

 The :ndx-catalog:`Neurodata Extensions Catalog (NDX Catalog) <>` is a community-led catalog of Neurodata Extensions (NDX) to the NWB data standard. The :ndx-catalog:`NDX Catalog <>` provides a central portal to search, publish, and review of NDX. :bdg-link-primary:`Catalog <https://nwb-extensions.github.io/>` :bdg-link-primary:`Source <https://github.com/nwb-extensions/>`

**Publishing NDX**

 The :nwb_extension_git:`staged-extensions` GitHub repository is used to register new extensions for publication in the :ndx-catalog:`Neurodata Extensions Catalog (NDX Catalog) <>`. :bdg-link-primary:`Source <https://github.com/nwb-extensions/staged-extensions>`

**Documentation Utilities**

 The :hdmf-docutils-docs:`HDMF Documentation Utilities (hdmf-docuils) <>` provides utility tools for creating documentation for extension schema defined using the :nwb-schema-language-docs:`NWB Schema Language <>`. :bdg-link-primary:`Source <https://github.com/hdmf-dev/hdmf-docutils>`

 The :ndx-template-docs:`NDX Template <>` automatically sets up the documentation. As such, developers of extensions will commonly :hdmf-docutils-docs:`hdmf-docuils <>` as part of the standard setup of NDX code repositories without having to interact with the tool directly.

**NWB Format Specification**

 The NWB data standard is governed by the :nwb-schema-docs:`NWB Format Specification <>`.  When creating new extensions we typically build on and reuse existing ``neurodata_types`` already available in NWB. The :nwb-schema-docs:`NWB Format Specification <>` provides a reference definition for all types available in NWB. The NWB schema itself includes/builds on the :hdmf-common-schema-docs:`HDMF Common Schema <>`. :bdg-link-primary:`Docs <https://nwb-schema.readthedocs.io/en/latest/>` :bdg-link-primary:`Source <https://github.com/NeurodataWithoutBorders/nwb-schema>`

**HDMF Common Schema**

 The :hdmf-common-schema-docs:`HDMF Common Schema <>` defines the schema of common, general data structures, which are used throughout the :nwb-schema-docs:`NWB Standard Schema <>` but which are not specific to neurophysiology. Example types defined in the HDMF common schema incude, e.g., all types related to :py:class:`~hdmf.common.table.DynamicTable` for defining data tables. :bdg-link-primary:`Docs <https://hdmf-common-schema.readthedocs.io/en/stable/>` :bdg-link-primary:`Source <https://github.com/hdmf-dev/hdmf-common-schema>`

---------------------

.. raw:: html

    <br/

:octicon:`package-dependencies;1.5em` Core Development
------------------------------------------------------

Understanding core development tools (e.g., HDMF) is useful for developers in particular when we need to dive deeper into the core data infrastructure for NWB, e.g., when changing or creating new storage methods or when developing features for common data types (e.g., :py:class:`~hdmf.common.DynamicTable`) that are defined in HDMF and used in NWB.

**HDMF**

 The :hdmf-docs:`Hierarchical Data Modeling Framework (HDMF) <>` is a python package for working with hierarchical data. It provides APIs for specifying data models, reading and writing data to different storage backends, and representing data with Python object. HDMF builds the foundation for the :pynwb-docs:`PyNWB <>` Python API for NWB. :bdg-link-primary:`Docs <https://hdmf.readthedocs.io/en/stable/>` :bdg-link-primary:`Source <https://github.com/hdmf-dev/hdmf>`




