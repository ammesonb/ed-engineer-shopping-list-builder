"""
Life Support
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect


class LifeSupport(BaseComponent):
    """
    Life Support
    """

    name = "Life Support"
    component_classification = Classification.CORE

    _modifications = [
        Modification.LIGHTWEIGHT,
        Modification.REINFORCED,
        Modification.SHIELDED,
    ]
