# -*- coding: utf-8 -*-
import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBAttributeSpec
# TODO: import other spec classes as needed
# from pynwb.spec import NWBDatasetSpec, NWBLinkSpec, NWBDtypeSpec, NWBRefSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        doc="""Extension describing lab-sepcific metadata for MyBrainLab""",
        name="""ndx-my-brainlab""",
        version="""0.1.0""",
        author=list(map(str.strip, """Peter Brain""".split(','))),
        contact=list(map(str.strip, """peterbrain@brainlab.org""".split(',')))
    )

    # as in which namespace they are found.
    # this is similar to specifying the Python modules that need to be imported
    # to use your new data types.
    # all types included or used by the types specified here will also be
    # included.
    ns_builder.include_type('LabMetaData', namespace='core')

    # Define our LabMetaData type
    labmetadata_ext = NWBGroupSpec(
        name='MyBrainLabMetaData',
        doc='type for storing lab metadata for MyBrainLab',
        neurodata_type_def='MyBrainLabMetaData',
        neurodata_type_inc='LabMetaData',
    )

    # Add custom metadata to our LabMetaData schema
    labmetadata_ext.add_dataset(
        name="tissue_preparation",
        doc="Lab-specific description of the preparation of the tissue",
        dtype='text',
        quantity='?'
    )

    # add all of new data types to this list
    new_data_types = [labmetadata_ext]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)
    print('Spec files generated. Please make sure to rerun `pip install .` to load the changes.')


if __name__ == '__main__':
    # usage: python create_extension_spec.py
    main()
