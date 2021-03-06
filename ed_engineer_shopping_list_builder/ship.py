"""
Defines a ship
"""
from typing import List, Dict

from ed_engineer_shopping_list_builder import utils
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)


def is_component_unique(component: BaseComponent) -> bool:
    """
    Can there only be one of this component on the ship
    """
    return (
        component.is_singleton
        or component.component_classification == Classification.CORE
    )


class Ship:
    """
    A representation of an elite dangerous ship
    """

    def __init__(self):
        self.outfitted = {}

    def add_component(self, component: BaseComponent):
        """
        Adds a component to this ship
        """
        if is_component_unique(component):
            self._set_single_component(component)
        else:
            self._add_optional_component(component)

    def _set_single_component(self, component: BaseComponent):
        """
        Set a singleton component on the ship, e.g. thrusters or power plant
        """
        self.outfitted[component.name] = component

    def _add_optional_component(self, component: BaseComponent):
        """
        Adds an optional component, of which there may be multiple
        """
        if component.name not in self.outfitted:
            self.outfitted[component.name] = []

        self.outfitted[component.name].append(component)

    def remove_component(self, component: BaseComponent):
        """
        Removes a component from the ship
        """
        if is_component_unique(component):
            del self.outfitted[component.name]
        else:
            self.outfitted[component.name].remove(component)

    @property
    def component_list(self) -> List[BaseComponent]:
        """
        Returns a list of all components
        """
        outfitted = list(self.outfitted.keys())
        outfitted.sort()
        components = []
        for component_name in outfitted:
            component = self.outfitted[component_name]
            if isinstance(component, list):
                components.extend(component)
            else:
                components.append(component)

        return components

    def summarize(self) -> str:
        """
        Makes a string summary of the ship's components
        """
        components_by_type = utils.organize_components_by_classification(
            self.component_list
        )
        return utils.get_component_summary_by_classification(components_by_type, str)

    def to_shopping_list(self, cmdr_name: str, grade_counts: Dict[int, int]) -> str:
        """
        Format the components on the ship to a shopping list
        """
        shopping_list = "["
        for component in self.component_list:
            shopping_list += component.to_shopping_list(cmdr_name, grade_counts) + ","

        shopping_list = shopping_list.rstrip(",") + "]"

        return shopping_list
