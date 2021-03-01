"""
Marsha Hicks
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    Cannon,
    CollectorLimpetController,
    FragmentCannon,
    FuelScoop,
    FuelTransferLimpetController,
    HatchBreakerLimpetController,
    MultiCannon,
    ProspectorLimpetController,
    Refinery,
)


# pylint: disable=too-few-public-methods
class MarshaHicks(Engineer):
    """
    Marsha Hicks
    """

    name = "Marsha Hicks"
    max_component_upgrade = {
        Cannon: 5,
        CollectorLimpetController: 5,
        FragmentCannon: 5,
        FuelScoop: 5,
        FuelTransferLimpetController: 5,
        HatchBreakerLimpetController: 5,
        MultiCannon: 5,
        ProspectorLimpetController: 5,
        Refinery: 5,
    }
