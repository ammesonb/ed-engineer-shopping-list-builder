"""
Missile Rack
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect


class MissileRack(BaseComponent):
    """
    Missile Rack
    """

    component_classification = Classification.HARDPOINT
    name = "Missile Rack"

    _modifications = [
        Modification.HIGH_CAPACITY_MAGAZINE,
        Modification.LIGHTWEIGHT_MOUNT,
        Modification.RAPID_FIRE_MODIFICATION,
        Modification.STURDY_MOUNT,
    ]

    _effects = [
        ExperimentalEffect.DRAG_MUNITION,
        ExperimentalEffect.EMISSIVE_MUNITIONS,
        ExperimentalEffect.FLOW_CONTROL,
        ExperimentalEffect.FSD_INTERRUPT,
        ExperimentalEffect.MULTI_SERVOS,
        ExperimentalEffect.OVERLOAD_MUNITIONS,
        ExperimentalEffect.OVERSIZED,
        ExperimentalEffect.PENETRATOR_MUNITIONS,
        ExperimentalEffect.STRIPPED_DOWN,
        ExperimentalEffect.THERMAL_CASCADE,
    ]

    _default_modification = Modification.HIGH_CAPACITY_MAGAZINE
    _default_effect = ExperimentalEffect.DRAG_MUNITION
