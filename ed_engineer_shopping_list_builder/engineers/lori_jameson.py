"""
Lori Jameson
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    AFMU,
    FuelScoop,
    KillWarrantScanner,
    LifeSupport,
    ManifestScanner,
    ShieldCellBank,
    Sensors,
    DetailedSurfaceScanner,
    FrameShiftWakeScanner,
    Refinery,
)


# pylint: disable=too-few-public-methods
class LoriJameson(Engineer):
    """
    Lori Jameson
    """

    name = "Lori Jameson"
    max_component_upgrade = {
        AFMU: 4,
        DetailedSurfaceScanner: 5,
        FrameShiftWakeScanner: 3,
        FuelScoop: 4,
        KillWarrantScanner: 3,
        LifeSupport: 4,
        ManifestScanner: 3,
        Refinery: 4,
        Sensors: 5,
        ShieldCellBank: 3,
    }
