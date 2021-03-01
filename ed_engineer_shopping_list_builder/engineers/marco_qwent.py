"""
Marco Qwent
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    PowerDistributor,
    PowerPlant,
)


# pylint: disable=too-few-public-methods
class MarcoQwent(Engineer):
    """
    Marco Qwent
    """

    name = "Marco Qwent"
    max_component_upgrade = {
        PowerDistributor: 3,
        PowerPlant: 4,
    }
