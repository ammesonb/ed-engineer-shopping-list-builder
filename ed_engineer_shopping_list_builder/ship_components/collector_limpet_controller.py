"""
Collector Limpet Controller
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect


class CollectorLimpetController(BaseComponent):
    """
    Collector Limpet Controller
    """

    name = "Collector Limpet Controller"
    component_classification = Classification.OPTIONAL_INTERNAL

    _modifications = [
        Modification.LIGHTWEIGHT,
        Modification.REINFORCED,
        Modification.SHIELDED,
    ]
