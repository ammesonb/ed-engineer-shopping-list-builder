"""
Chloe Sedesi
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import FrameShiftDrive, Thrusters


# pylint: disable=too-few-public-methods
class ChloeSedesi(Engineer):
    """
    Chloe Sedesi
    """

    name = "Chloe Sedesi"
    max_component_upgrade = {
        FrameShiftDrive: 3,
        Thrusters: 5,
    }
