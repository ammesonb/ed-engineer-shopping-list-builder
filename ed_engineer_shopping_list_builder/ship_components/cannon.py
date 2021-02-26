"""
Cannon
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect


class Cannon(BaseComponent):
    """
    Cannon
    """

    component_classification = Classification.HARDPOINT
    name = "Cannon"

    _modifications = [
        Modification.EFFICIENT_WEAPON,
        Modification.HIGH_CAPACITY_MAGAZINE,
        Modification.LIGHTWEIGHT_MOUNT,
        Modification.LONG_RANGE_WEAPON,
        Modification.OVERCHARGED_WEAPON,
        Modification.RAPID_FIRE_MODIFICATION,
        Modification.SHORT_RANGE_BLASTER,
        Modification.STURDY_MOUNT,
    ]
    _effects = [
        ExperimentalEffect.AUTO_LOADER,
        ExperimentalEffect.DISPERSAL_FIELD,
        ExperimentalEffect.SMART_ROUNDS,
        ExperimentalEffect.FORCE_SHELL,
        ExperimentalEffect.HIGH_YIELD_SHELL,
        ExperimentalEffect.THERMAL_CASCADE,
        ExperimentalEffect.OVERSIZED,
        ExperimentalEffect.STRIPPED_DOWN,
        ExperimentalEffect.FLOW_CONTROL,
        ExperimentalEffect.DOUBLE_BRACED,
        ExperimentalEffect.MULTI_SERVOS,
    ]

    _default_modification = Modification.LONG_RANGE_WEAPON
    _default_effect = ExperimentalEffect.AUTO_LOADER
