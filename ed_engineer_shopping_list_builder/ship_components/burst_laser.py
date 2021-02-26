"""
Burst Laser
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect


class BurstLaser(BaseComponent):
    """
    Burst Laser
    """

    component_classification = Classification.HARDPOINT
    name = "Burst Laser"

    _modifications = [
        Modification.EFFICIENT_WEAPON,
        Modification.FOCUSED_WEAPON,
        Modification.LIGHTWEIGHT_MOUNT,
        Modification.LONG_RANGE_WEAPON,
        Modification.OVERCHARGED_WEAPON,
        Modification.SHORT_RANGE_BLASTER,
        Modification.STURDY_MOUNT,
    ]
    _effects = [
        ExperimentalEffect.CONCORDANT_SEQUENCE,
        ExperimentalEffect.DOUBLE_BRACED,
        ExperimentalEffect.FLOW_CONTROL,
        ExperimentalEffect.INERTIAL_IMPACT,
        ExperimentalEffect.MULTI_SERVOS,
        ExperimentalEffect.OVERSIZED,
        ExperimentalEffect.PHASING_SEQUENCE,
        ExperimentalEffect.SCRAMBLE_SPECTRUM,
        ExperimentalEffect.STRIPPED_DOWN,
        ExperimentalEffect.THERMAL_SHOCK,
    ]

    _default_modification = Modification.LONG_RANGE_WEAPON
    _default_effect = ExperimentalEffect.SCRAMBLE_SPECTRUM
