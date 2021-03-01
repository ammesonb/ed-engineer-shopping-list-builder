"""
Ram Tah
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    ChaffLauncher,
    ElectronicCountermeasure,
    HeatsinkLauncher,
    CollectorLimpetController,
    FuelTransferLimpetController,
    HatchBreakerLimpetController,
    ProspectorLimpetController,
    PointDefence,
)


# pylint: disable=too-few-public-methods
class RamTah(Engineer):
    """
    Ram Tah
    """

    name = "Ram Tah"
    max_component_upgrade = {
        ChaffLauncher: 5,
        CollectorLimpetController: 4,
        ElectronicCountermeasure: 5,
        FuelTransferLimpetController: 4,
        HatchBreakerLimpetController: 3,
        HeatsinkLauncher: 5,
        PointDefence: 5,
        ProspectorLimpetController: 4,
    }
