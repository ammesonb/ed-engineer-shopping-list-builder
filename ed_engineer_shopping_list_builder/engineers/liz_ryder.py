"""
Liz Ryder
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    HullReinforcementPackage,
    Armour,
    MineLauncher,
    MissileRack,
    TorpedoPylon,
)


# pylint: disable=too-few-public-methods
class LizRyder(Engineer):
    """
    Liz Ryder
    """

    name = "Liz Ryder"
    max_component_upgrade = {
        Armour: 1,
        HullReinforcementPackage: 1,
        MineLauncher: 3,
        MissileRack: 5,
        TorpedoPylon: 5,
    }
