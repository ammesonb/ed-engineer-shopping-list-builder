"""
The Dweller
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    BeamLaser,
    BurstLaser,
    PowerDistributor,
    PulseLaser,
)


# pylint: disable=too-few-public-methods
class TheDweller(Engineer):
    """
    The Dweller
    """

    name = "The Dweller"
    max_component_upgrade = {
        BeamLaser: 3,
        BurstLaser: 3,
        PowerDistributor: 5,
        PulseLaser: 4,
    }
