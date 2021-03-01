"""
Etienne Dorn
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    KillWarrantScanner,
    LifeSupport,
    ManifestScanner,
    PlasmaAccelerator,
    PowerDistributor,
    PowerPlant,
    RailGun,
    Sensors,
    DetailedSurfaceScanner,
    FrameShiftWakeScanner,
)


# pylint: disable=too-few-public-methods
class EtienneDorn(Engineer):
    """
    Etienne Dorn
    """

    name = "Etienne Dorn"
    max_component_upgrade = {
        DetailedSurfaceScanner: 5,
        FrameShiftWakeScanner: 5,
        KillWarrantScanner: 5,
        LifeSupport: 5,
        ManifestScanner: 5,
        PlasmaAccelerator: 5,
        PowerDistributor: 5,
        PowerPlant: 5,
        RailGun: 5,
        Sensors: 5,
    }
