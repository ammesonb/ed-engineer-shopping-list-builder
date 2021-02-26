"""
Helpful functions for inputs
"""
from typing import List, Callable, Any, Optional

import inquirer
from inquirer.themes import GreenPassion


def make_choice(kind: str, options: List[str], default: str):
    """
    .
    """
    return inquirer.prompt(
        [inquirer.List(kind, f"Select {kind}", options, default, carousel=True)],
        theme=GreenPassion(),
    )[kind]


def get_grade(default: int = None) -> int:
    """
    Get the max modification grade
    """
    return int(
        single_prompt(
            "Max modification grade",
            lambda _, x: x.isnumeric() and int(x) > 0 and int(x) < 6,
            default,
        )
    )


def get_quantity(prompt: str = "How many?", default: int = 0) -> int:
    """
    Get quantity
    """
    return int(
        single_prompt(
            prompt,
            lambda _, x: x.isnumeric() and int(x) > 0,
            default if default else "",
        )
    )


def single_prompt(
    prompt: str,
    validation: Optional[Callable] = lambda _, x: True,
    default: Optional[Any] = None,
) -> Any:
    """
    Prompt user for an answer to a question
    """
    return inquirer.prompt(
        [inquirer.Text("question", prompt, default, validate=validation)],
        theme=GreenPassion(),
    )["question"]


def get_action() -> str:
    """
    Get the desired action
    """
    return make_choice("action", ["Add", "Update", "Remove", "Review", "Done"], "Add")


def check_confirmation(prompt: str, default: bool = False) -> bool:
    """
    Check confirmation of something
    """
    return inquirer.prompt(
        [inquirer.Confirm("check", message=prompt, default=default)],
        theme=GreenPassion(),
    )["check"]
