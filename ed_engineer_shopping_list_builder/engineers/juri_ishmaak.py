"""
Juri Ishmaak
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    ManifestScanner,
    KillWarrantScanner,
    MissileRack,
    TorpedoPylon,
    DetailedSurfaceScanner,
    Sensors,
    FrameShiftWakeScanner,
    MineLauncher,
)


# pylint: disable=too-few-public-methods
class JuriIshmaak(Engineer):
    """
    Juri Ishmaak
    """

    name = "Juri Ishmaak"
    max_component_upgrade = {
        DetailedSurfaceScanner: 5,
        FrameShiftWakeScanner: 3,
        KillWarrantScanner: 3,
        ManifestScanner: 3,
        MineLauncher: 5,
        MissileRack: 3,
        Sensors: 5,
        TorpedoPylon: 3,
    }
