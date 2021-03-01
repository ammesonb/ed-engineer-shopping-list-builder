"""
Mel Brandon
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    BeamLaser,
    BurstLaser,
    FrameShiftDrive,
    FrameShiftDriveInterdictor,
    ShieldBooster,
    ShieldCellBank,
    ShieldGenerator,
    Thrusters,
    PulseLaser,
)


# pylint: disable=too-few-public-methods
class MelBrandon(Engineer):
    """
    Mel Brandon
    """

    name = "Mel Brandon"
    max_component_upgrade = {
        BeamLaser: 5,
        BurstLaser: 5,
        FrameShiftDrive: 5,
        FrameShiftDriveInterdictor: 5,
        PulseLaser: 5,
        ShieldBooster: 5,
        ShieldCellBank: 4,
        ShieldGenerator: 5,
        Thrusters: 5,
    }
