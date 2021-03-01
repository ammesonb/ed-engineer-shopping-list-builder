"""
Selene Jean
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    Armour,
    HullReinforcementPackage,
)


# pylint: disable=too-few-public-methods
class SeleneJean(Engineer):
    """
    Selene Jean
    """

    name = "Selene Jean"
    max_component_upgrade = {
        Armour: 5,
        HullReinforcementPackage: 5,
    }
