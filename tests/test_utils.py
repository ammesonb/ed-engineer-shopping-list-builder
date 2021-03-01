"""
Tests utility functions
"""
from ed_engineer_shopping_list_builder import utils
from ed_engineer_shopping_list_builder.classification import Classification

from ed_engineer_shopping_list_builder.ship_components import (
    PowerPlant,
    Sensors,
    BeamLaser,
    MultiCannon,
    ChaffLauncher,
    ElectronicCountermeasure,
    DetailedSurfaceScanner,
    ShieldGenerator,
)


def test_organize_by_classification():
    """
    .
    """
    assert utils.organize_components_by_classification(
        [
            BeamLaser,
            ChaffLauncher,
            DetailedSurfaceScanner,
            ElectronicCountermeasure,
            MultiCannon,
            PowerPlant,
            Sensors,
            ShieldGenerator,
        ]
    ) == {
        Classification.CORE: [PowerPlant, Sensors],
        Classification.OPTIONAL_INTERNAL: [DetailedSurfaceScanner, ShieldGenerator],
        Classification.HARDPOINT: [BeamLaser, MultiCannon],
        Classification.UTILITY: [ChaffLauncher, ElectronicCountermeasure],
    }, "Components correctly organized"


def test_get_component_summary():
    """
    .
    """
    components = {
        Classification.CORE: [PowerPlant, Sensors],
        Classification.OPTIONAL_INTERNAL: [DetailedSurfaceScanner, ShieldGenerator],
        Classification.HARDPOINT: [BeamLaser, MultiCannon],
        Classification.UTILITY: [ChaffLauncher, ElectronicCountermeasure],
    }

    summary = utils.get_component_summary_by_classification(
        components, lambda component: component.name
    )
    assert summary == "\n".join(
        [
            "-" * 40,
            "CORE",
            "-" * 40,
            "",
            PowerPlant.name,
            Sensors.name,
            "",
            "",
            "-" * 40,
            "HARDPOINT",
            "-" * 40,
            "",
            BeamLaser.name,
            MultiCannon.name,
            "",
            "",
            "-" * 40,
            "OPTIONAL INTERNAL",
            "-" * 40,
            "",
            ShieldGenerator.name,
            DetailedSurfaceScanner.name,
            "",
            "",
            "-" * 40,
            "UTILITY",
            "-" * 40,
            "",
            ChaffLauncher.name,
            ElectronicCountermeasure.name,
            "",
            "",
            "",
        ]
    ), "Summary is correct"
