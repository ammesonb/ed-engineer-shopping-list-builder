"""
Test base component functionality
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.ship_components import PowerPlant
from ed_engineer_shopping_list_builder import inputs
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect
from ed_engineer_shopping_list_builder.utils import counter_wrapper


def test_creation(monkeypatch):
    """
    .
    """
    # pylint: disable=unused-argument
    @counter_wrapper
    def configure(self):
        """
        .
        """

    monkeypatch.setattr(BaseComponent, "configure", configure)
    component = BaseComponent()
    assert configure.counter == 1, "Component configured"
    assert not component.selected_effect, "No default effect"
    assert not component.selected_modification, "No default modification"
    assert component.max_modification_grade == 0, "Max grade is zero"


def test_configure(monkeypatch):
    """
    .
    """
    # pylint: disable=unused-argument,protected-access
    @counter_wrapper
    def set_modification(self):
        """
        .
        """

    @counter_wrapper
    def set_effect(self):
        """
        .
        """

    monkeypatch.setattr(BaseComponent, "_select_modification", set_modification)
    monkeypatch.setattr(BaseComponent, "_select_effect", set_effect)

    component = BaseComponent()
    assert (
        not set_modification.counter
    ), "Set modification not called if no modifications on component"
    assert not set_effect.counter, "Set effect not called if no effects on component"

    BaseComponent._modifications = ["something"]
    BaseComponent._effects = ["something else"]

    component = BaseComponent()

    assert component.modifications == ["something"], "Injected modifications returned"
    assert component.effects == ["something else"], "Injected effects returned"

    assert (
        set_modification.counter
    ), "Set modification called if modifications on component"
    assert set_effect.counter, "Set effect called if effects on component"


def test_select_modification(monkeypatch):
    """
    .
    """
    # pylint: disable=protected-access,unused-argument
    BaseComponent._modifications = ["option1", "option2"]
    BaseComponent._default_modification = "option2"
    monkeypatch.setattr(BaseComponent, "configure", lambda self: None)

    @counter_wrapper
    def make_choice(name: str, options: list, default):
        """
        .
        """
        assert name == "modification", "Name passed to inputs"
        assert options == [None, "option1", "option2"], "None added to options"
        assert default == (
            "option2" if make_choice.counter == 1 else None
        ), "Default passed in"

        return default

    @counter_wrapper
    def get_grade(default: int):
        """
        .
        """
        return 3

    monkeypatch.setattr(inputs, "make_choice", make_choice)
    monkeypatch.setattr(inputs, "get_grade", get_grade)

    component = BaseComponent()
    component._select_modification()
    assert make_choice.counter == 1, "Make choice called"
    assert component.selected_modification == "option2", "Modification selected"
    assert get_grade.counter == 1, "Get grade called"
    assert component.max_modification_grade == 3, "Max grade set"

    BaseComponent._default_modification = None
    component = BaseComponent()
    component._select_modification()
    assert make_choice.counter == 2, "Make choice called"
    assert component.selected_modification is None, "No modification selected"
    assert get_grade.counter == 1, "Get grade was NOT called again"
    assert component.max_modification_grade == 0, "No max grade set"


def test_select_effect(monkeypatch):
    """
    .
    """
    # pylint: disable=protected-access,unused-argument
    BaseComponent._effects = ["effect1", "effect2"]
    BaseComponent._default_effect = "effect2"
    monkeypatch.setattr(BaseComponent, "configure", lambda self: None)

    @counter_wrapper
    def make_choice(name: str, options: list, default):
        """
        .
        """
        assert name == "effect", "Name passed to inputs"
        assert options == [None, "effect1", "effect2"], "None added to options"
        assert default == "effect2", "Default effect passed in"

        return default

    monkeypatch.setattr(inputs, "make_choice", make_choice)

    component = BaseComponent()
    component._select_effect()
    assert make_choice.counter == 1, "Make choice called"
    assert component.selected_effect == "effect2", "Modification selected"


def test_to_shopping_list(monkeypatch):
    """
    .
    """
    monkeypatch.setattr(BaseComponent, "configure", lambda self: None)

    plant = PowerPlant()
    plant.selected_modification = Modification.ARMOURED
    plant.max_modification_grade = 4
    plant.selected_effect = ExperimentalEffect.MONSTERED
    shopping_list = plant.to_shopping_list("cmdr", {i: i for i in range(1, 6)})
    assert shopping_list == (
        '"cmdr:G1 [Power Plant] Armoured",'
        + '"cmdr:G2 [Power Plant] Armoured",' * 2
        + '"cmdr:G3 [Power Plant] Armoured",' * 3
        + '"cmdr:G4 [Power Plant] Armoured",' * 4
        + '"cmdr:G [Power Plant] Monstered"'
    ), "Shopping list for modification and effect correct"

    plant.selected_effect = None
    shopping_list = plant.to_shopping_list("cmdr", {i: i for i in range(1, 6)})
    assert shopping_list == (
        '"cmdr:G1 [Power Plant] Armoured",'
        + '"cmdr:G2 [Power Plant] Armoured",' * 2
        + '"cmdr:G3 [Power Plant] Armoured",' * 3
        + '"cmdr:G4 [Power Plant] Armoured",' * 4
    ).rstrip(","), "Shopping list for only modification correct"

    plant.selected_effect = ExperimentalEffect.MONSTERED
    plant.selected_modification = None
    plant.max_modification_grade = 0
    shopping_list = plant.to_shopping_list("cmdr", {i: i for i in range(1, 6)})
    assert shopping_list == (
        '"cmdr:G [Power Plant] Monstered"'
    ), "Shopping list for only effect correct"


def test_to_str(monkeypatch):
    """
    .
    """
    monkeypatch.setattr(BaseComponent, "configure", lambda self: None)
    plant = PowerPlant()
    assert str(plant) == "Power Plant", "Basic name returned"

    plant.selected_modification = Modification.ARMOURED
    plant.max_modification_grade = 4
    assert str(plant) == "Power Plant | G4 Armoured", "Name and modification returned"

    plant.selected_effect = ExperimentalEffect.MONSTERED
    assert (
        str(plant) == "Power Plant | G4 Armoured [Monstered]"
    ), "Name, modification, and effect returned"

    plant.selected_modification = None
    assert str(plant) == "Power Plant | [Monstered]", "Name and effect returned"
