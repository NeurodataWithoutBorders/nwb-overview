:orphan:

.. _why_hdmf_schema_language:

Why create the HDMF schema language instead of using an existing language?
---------------------------------------------------------------------------

HDMF and NWB define a custom schema language for specifying the allowable shape of HDMF and NWB files. This provides
a formal structure that HDMF and NWB use to create data types and specify the relationships between them. This
specification language handles the primitives of HDF5, i.e. Groups, Datasets, Attributes and Links, each of them with
properties, some common across these types like “name” and some unique to certain primitives like “shape” and “datatype”
of Datasets. The other aspect of the schema language is that it uses object oriented programming (OOP) principles such
as composition and inheritance. It is natural to ask, why did we create this schema language?

Historically, NWB 1 was introduced with a schema, but no formal schema language. The lack of a schema language was
problematic because the rules of the standard were not always clear, and there was no clear way to make changes to the
standard or build NWB extensions. Thus the existence of the schema language and the separation of the schema from the
schema language is an important feature of NWB 2.0 that enables its flexibility. Still, the question remains, why
build a new language instead of using a language that already exists?

In our experience, the pre-existing schema language that comes closest to meeting our needs is json-schema, a
mature and highly effective language for formally defining the structure of JSON documents. Indeed, json-schema
includes the concept of an "object", which is similar to the HDF5 Group in that it specifies containers that can be
nested and can contain attributes. The json-schema "properties" is similar to HDF5 Attributes in that you can specify
the name, number, and data type of small metadata. However, json-schema lacks constructs that would map well onto
HDF5 Datasets and HDF5 Groups. We might have been able to create our specific flavor of json-schema that did have
constructs for these new primitives, but the other problem is that json-schema does not support the OOP concepts of
inheritance and composition of data types that is used throughout the NWB schema and central to its maintainability.
In the end, json-schema is close but ultimately falls short of our particular needs. That is not surprising given that
it is built to specify json files and our data needs are clearly out of scope. We are not as familiar with XML-schema
much but have the sense that the same limitations would likely apply to that schema language as well. Some other
schema language might come closer but we are not aware of one.

What we found we *were* able to do is create a specification for the hdmf/nwb YAML schema files using json-schema
`here <https://github.com/NeurodataWithoutBorders/nwb-schema/blob/dev/nwb.schema.json>`_, and we can use that schema to
validate that core and extension YAML files meet the hdmf/nwb specifications
`here <https://github.com/NeurodataWithoutBorders/nwb-schema/blob/dev/.github/workflows/validate_schema.yml>`_. This is
a schema of a schema, built to validate the extensions themselves, not data written with those extensions. Still, it
has been very useful to leverage this meta-schema document within our continuous integration framework, as it helps us
ensure that our schema documents follow the HDMF schema language.