"""
Power Plant
"""
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect
from ed_engineer_shopping_list_builder.ship_components.shielded_component import (
    BaseComponent,
)


class PowerPlant(BaseComponent):
    """
    Power Plant
    """

    name = "Power Plant"
    component_classification = Classification.CORE

    _modifications = [
        Modification.ARMOURED,
        Modification.LOW_EMISSIONS,
        Modification.OVERCHARGED,
    ]

    _effects = [
        ExperimentalEffect.DOUBLE_BRACED,
        ExperimentalEffect.MONSTERED,
        ExperimentalEffect.STRIPPED_DOWN,
        ExperimentalEffect.THERMAL_SPREAD,
    ]

    _default_modification = Modification.OVERCHARGED
    _default_effect = ExperimentalEffect.MONSTERED
