"""
Elvira Martuuk
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    FrameShiftDrive,
    ShieldCellBank,
    ShieldGenerator,
    Thrusters,
)


# pylint: disable=too-few-public-methods
class ElviraMartuuk(Engineer):
    """
    Elvira Martuuk
    """

    name = "Elvira Martuuk"
    max_component_upgrade = {
        FrameShiftDrive: 5,
        ShieldCellBank: 1,
        ShieldGenerator: 3,
        Thrusters: 2,
    }
