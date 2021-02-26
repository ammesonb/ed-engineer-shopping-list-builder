"""
Shield Generator
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect


class ShieldGenerator(BaseComponent):
    """
    Shield Generator
    """

    component_classification = Classification.OPTIONAL_INTERNAL
    name = "Shield Generator"
    is_singleton = True

    _modifications = [
        Modification.ENHANCED_LOW_POWER_SHIELDS,
        Modification.REINFORCED_SHIELDS,
        Modification.KINETIC_RESISTANT_SHIELDS,
        Modification.THERMAL_RESISTANT_SHIELDS,
    ]
    _effects = [
        ExperimentalEffect.FAST_CHARGE,
        ExperimentalEffect.MULTI_WEAVE,
        ExperimentalEffect.HI_CAP,
        ExperimentalEffect.LO_DRAW,
        ExperimentalEffect.THERMO_BLOCK,
        ExperimentalEffect.FORCE_BLOCK,
        ExperimentalEffect.DOUBLE_BRACED,
        ExperimentalEffect.STRIPPED_DOWN,
    ]

    _default_modification = Modification.REINFORCED_SHIELDS
    _default_effect = ExperimentalEffect.FAST_CHARGE
