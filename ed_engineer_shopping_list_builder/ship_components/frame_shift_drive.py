"""
Frame Shift Drive
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect


class FrameShiftDrive(BaseComponent):
    """
    Frame Shift Drive
    """

    component_classification = Classification.CORE
    name = "Frame Shift Drive"

    _modifications = [
        Modification.FASTER_FSD_BOOT_SEQUENCE,
        Modification.INCREASED_FSD_RANGE,
        Modification.SHIELDED_FSD,
    ]
    _effects = [
        ExperimentalEffect.DEEP_CHARGE,
        ExperimentalEffect.MASS_MANAGER,
        ExperimentalEffect.DOUBLE_BRACED,
        ExperimentalEffect.STRIPPED_DOWN,
        ExperimentalEffect.THERMAL_SPREAD,
    ]

    _default_modification = Modification.INCREASED_FSD_RANGE
    _default_effect = ExperimentalEffect.MASS_MANAGER
