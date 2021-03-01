"""
Various utilities
"""
import functools
from typing import List, Dict, Callable

from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)


def counter_wrapper(func):
    """
    Adds a "counter" variable to the function, incrementing each time it is called
    """

    @functools.wraps(func)  # pragma: no mutate
    def execute(*args, **kwargs):
        """
        Adds a "counter" variable to the function, incrementing each time it is called
        """
        execute.counter += 1
        return func(*args, **kwargs)

    execute.counter = 0

    return execute


def organize_components_by_classification(
    components: List[BaseComponent],
) -> Dict[Classification, List[BaseComponent]]:
    """
    Takes a list of components, and returns a mapping by classification
    """
    components_by_type = {}

    for component in components:
        if component.component_classification not in components_by_type:
            components_by_type[component.component_classification] = []

        components_by_type[component.component_classification].append(component)

    return components_by_type


def get_component_summary_by_classification(
    components_by_classification: Dict[Classification, List[BaseComponent]],
    component_serialization: Callable[[BaseComponent], str],
) -> str:
    """
    Organizes a set of components by classification,
    using a custom serialization function
    """
    summary = ""

    for classification in [
        Classification.CORE,
        Classification.HARDPOINT,
        Classification.OPTIONAL_INTERNAL,
        Classification.UTILITY,
    ]:
        summary += "-" * 40 + "\n"
        summary += str(classification).upper() + "\n"
        summary += "-" * 40 + "\n\n"

        components = components_by_classification.get(classification, [])
        components.sort(key=lambda component: component.name)

        for component in components:
            summary += component_serialization(component) + "\n"

        summary += "\n\n"

    return summary
