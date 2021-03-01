"""
Bris Dekker
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    FrameShiftDriveInterdictor,
    FrameShiftDrive,
)


# pylint: disable=too-few-public-methods
class BrisDekker(Engineer):
    """
    Bris Dekker
    """

    name = "Bris Dekker"
    max_component_upgrade = {
        FrameShiftDrive: 3,
        FrameShiftDriveInterdictor: 4,
    }
