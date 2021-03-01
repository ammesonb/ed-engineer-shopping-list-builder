"""
Bill Turner
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    AFMU,
    FuelScoop,
    Refinery,
    FrameShiftWakeScanner,
    KillWarrantScanner,
    ManifestScanner,
    PlasmaAccelerator,
    LifeSupport,
    Sensors,
    DetailedSurfaceScanner,
)


# pylint: disable=too-few-public-methods
class BillTurner(Engineer):
    """
    Bill Turner
    """

    name = "Bill Turner"
    max_component_upgrade = {
        AFMU: 3,
        DetailedSurfaceScanner: 5,
        FrameShiftWakeScanner: 3,
        FuelScoop: 3,
        KillWarrantScanner: 3,
        LifeSupport: 3,
        ManifestScanner: 3,
        PlasmaAccelerator: 5,
        Refinery: 3,
        Sensors: 5,
    }
