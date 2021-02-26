"""
Armour
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect


class Armour(BaseComponent):
    """
    Armour
    """

    component_classification = Classification.CORE
    name = "Armour"

    _modifications = [
        Modification.BLAST_RESISTANT,
        Modification.HEAVY_DUTY,
        Modification.KINETIC_RESISTANT,
        Modification.LIGHTWEIGHT,
        Modification.THERMAL_RESISTANT,
    ]
    _effects = [
        ExperimentalEffect.ANGLED_PLATING,
        ExperimentalEffect.DEEP_PLATING,
        ExperimentalEffect.LAYERED_PLATING,
        ExperimentalEffect.REFLECTIVE_PLATING,
    ]

    _default_modification = Modification.HEAVY_DUTY
    _default_effect = ExperimentalEffect.DEEP_PLATING
