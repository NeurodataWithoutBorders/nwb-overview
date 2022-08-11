.. _core-tools-home:

**************************
Glossary of Core NWB Tools
**************************

The glossary shown here provides a quick overview of the key software packages of the core NWB software stack. For a more general discussion of the overall organization of the core NWB software stack see the :nwb-main:`NWB Software Ecosystem <nwb-software>` page on the main NWB website.


:octicon:`tools;1.5em` Read/Write NWB File APIs
-----------------------------------------------

The NWB reference APIs provide full support for reading and writing all components of the NWB standard, including support for extensions. The APIs are interoperable, i.e., files created with PyNWB can be read in MatNWB and vice versa. Both PyNWB and MatNWB support advanced read/write for efficient interaction with very large data files (i.e., data too large for main memory), via lazy data loading, iterative data write, and data compression among others.

.. image:: https://raw.githubusercontent.com/NeurodataWithoutBorders/pynwb/dev/docs/source/figures/logo_pynwb.png
    :class: align-left
    :width: 100

:pynwb-docs:`PyNWB <>` is the Python reference API for NWB. :bdg-link-primary:`Docs <https://pynwb.readthedocs.io/en/stable/>` :bdg-link-primary:`Tutorials <https://pynwb.readthedocs.io/en/stable/tutorials/index.html>` :bdg-link-primary:`Source <https://github.com/NeurodataWithoutBorders/pynwb/>`


.. raw:: html

    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>

.. image:: https://raw.githubusercontent.com/NeurodataWithoutBorders/matnwb/master/logo/logo_matnwb_small.png
    :class: align-left
    :width: 100

:matnwb-docs:`MatNWB <>` is a MATLAB library for reading and writing NWB files. :bdg-link-primary:`Docs <https://neurodatawithoutborders.github.io/matnwb/>` :bdg-link-primary:`Tutorials <https://neurodatawithoutborders.github.io/matnwb/#tutorials>`  :bdg-link-primary:`Source <https://github.com/NeurodataWithoutBorders/matnwb/>`

.. raw:: html

    <br/>
    <br/>


---------------------

.. raw:: html

    <br/


:octicon:`git-branch;1.5em` Converting Data to NWB
--------------------------------------------------

**NWB Conversion Tools**

 The :nwbconversiontool-docs:`NWB Conversion Tools <>` is a Python library for automatic conversion from proprietary data formats to NWB.  :bdg-link-primary:`Docs <https://nwb-conversion-tools.readthedocs.io/en/main/>` :bdg-link-primary:`Source <https://github.com/catalystneuro/nwb-conversion-tools>`

---------------------

.. raw:: html

    <br/

:octicon:`code-review;1.5em` Validating NWB Files
-------------------------------------------------

NWB provides tools to check that files comply with the :nwb-schema-docs:`NWB standard schema <>` as well as to check whether the data complies with :nwbinspector-docs:`NWB Best Practices <best_practices/best_practices_index.html>`. Validating compliance with the NWB schema ensures that files are structurally correct and can be read by NWB APIs. Validating compliance with best practices helps improve data quality and (re-)usability.

.. image:: https://raw.githubusercontent.com/NeurodataWithoutBorders/nwbinspector/dev/docs/logo/logo.png
    :class: align-left
    :width: 120

:nwbinspector-docs:`NWB Inspector <>` is a python library and command-line tool for inspecting NWB files for adherence to :nwbinspector-docs:`NWB best practices <best_practices/best_practices_index.html>`. By default, the Inspector also runs the PyNWB validator to check for compliance with the NWB schema. The Inspector can also be easily extended to integrate custom data checks and to configure checks. :bdg-link-primary:`Docs <https://nwbinspector.readthedocs.io/en/add_docs/>` :bdg-link-primary:`Source <https://github.com/NeurodataWithoutBorders/nwbinspector>`


.. image:: https://raw.githubusercontent.com/NeurodataWithoutBorders/pynwb/dev/docs/source/figures/logo_pynwb.png
    :class: align-left
    :width: 120


The :pynwb-docs:`PyNWB <>` reference Python API includes classes and command line tools for validating compliance of files with the core NWB schema and the schema of NWB Neurodata Extensions (NDX). :bdg-link-primary:`Validation Docs <https://pynwb.readthedocs.io/en/stable/validation.html>`


.. hint::

    In practice, most user should use the :nwbinspector-docs:`NWB Inspector <>` to validate NWB files, as it helps to check for compliance with both the schema and best practices and provides greater flexibility. Direct use of :pynwb-docs:`PyNWB's validator <validation.html>` is primarily useful for use case where schema compliance and performance are of primary concern, for example, during development of extensions or as part of automated test environments.


---------------------

.. raw:: html

    <br/

:octicon:`diff-added;1.5em` Extending NWB
-----------------------------------------

Neurodata Extensions (NDX) are used to extend the NWB data standard, e.g., to integrate new data types with NWB or define standard for lab- or project-specific metadata. The collection of tools listed here are used to create, document, publish extensions. To learn more about how create extensions see the :ref:`extending-nwb` section.

.. image:: https://nwb-extensions.github.io/images/ndx-logo-text.png
    :class: align-left
    :width: 120

The :ndx-catalog:`Neurodata Extensions Catalog (NDX Catalog) <>` is a community-led catalog of Neurodata Extensions (NDX) to the NWB data standard. The :ndx-catalog:`NDX Catalog <>` provides a central portal to search, publish, and review of NDX. :bdg-link-primary:`Catalog <https://nwb-extensions.github.io/>` :bdg-link-primary:`Source <https://github.com/nwb-extensions/>`

**NDX Template**

 The :ndx-template-docs:`NDX Template <>`  provides a template for creating Neurodata Extensions (NDX) for the NWB data standard. :bdg-link-primary:`Source <https://github.com/nwb-extensions/ndx-template>`

 When creating a new extension, the NDX-template will create a detailed NEXTSTEPS.md file describing how to create an extension and how to submit it to the NDX catalog.

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

.. image:: https://raw.githubusercontent.com/hdmf-dev/hdmf/dev/docs/source/hdmf_logo.png
    :class: align-left
    :width: 120

The :hdmf-docs:`Hierarchical Data Modeling Framework (HDMF) <>` is a python package for working with hierarchical data. It provides APIs for specifying data models, reading and writing data to different storage backends, and representing data with Python object. HDMF builds the foundation for the :pynwb-docs:`PyNWB <>` Python API for NWB. :bdg-link-primary:`Docs <https://hdmf.readthedocs.io/en/stable/>` :bdg-link-primary:`Source <https://github.com/hdmf-dev/hdmf>`
