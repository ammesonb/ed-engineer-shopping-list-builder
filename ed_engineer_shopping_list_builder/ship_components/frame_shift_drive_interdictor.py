"""
Frame Shift Drive Interdictor
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect


class FrameShiftDriveInterdictor(BaseComponent):
    """
    Frame Shift Drive Interdictor
    """

    name = "Frame Shift Drive Interdictor"
    component_classification = Classification.OPTIONAL_INTERNAL
    is_singleton = True

    _modifications = [
        Modification.EXPANDED_FSD_INTERDICTOR_CAPTURE_ARC,
        Modification.LONG_RANGE_FSD_INTERDICTOR,
    ]

    _default_modification = Modification.LONG_RANGE_FSD_INTERDICTOR
