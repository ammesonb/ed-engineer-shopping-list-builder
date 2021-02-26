#!/usr/bin/env python3
from dataclasses import dataclass
from os import path
import sys
from typing import List, Dict, Any, Optional

from ed_engineer_shopping_list_builder import inputs
from ed_engineer_shopping_list_builder.ship import Ship, ALL_COMPONENTS
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)


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


def make_shopping_list():
    """
    Makes the actual shopping list
    """
    cmdr = get_cmdr()
    count_per_grade = get_grade_counts()

    ship = Ship()

    while True:
        selected_action = inputs.get_action()
        print(selected_action)
        if selected_action == "Add":
            add_component(ship)
        elif selected_action == "Update":
            update_component(ship)
        elif selected_action == "Remove":
            remove_component(ship)
        elif selected_action == "Review":
            summarize_ship(ship)
        elif selected_action == "Done":
            summarize_ship(ship)
            save_shopping_list(ship, cmdr, count_per_grade)


def get_cmdr() -> str:
    """
    Sets commander
    """
    return sys.argv[1] if len(sys.argv) > 1 else input("CMDR name: ")


def get_grade_counts() -> Dict[int, int]:
    """
    Sets grade count
    """
    defaults = [2, 2, 4, 5, 10]
    count_per_grade = {}
    for i in range(1, 6):
        count_per_grade[i] = inputs.get_quantity(
            f"How many rolls per average for grade {i}?", defaults[i - 1]
        )

    return count_per_grade


def add_component(ship: Ship):
    """
    Adds a component to the ship
    """
    component_map = {component.name: component for component in ALL_COMPONENTS}
    options = list(component_map.keys())
    if "" in options:
        options.remove("")
    options.sort()

    component = inputs.make_choice("component", [None] + options, None)

    if component:
        ship.add_component(component_map[component]())


def update_component(ship: Ship):
    """
    .
    """
    # NOTE: this will collapse multiple components with same configurations to one entry
    # NOTE: only one instance will be updated, so this is okay
    component_map = {str(component): component for component in ship.component_list}
    options = list(component_map.keys())
    if "" in options:
        options.remove("")
    options.sort()

    component = inputs.make_choice("component", [None] + options, None)

    if component:
        # Since working on references with state, don't need to update the ship
        component_map[component].configure()


def remove_component(ship: Ship):
    """
    Remove a component from the ship
    """
    # NOTE: this will collapse multiple components with same configurations to one entry
    # NOTE: only one instance will be removed, so this is okay
    component_map = {str(component): component for component in ship.component_list}
    options = list(component_map.keys())
    if "" in options:
        options.remove("")
    options.sort()

    component = inputs.make_choice("component", [None] + options, None)

    if component:
        ship.remove_component(component_map[component])


def summarize_ship(ship: Ship):
    """
    .
    """
    print(ship.summarize())


def save_shopping_list(ship: Ship, cmdr_name: str, grade_counts: Dict[int, int]):
    """
    Save the ship configuration to an output
    """
    output_file = inputs.single_prompt(
        "Output ship to file? (leave BLANK to return to editing) ",
        default="ship.shoppingList",
    )

    if not output_file:
        return

    if path.isfile(output_file):
        if not inputs.check_confirmation("Overwrite file?"):
            return

    shopping_list = ship.to_shopping_list(cmdr_name, grade_counts)
    output_handle = open(output_file, "w")
    output_handle.write(shopping_list + "\n")
    output_handle.close()
    exit(0)


def format_component_to_strings(
    commander_name: str,
    component: BaseComponent,
    quantity: int,
    grade_counts: Dict[int, int],
) -> List[str]:
    """
    Formats a component configuration into a string
    """
    command_base = f"{commander_name}:G{{grade}} [{component.name}] {{modification}}"
    shopping_list_entries = DuplicatedList(quantity)

    for grade in range(1, component.max_modification_grade + 1):
        shopping_list_entries.append(
            command_base.format(
                grade=grade, modification=component.selected_modification
            ),
            grade_counts[grade],
        )

    if component.selected_effect:
        shopping_list_entries.append(
            command_base.format(grade="", modification=component.effect)
        )

    return shopping_list_entries.items


if __name__ == "__main__":
    make_shopping_list()
