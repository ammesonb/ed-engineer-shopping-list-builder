"""
Didi Vatermann
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    ShieldBooster,
    ShieldGenerator,
)


# pylint: disable=too-few-public-methods
class DidiVatermann(Engineer):
    """
    Didi Vatermann
    """

    name = "Didi Vatermann"
    max_component_upgrade = {
        ShieldBooster: 5,
        ShieldGenerator: 3,
    }
