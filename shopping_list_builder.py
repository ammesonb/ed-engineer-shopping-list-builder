#!/usr/bin/env python3
from dataclasses import dataclass
from os import path
import sys
from typing import List, Dict, Any, Optional
import yaml


@dataclass
class Component:
    """
    An engineerable component
    """

    name: str
    modification: str
    max_modification_grade: int
    effect: str
    quantity: int


class DuplicatedList:
    """
    A list that adds multiple things at one
    """

    def __init__(self, quantity: int):
        self._quantity = quantity
        self.items = []

    def append(self, item: Any, times: int = 1):
        """
        Appends an item to this list

        In some cases, we will want to add say, 2 sets of G5 items, for a total of 20
        """
        for _ in range(self._quantity):
            for time in range(0, times):
                self.items.append(item)


def _load_yaml(file_path) -> List[str]:
    """
    Loads a yaml file, which return lists
    """
    with open(file_path) as file_handle:
        return yaml.load(file_handle, Loader=yaml.FullLoader)


def make_shopping_list():
    """
    Makes the actual shopping list
    """
    components = _load_yaml("components.yaml")
    modifications = _load_yaml("modifications.yaml")
    effects = _load_yaml("effects.yaml")
    cmdr = get_cmdr()
    count_per_grade = get_grade_counts()

    shopping_list = []

    overwrite = False
    if path.exists("output.shoppingList"):
        overwrite = input("Overwrite? (y/N) ") == "y"
    else:
        overwrite = True

    if overwrite:
        handle = open("output.shoppingList", "w")
        handle.write("[")
        handle.flush()
        handle.close()

    output_handle = open("output.shoppingList", "a")
    first_component = True
    while True:
        component = get_component(components, modifications, effects)
        if not component:
            break

        for entry in format_component_to_strings(cmdr, component, count_per_grade):
            if not first_component or not overwrite:
                output_handle.write(",")
            output_handle.write(f'"{entry}"')
            output_handle.flush()
            first_component = False

    output_handle.write("]\n")
    output_handle.close()


def get_cmdr() -> str:
    """
    Sets commander
    """
    return sys.argv[1] if len(sys.argv) > 1 else input("CMDR name: ")


def get_grade_counts() -> Dict[int, int]:
    """
    Sets grade count
    """
    count_per_grade = {}
    for i in range(1, 6):
        if len(sys.argv) > 1 + i:
            count = int(sys.argv[i + 1])
        else:
            count = input(f"How many rolls on average for grade {i}? ")
        count_per_grade[i] = int(count)

    return count_per_grade


def get_component(
    components: List[str], modifications: List[str], effects: List[str]
) -> Optional[Component]:
    """
    Prompts user for a component
    """
    component_name = ""
    while component_name not in components:
        component_name = input("Component name: ")
        if not component_name:
            if input("Are you sure? (y/N) ") == "y":
                return None

    modification = "invalid"
    while modification and modification not in modifications:
        modification = input("Modification: ")
        if not modification:
            break

    modification_grade = "0"
    while modification and (
        (not modification_grade.isnumeric())
        or int(modification_grade) < 1
        or int(modification_grade) > 5
    ):
        modification_grade = input("Max modification grade: ")

    modification_grade = int(modification_grade)

    effect_name = "invalid"
    while effect_name and effect_name not in effects:
        effect_name = input("Effect: ")

    quantity = input("Quantity (default 1): ") or "1"
    while not quantity.isnumeric():
        quantity = input("Quantity (default 1): ") or "1"

    return Component(
        component_name, modification, modification_grade, effect_name, int(quantity)
    )


def format_component_to_strings(
    commander_name: str, component: Component, grade_counts: Dict[int, int],
) -> List[str]:
    """
    Formats a component configuration into a string
    """
    command_base = f"{commander_name}:G{{grade}} [{component.name}] {{modification}}"
    shopping_list_entries = DuplicatedList(component.quantity)

    for grade in range(1, component.max_modification_grade + 1):
        shopping_list_entries.append(
            command_base.format(grade=grade, modification=component.modification),
            grade_counts[grade],
        )

    if component.effect:
        shopping_list_entries.append(
            command_base.format(grade="", modification=component.effect)
        )

    return shopping_list_entries.items


if __name__ == "__main__":
    make_shopping_list()
