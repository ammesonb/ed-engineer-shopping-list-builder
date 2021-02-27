"""
Test ship functionality
"""

from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect
from ed_engineer_shopping_list_builder.ship import Ship, is_component_unique
from ed_engineer_shopping_list_builder.ship_components import (
    PowerPlant,
    ShieldGenerator,
    BeamLaser,
    ChaffLauncher,
)
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)


def test_is_component_unique():
    """
    Check component uniqueness
    """

    assert is_component_unique(PowerPlant), "Power plant is unique"
    assert is_component_unique(ShieldGenerator), "Shield generator is unique"
    assert not is_component_unique(BeamLaser), "Beam laser is not unique"


def test_add_remove_components(monkeypatch):
    """
    .
    """
    ship = Ship()

    monkeypatch.setattr(BaseComponent, "configure", lambda self: None)

    power = PowerPlant()
    shield = ShieldGenerator()
    laser1 = BeamLaser()
    laser2 = BeamLaser()
    ship.add_component(power)
    ship.add_component(laser1)
    ship.add_component(shield)
    ship.add_component(laser2)

    assert ship.component_list == [
        laser1,
        laser2,
        power,
        shield,
    ], "Component list correct"

    assert ship.outfitted == {
        power.name: power,
        shield.name: shield,
        laser1.name: [laser1, laser2],
    }, "Outfitted modules correct"

    ship.remove_component(laser1)
    ship.remove_component(shield)

    assert ship.component_list == [
        laser2,
        power,
    ], "Component list correct post-removal"

    assert ship.outfitted == {
        power.name: power,
        laser1.name: [laser2],
    }, "Outfitted modules correct"


def test_summarize(monkeypatch):
    """
    .
    """
    ship = Ship()

    monkeypatch.setattr(BaseComponent, "configure", lambda self: None)
    power = PowerPlant()
    power.max_modification_grade = 4
    power.selected_modification = Modification.ARMOURED
    power.selected_effect = ExperimentalEffect.MONSTERED

    beam = BeamLaser()
    beam.max_modification_grade = 5
    beam.selected_modification = Modification.EFFICIENT_WEAPON
    beam.selected_effect = ExperimentalEffect.THERMAL_VENT

    shield = ShieldGenerator()
    shield.max_modification_grade = 5
    shield.selected_effect = ExperimentalEffect.FAST_CHARGE

    chaff = ChaffLauncher()
    chaff.max_modification_grade = 2
    chaff.selected_modification = Modification.AMMO_CAPACITY

    ship.add_component(power)
    ship.add_component(beam)
    ship.add_component(shield)
    ship.add_component(chaff)

    summary = ship.summarize()
    assert summary == "\n".join(
        [
            "-" * 40,
            "CORE",
            "-" * 40,
            "",
            str(power),
            "",
            "",
            "-" * 40,
            "HARDPOINT",
            "-" * 40,
            "",
            str(beam),
            "",
            "",
            "-" * 40,
            "OPTIONAL INTERNAL",
            "-" * 40,
            "",
            str(shield),
            "",
            "",
            "-" * 40,
            "UTILITY",
            "-" * 40,
            "",
            str(chaff),
            "",
            "",
            "",
        ]
    )


def test_to_shopping_list(monkeypatch):
    """
    .
    """
    ship = Ship()

    monkeypatch.setattr(BaseComponent, "configure", lambda self: None)
    power = PowerPlant()
    power.max_modification_grade = 4
    power.selected_modification = Modification.ARMOURED
    power.selected_effect = ExperimentalEffect.MONSTERED

    beam = BeamLaser()
    beam.max_modification_grade = 5
    beam.selected_modification = Modification.EFFICIENT_WEAPON
    beam.selected_effect = ExperimentalEffect.THERMAL_VENT

    shield = ShieldGenerator()
    shield.max_modification_grade = 5
    shield.selected_effect = ExperimentalEffect.FAST_CHARGE

    chaff = ChaffLauncher()
    chaff.max_modification_grade = 2
    chaff.selected_modification = Modification.AMMO_CAPACITY

    ship.add_component(power)
    ship.add_component(beam)
    ship.add_component(shield)
    ship.add_component(chaff)

    grade_counts = {i: i for i in range(1, 6)}
    shopping_list = ship.to_shopping_list("cmdr", grade_counts)
    assert (
        shopping_list
        == "["
        + ",".join(
            [
                beam.to_shopping_list("cmdr", grade_counts),
                chaff.to_shopping_list("cmdr", grade_counts),
                power.to_shopping_list("cmdr", grade_counts),
                shield.to_shopping_list("cmdr", grade_counts),
            ]
        )
        + "]"
    ), "Shopping list correct"
