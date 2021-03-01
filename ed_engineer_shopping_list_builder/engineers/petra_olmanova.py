"""
Petra Olmanova
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    Armour,
    AFMU,
    ChaffLauncher,
    ElectronicCountermeasure,
    HeatsinkLauncher,
    HullReinforcementPackage,
    MineLauncher,
    MissileRack,
    PointDefence,
    TorpedoPylon,
)


# pylint: disable=too-few-public-methods
class PetraOlmanova(Engineer):
    """
    Petra Olmanova
    """

    name = "Petra Olmanova"
    max_component_upgrade = {
        AFMU: 5,
        Armour: 5,
        ChaffLauncher: 5,
        ElectronicCountermeasure: 5,
        HeatsinkLauncher: 5,
        HullReinforcementPackage: 5,
        MineLauncher: 5,
        MissileRack: 5,
        PointDefence: 5,
        TorpedoPylon: 5,
    }
