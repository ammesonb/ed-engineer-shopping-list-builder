"""
FragmentCannon
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect


class FragmentCannon(BaseComponent):
    """
    FragmentCannon
    """

    component_classification = Classification.HARDPOINT
    name = "Fragment Cannon"

    _modifications = [
        Modification.DOUBLE_SHOT,
        Modification.EFFICIENT_WEAPON,
        Modification.HIGH_CAPACITY_MAGAZINE,
        Modification.LIGHTWEIGHT_MOUNT,
        Modification.OVERCHARGED_WEAPON,
        Modification.RAPID_FIRE_MODIFICATION,
        Modification.STURDY_MOUNT,
    ]
    _effects = [
        ExperimentalEffect.CORROSIVE_SHELL,
        ExperimentalEffect.DAZZLE_SHELL,
        ExperimentalEffect.DRAG_MUNITION,
        ExperimentalEffect.FLOW_CONTROL,
        ExperimentalEffect.INCENDIARY_ROUNDS,
        ExperimentalEffect.SCREENING_SHELL,
    ]

    _default_modification = Modification.DOUBLE_SHOT
    _default_effect = ExperimentalEffect.DRAG_MUNITION
