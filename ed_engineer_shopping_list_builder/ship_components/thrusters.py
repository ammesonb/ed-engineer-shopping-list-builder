"""
Thrusters
"""
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect
from ed_engineer_shopping_list_builder.ship_components.shielded_component import (
    BaseComponent,
)


class Thrusters(BaseComponent):
    """
    Thrusters
    """

    name = "Thrusters"
    component_classification = Classification.CORE

    _modifications = [
        Modification.CLEAN_DRIVE_TUNING,
        Modification.DIRTY_DRIVE_TUNING,
        Modification.DRIVE_STRENGTHENING,
    ]

    _effects = [
        ExperimentalEffect.DOUBLE_BRACED,
        ExperimentalEffect.DRAG_DRIVES,
        ExperimentalEffect.DRIVE_DISTRIBUTORS,
        ExperimentalEffect.STRIPPED_DOWN,
        ExperimentalEffect.THERMAL_SPREAD,
    ]

    _default_modification = Modification.DIRTY_DRIVE_TUNING
    _default_effect = ExperimentalEffect.DRAG_DRIVES
