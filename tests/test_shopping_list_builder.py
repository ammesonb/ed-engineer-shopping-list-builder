"""
Tests the actual shopping list builder
"""
from os import path

from ed_engineer_shopping_list_builder import build_shopping_list, inputs, ship
from ed_engineer_shopping_list_builder.utils import counter_wrapper
from ed_engineer_shopping_list_builder.ship_components import PowerPlant
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)


def test_get_cmdr(monkeypatch):
    """
    .
    """
    # pylint: disable=unused-argument
    monkeypatch.setattr(inputs, "single_prompt", lambda *args, **kwargs: "cmdr")

    assert (
        build_shopping_list.get_cmdr(["script", "name"]) == "name"
    ), "CLI commander used"
    assert build_shopping_list.get_cmdr(["script"]) == "cmdr", "Prompted commander used"


def test_get_grade_counts(monkeypatch):
    """
    .
    """
    # pylint: disable=unused-argument
    monkeypatch.setattr(inputs, "get_quantity", lambda prompt, default: default + 1)
    assert build_shopping_list.get_grade_counts() == {
        1: 3,
        2: 3,
        3: 5,
        4: 6,
        5: 11,
    }, "Expected grade counts returned"


def test_add_component(monkeypatch):
    """
    .
    """
    # pylint: disable=unused-argument
    @counter_wrapper
    def make_choice(prompt: str, options: list, default):
        """
        .
        """
        assert None in options, "None added to options"
        return "Power Plant" if make_choice.counter == 1 else None

    @counter_wrapper
    def add_component(self, component):
        """
        .
        """

    monkeypatch.setattr(inputs, "make_choice", make_choice)
    monkeypatch.setattr(ship.Ship, "add_component", add_component)
    monkeypatch.setattr(BaseComponent, "configure", lambda self: None)

    build_shopping_list.add_component(ship.Ship())
    assert make_choice.counter == 1, "Component selected"
    assert add_component.counter == 1, "Component added"

    build_shopping_list.add_component(ship.Ship())
    assert make_choice.counter == 2, "Component selected again"
    assert add_component.counter == 1, "Component NOT added if None selected"


def test_update_component(monkeypatch):
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

    @counter_wrapper
    def make_choice(prompt: str, options: list, default):
        """
        .
        """
        assert None in options, "None added to options"
        return "Power Plant" if make_choice.counter == 1 else None

    monkeypatch.setattr(inputs, "make_choice", make_choice)
    configured_ship = ship.Ship()
    configured_ship.add_component(PowerPlant())

    build_shopping_list.update_component(configured_ship)
    assert make_choice.counter == 1, "Component selected"
    assert configure.counter == 2, "Component configured and re-configured"

    build_shopping_list.update_component(configured_ship)
    assert make_choice.counter == 2, "Component selected again"
    assert configure.counter == 2, "Component NOT re-configured if None selected"


def test_remove_component(monkeypatch):
    """
    .
    """

    # pylint: disable=unused-argument
    @counter_wrapper
    def make_choice(prompt: str, options: list, default):
        """
        .
        """
        assert None in options, "None added to options"
        return None if make_choice.counter == 1 else "Power Plant"

    monkeypatch.setattr(BaseComponent, "configure", lambda self: None)
    monkeypatch.setattr(inputs, "make_choice", make_choice)
    configured_ship = ship.Ship()
    configured_ship.add_component(PowerPlant())

    assert len(configured_ship.component_list) == 1, "One component on ship"

    build_shopping_list.remove_component(configured_ship)
    assert make_choice.counter == 1, "Component selected"
    assert len(configured_ship.component_list) == 1, "Component not removed"

    build_shopping_list.remove_component(configured_ship)
    assert make_choice.counter == 2, "Component selected again"
    assert len(configured_ship.component_list) == 0, "Component removed"


def test_summarize(monkeypatch, capsys):
    """
    .
    """
    # pylint: disable=unused-argument
    monkeypatch.setattr(ship.Ship, "summarize", lambda self: "Ship")
    build_shopping_list.summarize_ship(ship.Ship())
    printed = capsys.readouterr()
    assert printed.out == "Ship\n", "Summary prints"


def test_save_shopping_list(monkeypatch):
    """
    .
    """
    # pylint: disable=unused-argument
    monkeypatch.setattr(inputs, "single_prompt", lambda *args, **kwargs: "")

    assert not build_shopping_list.save_shopping_list(
        ship.Ship(), "cmdr", {}
    ), "Shopping list doesn't save if no file given"

    monkeypatch.setattr(inputs, "single_prompt", lambda *args, **kwargs: "file")
    monkeypatch.setattr(path, "isfile", lambda file_path: True)
    monkeypatch.setattr(inputs, "check_confirmation", lambda *args, **kwargs: False)
    assert not build_shopping_list.save_shopping_list(
        ship.Ship(), "cmdr", {}
    ), "Shopping list doesn't save if user doesn't overwrite existing file"

    @counter_wrapper
    def output_file(*args, **kwargs):
        """
        .
        """

    monkeypatch.setattr(build_shopping_list, "save_data_to_file", output_file)
    monkeypatch.setattr(inputs, "check_confirmation", lambda *args, **kwargs: True)

    assert build_shopping_list.save_shopping_list(
        ship.Ship(), "cmdr", {}
    ), "Shopping list written to file if overwritten"
    assert output_file.counter == 1, "File saved"

    monkeypatch.setattr(inputs, "check_confirmation", lambda *args, **kwargs: True)
    monkeypatch.setattr(path, "isfile", lambda file_path: False)

    assert build_shopping_list.save_shopping_list(
        ship.Ship(), "cmdr", {}
    ), "Shopping list written to file if new file"
    assert output_file.counter == 2, "File saved"


def test_make_shopping_list(monkeypatch):
    """
    .
    """

    # pylint: disable=unused-argument
    @counter_wrapper
    def get_cmdr(argv):
        """
        .
        """
        return "cmdr"

    @counter_wrapper
    def get_grade_counts():
        """
        .
        """
        return {}

    @counter_wrapper
    def add(outfitted_ship):
        """
        .
        """

    @counter_wrapper
    def update(outfitted_ship):
        """
        .
        """

    @counter_wrapper
    def remove(outfitted_ship):
        """
        .
        """

    @counter_wrapper
    def review(outfitted_ship):
        """
        .
        """

    @counter_wrapper
    def summarize(outfitted_ship):
        """
        .
        """

    @counter_wrapper
    def save(outfitted_ship, cmdr, grade_counts):
        """
        .
        """
        return save.counter == 2

    @counter_wrapper
    def get_action():
        """
        .
        """
        return {1: "Add", 2: "Update", 3: "Remove", 4: "Review"}.get(
            get_action.counter, "Done"
        )

    monkeypatch.setattr(build_shopping_list, "add_component", add)
    monkeypatch.setattr(build_shopping_list, "get_cmdr", get_cmdr)
    monkeypatch.setattr(build_shopping_list, "get_grade_counts", get_grade_counts)
    monkeypatch.setattr(build_shopping_list, "update_component", update)
    monkeypatch.setattr(build_shopping_list, "remove_component", remove)
    monkeypatch.setattr(build_shopping_list, "summarize_ship", summarize)
    monkeypatch.setattr(build_shopping_list, "save_shopping_list", save)
    monkeypatch.setattr(inputs, "get_action", get_action)

    build_shopping_list.make_shopping_list()
    assert get_cmdr.counter == 1, "Requested commander name"
    assert get_grade_counts.counter == 1, "Set grade counts"
    assert add.counter == 1, "Component added"
    assert update.counter == 1, "Component updated"
    assert remove.counter == 1, "Component removed"
    assert (
        summarize.counter == 3
    ), "Component summarized, once explicitly twice with save"
    assert save.counter == 2, "Ship saved (twice, since failed first time)"
