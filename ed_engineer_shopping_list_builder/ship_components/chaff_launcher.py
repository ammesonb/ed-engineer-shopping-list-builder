"""
Chaff Launcher
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification


class ChaffLauncher(BaseComponent):
    """
    Chaff Launcher
    """

    name = "Chaff Launcher"
    component_classification = Classification.UTILITY

    _modifications = [
        Modification.AMMO_CAPACITY,
        Modification.LIGHTWEIGHT,
        Modification.REINFORCED,
        Modification.SHIELDED,
    ]

    _default_modification = Modification.AMMO_CAPACITY
