"""
Hera Tani
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    PowerPlant,
    PowerDistributor,
    Sensors,
    DetailedSurfaceScanner,
)


# pylint: disable=too-few-public-methods
class HeraTani(Engineer):
    """
    Hera Tani
    """

    name = "Hera Tani"
    max_component_upgrade = {
        DetailedSurfaceScanner: 5,
        PowerDistributor: 3,
        PowerPlant: 5,
        Sensors: 3,
    }
