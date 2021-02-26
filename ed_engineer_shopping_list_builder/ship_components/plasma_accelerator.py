"""
Plasma Accelerator
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect


class PlasmaAccelerator(BaseComponent):
    """
    Plasma Accelerator
    """

    component_classification = Classification.HARDPOINT
    name = "Plasma Accelerator"

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
        ExperimentalEffect.DAZZLE_SHELL,
        ExperimentalEffect.DISPERSAL_FIELD,
        ExperimentalEffect.DOUBLE_BRACED,
        ExperimentalEffect.FLOW_CONTROL,
        ExperimentalEffect.MULTI_SERVOS,
        ExperimentalEffect.OVERSIZED,
        ExperimentalEffect.PHASING_SEQUENCE,
        ExperimentalEffect.PLASMA_SLUG,
        ExperimentalEffect.STRIPPED_DOWN,
        ExperimentalEffect.TARGET_LOCK_BREAKER,
        ExperimentalEffect.THERMAL_CONDUIT,
    ]

    _default_modification = Modification.EFFICIENT_WEAPON
    _default_effect = ExperimentalEffect.TARGET_LOCK_BREAKER
