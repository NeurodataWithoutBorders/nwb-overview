Building the docs locally
==========================

.. code-block:: bash

    sphinx-build -a docs/source build


or

.. code-block:: bash

    cd docs
    make html

And to view the docs open ``build/html/index.html``.


Adding a Community Tool
=======================

To contribute a new tool to the list of analysis, visualization and data management tools, please create a pull request to this repo. Adding a tool requires the following steps.

**Step 1:** Create a new folder for your tool in ``docs/source/tools/<mytool>`` with the name of your tool

**Step 2:** Create a new file ``docs/source/tools/<mytool>/<mytool>.rst`` for your tool and copy the following template to that file

.. code-block::

    .. _analysistools-<mytool>:

    <mytoolname>
    ------------

    .. short_description_start

    :ref:`analysistools-<mytool>` <briefly describe your tool> :bdg-link-primary:`Docs <mydocs>` :bdg-link-primary:`Source <mysoure>`.

    .. short_description_end

    .. image:: <myimgage>
        :class: align-left
        :width: 400

**Step 3:** Update the ``<my*>`` parts and add a brief description of your tool as well as an image for your tool.

**Step 4:** You may add additional sections as approbriate to the page, e.g., to describe tool features, usage, or installation. In particular, also consider adding a section on ``Compatability with NWB`` to describe how your tools integrate with NWB (e.g., does your tool support read/write/update of specific neurodata_types in NWB and does your tool require any extensions).

**Step 5:** In ``docs/source/tools/tools_home.rst`` Add your tool to the toctree at the top of the page to ensure the tool gets listed in the main menu

**Step 6:** In the section that best fits your tool on ``docs/source/tools/tools_home.rst`` add the following and again update the ``<my*>`` marked parts.

.. code-block::

    .. image:: <mytool>/<myimage>
        :class: align-left
        :width: 180

    .. include::  <mytool>/<mytool.rst>
            :start-after: .. short_description_start
            :end-before: .. short_description_end

With ``.. include`` directive with the ``start-after`` and ``end-before`` parameters, Sphinx will automatically include the short description from your doc so the glossary will automatically be updated as you make changes in the main document of your your tool.

.. note::

    Depending on how long your and the previous tool description are, you may need to add some empty lines in HTML before/after your entry to ensure the overview displays correctly. You can add lines in HTML by adding the following in the file

.. code-block::

    .. raw:: html

        <br />
        <br />

.. note::

    Latex does not support ``gif`` images. If you need to use ``gif`` images then you should place them in a ``.. only:: html`` directive and provide a corresponding ``.. only:: latex`` directive with the appropriate content for Latex PDF builds.



**Step 7:** Build the docs and and review your changes via

.. code-block::

    cd docs
    make html
    open build/html/index.html

**Step 7** Create a pull request to this repo with your changes


Adding a Community Project
==========================

To contribute a new project to the community gallery, please create a pull request to this repo. Adding a tool requires the following steps.

**Step 1:** Create a new entry on the  ``docs/source/community_gallery/community_gallery.rst page. An entry should consist of a small figure or icon and brief description, following the style of the existing entries.

    * Figure should be added to the folder ``docs/source/community_gallery/figures``
    * If you design the figure in PowerPoint then please add the source slide to the ``docs/source/community_gallery/figures/figure_icons_source.pptx`` file

**Step 2:** Build the docs and and review your changes via

.. code-block::

    cd docs
    make html
    open build/html/index.html

**Step 3** Create a pull request to this repo with your changes


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

Normally the ``extlinks`` extension will add the part we link to the URL. To use the exact URL as defined in ``extlinks`` dict use the following syntax ``:pynwb-docs:`PyNWB <>```, which will render the text (here PyNWB) with a hyperlink to the exact, unmodified URL.

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
