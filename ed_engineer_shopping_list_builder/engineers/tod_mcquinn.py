"""
Tod McQuinn
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    Cannon,
    FragmentCannon,
    MultiCannon,
    RailGun,
)


# pylint: disable=too-few-public-methods
class TodMcQuinn(Engineer):
    """
    Tod McQuinn
    """

    name = "Tod McQuinn"
    max_component_upgrade = {
        Cannon: 2,
        FragmentCannon: 3,
        MultiCannon: 5,
        RailGun: 5,
    }
