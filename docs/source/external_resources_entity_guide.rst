.. _external_resources_entity_guide:

Using Ontologies and Identifiers with NWB
=========================================

Neurophysiology data is full of terms that mean something specific outside of your file: the
species of a subject, the institution that collected the data, the researchers who ran the
experiment, or the brain region a probe was implanted in. Writing these as free text (``"mouse"``,
``"the Allen Institute"``, ``"V1"``) is easy to do but hard to compute on — different files spell
the same thing different ways, and a reader has no authoritative reference for what exactly was
meant.

**External resources** solve this by linking a term in your file to a standardized entry in an
external **ontology**, **registry**, or **atlas**; for example linking the species
``"Mus musculus"`` to its entry in the NCBI Taxonomy. This makes your annotations unambiguous,
machine-readable, and interoperable, enabling tools to group, search, and compare data across 
files and labs because everyone points at the same canonical identifier.

In NWB, these links are stored using **HERD** (HDMF External Resources Data Structure). HERD is a
dedicated data structure for attaching external references to existing values in a file.
HERD stores, for each annotation, the term as it appears in your file and the location where it is used,
along with a compact identifier (``entity_id``) and a resolvable URL (``entity_uri``) for the
external entry.

To simplify the use of external resources, **TermSets** defined via LinkML can be used to 
define a set of valid terms and their corresponding external references. Using TermSets, you
can then constrain a field to only accept terms from that set, validate values as they are written,
and automatically populate HERD with the corresponding references.


How to add external resources to an NWB file
--------------------------------------------

**PyNWB tutorials**: The following tutorials provide a practical guide to using HERD and TermSets in PyNWB:

* :pynwb-docs:`Linking to External Resources <tutorials/general/plot_external_resources.html>`: 
  Learn how to use HERD to annotate a single NWB file with external resources in PyNWB. 
* :pynwb-docs:`Annotating Multiple Files <tutorials/general/resources_streaming.html>`:
  Learn how to use HERD to annotate multiple remote NWB files using streaming to avoid downloading them all.
* :pynwb-docs:`TermSet for Validation <tutorials/general/plot_configurator.html>`: Learn how to configure PyNWB
  to automatically use pre-configured TermSets to validate terms and automatically populate HERD.

**HDMF tutorials**: The following tutorials provide a deeper dive into the underlying HDMF structures and how to use them:

* :hdmf-docs:`HERD tutorial <tutorials/plot_external_resources.html>`: Learn more about the 
  underlying HDMF HERD data structure and how to use it.
* :hdmf-docs:`TermSet tutorial <tutorials/plot_term_set.html>`: Learn more about how to create 
  new term sets and how to use TermSets to validate values against an ontology and automatically
  populate HERD.

The rest of this page covers a question that comes up with both approaches: once you have picked
an external term, what exactly should go in the ``entity_id`` and ``entity_uri`` fields?

Choosing ``entity_id`` and ``entity_uri``
-----------------------------------------

When you annotate data with an external resource using
:py:meth:`HERD.add_ref <hdmf.common.resources.HERD.add_ref>`, each reference records two
fields that identify the external term:

``entity_id``
    A compact identifier (a `CURIE <https://www.w3.org/TR/curie/>`_) of the form
    ``prefix:identifier`` (e.g. ``NCBITaxon:10090``). The ``prefix`` names the registry or
    ontology and the ``identifier`` is the term's accession within it.

``entity_uri``
    The full URL that the ``entity_id`` resolves to — a persistent, dereferenceable web
    address for that exact term.

Recommended practice
^^^^^^^^^^^^^^^^^^^^^

#. **Use a CURIE for** ``entity_id``. Prefer an identifier whose ``prefix`` is registered with
   `bioregistry.io <https://bioregistry.io>`_. The Bioregistry is a comprehensive registry of
   prefixes that maps each CURIE to a canonical, resolvable URL, which avoids the ambiguity of
   the many overlapping identifier schemes (e.g. ``NCBITaxon`` vs. ``taxonomy`` vs.
   ``NCBI_TAXON``).

#. **Use the resolved URL for** ``entity_uri``. The ``entity_uri`` should be the URL that the
   CURIE resolves to. You can look this up by resolving the CURIE through the Bioregistry:
   visiting ``https://bioregistry.io/<entity_id>`` (for example
   ``https://bioregistry.io/NCBITaxon:10090``) redirects to the canonical provider URL, which is
   the value to store in ``entity_uri``.

Keeping ``entity_id`` and ``entity_uri`` consistent in this way means a reader can both
recognize the registry from the compact ``entity_id`` and dereference the ``entity_uri`` to land
on an authoritative description of the term.

Commonly used registries
^^^^^^^^^^^^^^^^^^^^^^^^^

All of the registries below are registered with the Bioregistry. The ``entity_uri`` column shows
the canonical URL the example ``entity_id`` resolves to.

.. list-table::
   :header-rows: 1
   :widths: 10 16 22 20 32

   * - Prefix
     - Use for
     - Common NWB field(s)
     - Example ``entity_id``
     - Example ``entity_uri``
   * - ``NCBITaxon``
     - Species
     - ``Subject.species``
     - ``NCBITaxon:10090``
     - ``http://purl.obolibrary.org/obo/NCBITaxon_10090``
   * - ``ROR``
     - Organizations / institutions
     - ``NWBFile.institution``
     - ``ROR:013meh722``
     - ``https://ror.org/013meh722``
   * - ``ORCID``
     - People (researchers)
     - ``NWBFile.experimenter``
     - ``ORCID:0000-0002-1825-0097``
     - ``https://orcid.org/0000-0002-1825-0097``
   * - ``UBERON``
     - Brain regions (cross-species)
     - Brain-region location fields [#loc]_
     - ``UBERON:0001950``
     - ``http://purl.obolibrary.org/obo/UBERON_0001950``
   * - ``MBA``
     - Brain regions (Allen Mouse Brain Atlas)
     - Brain-region location fields [#loc]_
     - ``MBA:385``
     - ``https://purl.brain-bican.org/ontology/mbao/MBA_385``
   * - ``HBA``
     - Brain regions (Allen Human Brain Atlas)
     - Brain-region location fields [#loc]_
     - ``HBA:4005``
     - ``https://purl.brain-bican.org/ontology/hbao/HBA_4005``
   * - ``DANDI``
     - Dandisets
     - (identifies the dataset as a whole)
     - ``DANDI:000015``
     - ``https://dandiarchive.org/dandiset/000015``

.. [#loc] Brain-region annotations commonly apply to ``ElectrodeGroup.location``,
   ``ImagingPlane.location``, and the ``location`` column of the ``electrodes`` table.

Example
^^^^^^^

.. code-block:: python

    # the species of the subject, mapped to NCBI Taxonomy
    herd.add_ref(
        container=nwbfile.subject,
        attribute="species",
        key="Mus musculus",
        entity_id="NCBITaxon:10090",
        entity_uri="http://purl.obolibrary.org/obo/NCBITaxon_10090",
    )

Resources without individually resolvable URLs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some resources do not provide a dereferenceable URL for each individual term. For example, many
brain atlases (such as the macaque **D99** atlas) publish a single document or download for the
whole atlas rather than one persistent URL per region.

In that case:

* Put the **URL of the resource as a whole** in ``entity_uri`` (e.g. the atlas's landing or
  download page).
* Put the resource's **identifier for the specific term** — for example, the brain area ID used
  by the atlas — in ``entity_id``.

This keeps every reference dereferenceable to *something* authoritative (the resource) while
still recording the precise term identifier, even when a per-term URL does not exist.

.. code-block:: python

    # a region from an atlas that has no per-region URL: identify the region by its
    # atlas-specific ID and point entity_uri at the atlas itself
    herd.add_ref(
        container=electrodes_table,
        attribute="location",
        key="area_42",
        entity_id="42",
        entity_uri="https://afni.nimh.nih.gov/pub/dist/doc/htmldoc/nonhuman/macaque_tempatl/atlas_d99v2.html",
    )

.. seealso::

   :py:class:`HERD <hdmf.common.resources.HERD>` for the full API, and
   :py:meth:`HERD.add_ref <hdmf.common.resources.HERD.add_ref>` for adding references.
