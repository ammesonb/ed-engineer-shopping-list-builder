"""
Shield Cell Bank
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect


class ShieldCellBank(BaseComponent):
    """
    Shield Cell Bank
    """

    component_classification = Classification.OPTIONAL_INTERNAL
    name = "Shield Cell Bank"

    _modifications = [
        Modification.RAPID_CHARGE,
        Modification.SPECIALISED,
    ]
    _effects = [
        ExperimentalEffect.RECYCLING_CELLS,
        ExperimentalEffect.DOUBLE_BRACED,
        ExperimentalEffect.FLOW_CONTROL,
        ExperimentalEffect.BOSS_CELLS,
        ExperimentalEffect.STRIPPED_DOWN,
    ]

    _default_modification = Modification.SPECIALISED
    _default_effect = ExperimentalEffect.FLOW_CONTROL
