"""
Electronic Countermeasure
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification


class ElectronicCountermeasure(BaseComponent):
    """
    Electronic Countermeasure
    """

    name = "Electronic Countermeasure"
    component_classification = Classification.UTILITY

    _modifications = [
        Modification.LIGHTWEIGHT,
        Modification.REINFORCED,
        Modification.SHIELDED,
    ]
