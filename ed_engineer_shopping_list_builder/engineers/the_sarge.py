"""
The Sarge
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    Cannon,
    CollectorLimpetController,
    FuelTransferLimpetController,
    HatchBreakerLimpetController,
    ProspectorLimpetController,
    RailGun,
)


# pylint: disable=too-few-public-methods
class TheSarge(Engineer):
    """
    The Sarge
    """

    name = "The Sarge"
    max_component_upgrade = {
        Cannon: 5,
        CollectorLimpetController: 5,
        FuelTransferLimpetController: 5,
        HatchBreakerLimpetController: 5,
        ProspectorLimpetController: 5,
        RailGun: 3,
    }
