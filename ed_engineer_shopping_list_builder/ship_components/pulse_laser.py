"""
Beam Laser
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect


class PulseLaser(BaseComponent):
    """
    Pulse Laser
    """

    component_classification = Classification.HARDPOINT
    name = "Pulse Laser"

    _modifications = [
        Modification.EFFICIENT_WEAPON,
        Modification.FOCUSED_WEAPON,
        Modification.LIGHTWEIGHT_MOUNT,
        Modification.LONG_RANGE_WEAPON,
        Modification.OVERCHARGED_WEAPON,
        Modification.RAPID_FIRE_MODIFICATION,
        Modification.STURDY_MOUNT,
    ]
    _effects = [
        ExperimentalEffect.CONCORDANT_SEQUENCE,
        ExperimentalEffect.EMISSIVE_MUNITIONS,
        ExperimentalEffect.PHASING_SEQUENCE,
        ExperimentalEffect.SCRAMBLE_SPECTRUM,
        ExperimentalEffect.THERMAL_SHOCK,
    ]

    _default_modification = Modification.LONG_RANGE_WEAPON
    _default_effect = ExperimentalEffect.SCRAMBLE_SPECTRUM
