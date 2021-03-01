"""
Lei Cheung
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    Sensors,
    ShieldBooster,
    ShieldGenerator,
    DetailedSurfaceScanner,
)


# pylint: disable=too-few-public-methods
class LeiCheung(Engineer):
    """
    Lei Cheung
    """

    name = "Lei Cheung"
    max_component_upgrade = {
        DetailedSurfaceScanner: 5,
        Sensors: 5,
        ShieldBooster: 3,
        ShieldGenerator: 5,
    }
