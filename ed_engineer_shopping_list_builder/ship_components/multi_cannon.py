"""
MultiCannon
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect


class MultiCannon(BaseComponent):
    """
    MultiCannon
    """

    component_classification = Classification.HARDPOINT
    name = "Multi-cannon"

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
        ExperimentalEffect.CORROSIVE_SHELL,
        ExperimentalEffect.DOUBLE_BRACED,
        ExperimentalEffect.EMISSIVE_MUNITIONS,
        ExperimentalEffect.FLOW_CONTROL,
        ExperimentalEffect.INCENDIARY_ROUNDS,
        ExperimentalEffect.MULTI_SERVOS,
        ExperimentalEffect.OVERSIZED,
        ExperimentalEffect.SMART_ROUNDS,
        ExperimentalEffect.STRIPPED_DOWN,
        ExperimentalEffect.THERMAL_SHOCK,
    ]

    _default_modification = Modification.OVERCHARGED_WEAPON
