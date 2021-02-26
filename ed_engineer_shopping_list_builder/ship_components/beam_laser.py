"""
Beam Laser
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect


class BeamLaser(BaseComponent):
    """
    Beam Laser
    """

    component_classification = Classification.HARDPOINT
    name = "Beam Laser"

    _modifications = [
        Modification.EFFICIENT_WEAPON,
        Modification.LIGHTWEIGHT_MOUNT,
        Modification.LONG_RANGE_WEAPON,
        Modification.OVERCHARGED_WEAPON,
        Modification.SHORT_RANGE_BLASTER,
        Modification.STURDY_MOUNT,
    ]
    _effects = [
        ExperimentalEffect.STRIPPED_DOWN,
        ExperimentalEffect.OVERSIZED,
        ExperimentalEffect.FLOW_CONTROL,
        ExperimentalEffect.DOUBLE_BRACED,
        ExperimentalEffect.THERMAL_VENT,
        ExperimentalEffect.CONCORDANT_SEQUENCE,
        ExperimentalEffect.THERMAL_SHOCK,
        ExperimentalEffect.REGENERATION_SEQUENCE,
        ExperimentalEffect.THERMAL_CONDUIT,
    ]

    _default_modification = Modification.EFFICIENT_WEAPON
    _default_effect = ExperimentalEffect.THERMAL_VENT
