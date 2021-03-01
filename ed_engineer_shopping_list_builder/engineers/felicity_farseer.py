"""
Felicity Farseer
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    FrameShiftDriveInterdictor,
    DetailedSurfaceScanner,
    ShieldBooster,
    PowerPlant,
    Thrusters,
    Sensors,
    FrameShiftDrive,
)


# pylint: disable=too-few-public-methods
class FelicityFarseer(Engineer):
    """
    Felicity Farseer
    """

    name = "Felicity Farseer"
    max_component_upgrade = {
        DetailedSurfaceScanner: 3,
        FrameShiftDrive: 5,
        FrameShiftDriveInterdictor: 1,
        PowerPlant: 1,
        Sensors: 3,
        ShieldBooster: 1,
        Thrusters: 3,
    }
