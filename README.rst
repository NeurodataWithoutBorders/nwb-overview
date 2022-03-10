To build locally, run

```bash
sphinx-build -a docs/source build
```

Read the tutorial here:

https://docs.readthedocs.io/en/stable/tutorial/

External links
==============

Adding new external links
-------------------------

For managing links to external resources we use the :ref:`extlinks <https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html>` of sphinx. The mapping of links is defined in the ``/docs/source/conf_extlinks.py`` as part of ``extlinks`` dictionary. To update or add a new link edit the ``extlinks`` dictionary. For example, ``extlinks`` includes the entry

.. code-block:

    extlinks = {
        'incf_collection': ('https://training.incf.org/collection/neurodata-without-borders-neurophysiology-nwbn', ''),
        'pynwb_issue': ('https://github.com/NeurodataWithoutBorders/pynwb/issues/%s', 'pynwb#%s')
    }

The key in the dict defines the alias name as a new role so that we can writhe ``:pynwb_issue:```` to create a link. The value is the dict are a tuple consisting of the ``URL`` and the ``caption``.

* **URL** The ``URL`` may contain ``%s`` once to extend the URL, e.g, in the case of linking to issues we need to add the issue number.
* **Caption**:
   * ``None`` : The the link caption rendered in the docs is the full URL
   * ``''`` : The link caption in the text is the custom text indicated in the role
   * ``text%s`` :  If the ``caption`` is a string, then it must contain ``%s`` exactly once. In this case the link caption is caption with the partial URL substituted for %s. E.g.,  in the above example, the link caption for pynwb issues would be issue pynwb#1.

Creating external links in the docs
-----------------------------------

The ``extlinks`` dict in ``/docs/source/conf_extlinks.py`` defines a set of new roles. This allows us to refer, e.g., to specific usses in PyNWB via ``:pynwb_issue:`1``` which will in turn will be rendered as the text "pynwb#1" in the docs with the appropriate link to the issue. Similarly, if we want to refer to the INCF training we can write ``:incf_collection:`INCF Training``` in the text. Since the caption is an empty string in the ``extlinks`` dict for the ``incf_collection`` key, the link will be rendered using the provided text, i.e., here "INCF Training" with the approbriate link.

Linking to external packages
=============================

Adding links to external packages
---------------------------------

To link to specific entities (e.g., classes) in documentation of external software packages, we use the `intersphinx <https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html>`_ feature. The mapping to external docs is defined in ``/docs/source/conf_extlinks.py`` as part of the ``intersphinx_mapping`` dictionary. To support linking to a new tool, add the tool to the mapping.

Creating external links to external packages in the docs
--------------------------------------------------------

Once the mapping is defined, we can refer to specific types much like we would refer to classes in our own tools. For example, the intersphinx mapping includes mappings for ``PynNWB`` and ``Pandas``:

.. code-block:: python

    intersphinx_mapping = {
        'pynwb': ('https://pynwb.readthedocs.io/en/stable/', None),
        'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    }

With this we can now easly link to elements in those packages. E.g., to links to the docs of ``pandas.DataFrame`` we would write ``:py:class:`~pandas.DataFrame``` in the docs. Similarly, to link to ``NWBFile`` in ``PyNWB`` we would write ``:py:class:`~pynwb.file.NWBFile``` in the docs. When including the ``~`` we tell Sphinx to ignore the package when rendering in the text, i.e., ``:py:class:`~pynwb.file.NWBFile``` (with ``~``) will render as ``NWBFile`` in the docs, whereas ``:py:class:`pynwb.file.NWBFile``` (without ``~``) will render as the full name ``pynwb.file.NWBFile``.
