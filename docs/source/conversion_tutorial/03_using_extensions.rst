3. Using Neurodata Extensions
-----------------------------

Neurophysiology is always changing as new technologies are developed. While the core NWB schema supports many of the
most common data types in neurophysiology, we need a way to accommodate new technologies and unique metadata needs.
Neurodata extensions (NDX) allow us to define new data types. These data types can extend core types, contain core
types, or can be entirely new. These extensions are formally defined with a collection of YAML files following
the `NWB Specification Language <https://schema-language.readthedocs.io/en/latest/index.html>`_.

If the core nwb schema does not meet your needs, you will need to use an extension. Your first step should be to search
the :ndx-catalog:`NDX Catalog <>`. Using an existing extension is preferred, because it saves you the work of creating a
new one, and it improves data standardization across the community. If you do not find an extension that meets your
needs, head to the :ref:`extending-nwb` tutorial. When creating a new extension you should also consider 
to let the community know by adding a post on the `NWB Help Desk <https://github.com/NeurodataWithoutBorders/helpdesk/discussions>`_.