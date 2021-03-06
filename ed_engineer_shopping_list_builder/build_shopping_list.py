#!/usr/bin/env python3
"""
Builds a shopping list for ED engineer
"""
from os import path
import sys
from typing import Dict

from ed_engineer_shopping_list_builder import inputs
from ed_engineer_shopping_list_builder.ship import Ship
from ed_engineer_shopping_list_builder.ship_components import ALL_COMPONENTS

LAST_MOD_ADDED = None


def make_shopping_list():
    """
    Makes the actual shopping list
    """
    cmdr = get_cmdr(sys.argv)
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
            if save_shopping_list(ship, cmdr, count_per_grade):
                break


def get_cmdr(argv) -> str:
    """
    Sets commander
    """
    return argv[1] if len(argv) > 1 else inputs.single_prompt("CMDR name")


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
    global LAST_MOD_ADDED
    component_map = {component.name: component for component in ALL_COMPONENTS}
    options = list(component_map.keys())
    if "" in options:
        options.remove("")
    options.sort(
        key=lambda option: str(component_map[option].component_classification) + option
    )

    component = inputs.make_choice("component", [None] + options, LAST_MOD_ADDED)

    if component:
        LAST_MOD_ADDED = component
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
    options.sort(
        key=lambda option: str(component_map[option].component_classification) + option
    )

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
    options.sort(
        key=lambda option: str(component_map[option].component_classification) + option
    )

    component = inputs.make_choice("component", [None] + options, None)

    if component:
        ship.remove_component(component_map[component])


def summarize_ship(ship: Ship):
    """
    .
    """
    print(ship.summarize())


def save_shopping_list(
    ship: Ship, cmdr_name: str, grade_counts: Dict[int, int]
) -> bool:
    """
    Save the ship configuration to an output
    Returns True if saved and should exit, False otherwise
    """
    output_file = inputs.single_prompt(
        "Output ship to file? (leave BLANK to return to editing) ",
        default="ship.shoppingList",
    )

    if not output_file:
        return False

    if path.isfile(output_file):
        if not inputs.check_confirmation("Overwrite file?"):
            return False

    shopping_list = ship.to_shopping_list(cmdr_name, grade_counts)
    save_data_to_file(output_file, shopping_list)

    return True


def save_data_to_file(output_file: str, shopping_list: str):
    """
    Saves data to a file
    """
    output_handle = open(output_file, "w")
    output_handle.write(shopping_list + "\n")
    output_handle.close()


if __name__ == "__main__":
    make_shopping_list()
