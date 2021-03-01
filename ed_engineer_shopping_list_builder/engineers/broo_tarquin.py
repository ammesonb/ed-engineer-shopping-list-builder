"""
Broo Tarquin
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    BeamLaser,
    BurstLaser,
    PulseLaser,
)


# pylint: disable=too-few-public-methods
class BrooTarquin(Engineer):
    """
    Broo Tarquin
    """

    name = "Broo Tarquin"
    max_component_upgrade = {
        BeamLaser: 5,
        BurstLaser: 5,
        PulseLaser: 5,
    }
