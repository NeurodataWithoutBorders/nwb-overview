.. _analysistools-deeplabcut:

DeepLabCut
----------

.. short_description_start

:ref:`analysistools-deeplabcut` is an efficient method for 2D and 3D markerless
pose estimation based on transfer learning with deep neural networks that
achieves excellent results (i.e. you can match human labeling accuracy) with
minimal training data (typically 50-200 frames). We demonstrate the versatility
of this framework by tracking various body parts in multiple species across a
broad collection of behaviors.
:bdg-link-primary:`Documentation <http://www.mackenziemathislab.org/deeplabcut>`

.. short_description_end


.. image:: deeplabcut.gif
    :class: align-left
    :width: 400

DeepLabCut has developed `DLC2NWB <https://github.com/DeepLabCut/DLC2NWB>`_, a
Python package for converting from their native output format to NWB. This
library uses the NWB extension `ndx-pose <https://github.com/rly/ndx-pose>`_,
which aims to provide a standardized format for storing pose estimation data in
NWB. ndx-pose was developed initially to store the output of DeepLabCut in NWB,
but is also designed to store the output of general pose estimation tools.