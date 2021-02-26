"""
Hull Reinforcement Package
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect


class HullReinforcementPackage(BaseComponent):
    """
    Hull Reinforcement Package
    """

    component_classification = Classification.OPTIONAL_INTERNAL
    name = "Hull Reinforcement Package"

    _modifications = [
        Modification.BLAST_RESISTANT_HULL_REINFORCEMENT,
        Modification.HEAVY_DUTY_HULL_REINFORCEMENT,
        Modification.KINETIC_RESISTANT_HULL_REINFORCEMENT,
        Modification.LIGHTWEIGHT_HULL_REINFORCEMENT,
        Modification.THERMAL_RESISTANT_HULL_REINFORCEMENT,
    ]
    _effects = [
        ExperimentalEffect.ANGLED_PLATING,
        ExperimentalEffect.DEEP_PLATING,
        ExperimentalEffect.LAYERED_PLATING,
        ExperimentalEffect.REFLECTIVE_PLATING,
    ]

    _default_modification = Modification.HEAVY_DUTY_HULL_REINFORCEMENT
    _default_effect = ExperimentalEffect.DEEP_PLATING
