"""
Mine Launcher
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect


class MineLauncher(BaseComponent):
    """
    Mine Launcher
    """

    component_classification = Classification.HARDPOINT
    name = "Mine Launcher"

    _modifications = [
        Modification.HIGH_CAPACITY_MAGAZINE,
        Modification.LIGHTWEIGHT_MOUNT,
        Modification.RAPID_FIRE_MODIFICATION,
        Modification.STURDY_MOUNT,
    ]

    _effects = [
        ExperimentalEffect.EMISSIVE_MUNITIONS,
        ExperimentalEffect.ION_DISRUPTOR,
        ExperimentalEffect.OVERLOAD_MUNITIONS,
        ExperimentalEffect.FSD_INTERRUPT,
        ExperimentalEffect.RADIANT_CANISTER,
        ExperimentalEffect.REVERBERATING_CASCADE,
        ExperimentalEffect.SHIFT_LOCK_CANISTER,
        ExperimentalEffect.FLOW_CONTROL,
        ExperimentalEffect.OVERSIZED,
        ExperimentalEffect.STRIPPED_DOWN,
        ExperimentalEffect.DOUBLE_BRACED,
    ]

    _default_modification = Modification.HIGH_CAPACITY_MAGAZINE
    _default_effect = ExperimentalEffect.ION_DISRUPTOR
