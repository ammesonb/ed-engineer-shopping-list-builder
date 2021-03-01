"""
Tests for the input getter
"""
import inquirer

from ed_engineer_shopping_list_builder import inputs
from ed_engineer_shopping_list_builder.utils import counter_wrapper


def test_make_choice(monkeypatch):
    """
    .
    """
    # pylint: disable=unused-argument
    @counter_wrapper
    def prompt(questions, theme):
        """
        .
        """
        return {"q": "answer"}

    monkeypatch.setattr(inquirer, "prompt", prompt)
    assert inputs.make_choice("q", ["a"], "a") == "answer", "Expected answer returned"
    assert prompt.counter == 1, "Prompt called"


def test_make_choices(monkeypatch):
    """
    .
    """
    # pylint: disable=unused-argument
    @counter_wrapper
    def prompt(questions, theme):
        """
        .
        """
        return {"q": "answer"}

    monkeypatch.setattr(inquirer, "prompt", prompt)
    assert inputs.make_choices("q", ["a"]) == "answer", "Expected answer returned"
    assert prompt.counter == 1, "Prompt called"


def test_get_grade(monkeypatch):
    """
    .
    """
    # pylint: disable=unused-argument
    monkeypatch.setattr(inputs, "single_prompt", lambda *args, **kwargs: "4")
    assert inputs.get_grade(3) == 4, "Prompt value returned as int"


def test_get_quantity(monkeypatch):
    """
    .
    """
    # pylint: disable=unused-argument
    monkeypatch.setattr(inputs, "single_prompt", lambda *args, **kwargs: "3")
    assert inputs.get_quantity(4) == 3, "Prompt value returned as int"


def test_single_prompt(monkeypatch):
    """
    .
    """
    valid = lambda _, x: x == "foo"

    # pylint: disable=unused-argument,protected-access
    @counter_wrapper
    def prompt(questions: list, theme):
        """
        .
        """
        assert questions[0].message == "prompt", "Message correct"
        assert questions[0].default == "default", "Default passed through"
        assert questions[0]._validate == valid, "Validation correct"

        return {"question": "value"}

    monkeypatch.setattr(inquirer, "prompt", prompt)
    assert (
        inputs.single_prompt("prompt", valid, "default") == "value"
    ), "Answer returned"
    assert prompt.counter == 1, "Prompt called"


def test_get_action(monkeypatch):
    """
    .
    """
    # pylint: disable=unused-argument
    monkeypatch.setattr(inputs, "make_choice", lambda *args, **kwargs: "add")
    assert inputs.get_action() == "add", "Action returned"


def test_check_confirmation(monkeypatch):
    """
    .
    """

    # pylint: disable=unused-argument
    @counter_wrapper
    def prompt(questions: list, theme):
        """
        .
        """
        assert questions[0].message == "prompt", "Message correct"
        assert questions[0].default, "Default passed through"

        return {"check": False}

    monkeypatch.setattr(inquirer, "prompt", prompt)
    assert not inputs.check_confirmation("prompt", True), "Answer returned"
    assert prompt.counter == 1, "Prompt called"
