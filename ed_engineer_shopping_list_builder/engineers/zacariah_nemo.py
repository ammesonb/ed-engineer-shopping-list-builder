"""
Zacariah Nemo
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    FragmentCannon,
    MultiCannon,
    PlasmaAccelerator,
)


# pylint: disable=too-few-public-methods
class ZacariahNemo(Engineer):
    """
    Zacariah Nemo
    """

    name = "Zacariah Nemo"
    max_component_upgrade = {
        FragmentCannon: 5,
        MultiCannon: 3,
        PlasmaAccelerator: 2,
    }
