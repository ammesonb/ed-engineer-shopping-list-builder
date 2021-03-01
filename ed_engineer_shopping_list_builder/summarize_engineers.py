"""
Prints a summary of available upgrades from a given set of engineers available
"""
from typing import List, Dict

from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.engineers import ALL_ENGINEERS
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder import inputs, utils


def summarize_engineers():
    """
    Performs the engineer summary
    """
    engineers = get_available_engineers()
    optimal_engineers = simplify_engineer_components(engineers)
    print_component_summary(optimal_engineers)


def get_available_engineers() -> List[Engineer]:
    """
    Gets the user's available engineers
    """
    engineer_map = {engineer.name: engineer for engineer in ALL_ENGINEERS}
    available_engineers = inputs.make_choices("engineer", list(engineer_map.keys()))
    return [engineer_map[engineer] for engineer in available_engineers]


def simplify_engineer_components(
    engineers: List[Engineer],
) -> Dict[BaseComponent, Engineer]:
    """
    Given a list of engineers, for each component find
    """
    best_component_engineer = {}  # type: Dict[BaseComponent, Engineer]
    # Check each components available for each engineer
    for engineer in engineers:
        for component, grade in engineer.max_component_upgrade.items():
            # If we haven't seen this component yet, or
            # this engineer can upgrade the component further than the best so far
            if (
                component not in best_component_engineer
                or grade
                > best_component_engineer[component].max_component_upgrade[component]
            ):
                best_component_engineer[component] = engineer

    return best_component_engineer


def print_component_summary(components_with_engineers: Dict[BaseComponent, Engineer]):
    """
    .
    """
    components_by_classification = utils.organize_components_by_classification(
        list(components_with_engineers.keys())
    )
    print(
        utils.get_component_summary_by_classification(
            components_by_classification,
            lambda component: (
                "G"
                + str(
                    components_with_engineers[component].max_component_upgrade[
                        component
                    ]
                )
                + f" {component.name} [{components_with_engineers[component].name}]"
            ),
        )
    )


if __name__ == "__main__":
    summarize_engineers()
