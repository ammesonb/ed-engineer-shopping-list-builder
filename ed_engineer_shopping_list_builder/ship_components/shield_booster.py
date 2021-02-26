"""
Shield Booster
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect


class ShieldBooster(BaseComponent):
    """
    Shield Booster
    """

    component_classification = Classification.UTILITY
    name = "Shield Booster"

    _modifications = [
        Modification.BLAST_RESISTANT,
        Modification.HEAVY_DUTY,
        Modification.KINETIC_RESISTANT,
        Modification.RESISTANCE_AUGMENTED,
        Modification.THERMAL_RESISTANT,
    ]
    _effects = [
        ExperimentalEffect.FORCE_BLOCK,
        ExperimentalEffect.SUPER_CAPACITOR,
        ExperimentalEffect.DOUBLE_BRACED,
        ExperimentalEffect.FLOW_CONTROL,
        ExperimentalEffect.BLAST_BLOCK,
        ExperimentalEffect.THERMO_BLOCK,
    ]

    _default_modification = Modification.THERMAL_RESISTANT
    _default_effect = ExperimentalEffect.THERMO_BLOCK
