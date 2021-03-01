"""
Tiana Fortune
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    KillWarrantScanner,
    ManifestScanner,
    FrameShiftWakeScanner,
    ProspectorLimpetController,
    HatchBreakerLimpetController,
    FuelTransferLimpetController,
    CollectorLimpetController,
    DetailedSurfaceScanner,
    Sensors,
    FrameShiftDriveInterdictor,
)


# pylint: disable=too-few-public-methods
class TianaFortune(Engineer):
    """
    Tiana Fortune
    """

    name = "Tiana Fortune"
    max_component_upgrade = {
        CollectorLimpetController: 5,
        DetailedSurfaceScanner: 3,
        FrameShiftDriveInterdictor: 3,
        FrameShiftWakeScanner: 5,
        FuelTransferLimpetController: 5,
        HatchBreakerLimpetController: 5,
        KillWarrantScanner: 5,
        ManifestScanner: 5,
        ProspectorLimpetController: 5,
        Sensors: 5,
    }
