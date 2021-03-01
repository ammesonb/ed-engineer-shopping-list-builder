"""
Represents an engineer
"""
from typing import Dict

from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)


# pylint: disable=too-few-public-methods
class Engineer:
    """
    Base engineer
    """

    name = ""
    max_component_upgrade: Dict[BaseComponent, int]
