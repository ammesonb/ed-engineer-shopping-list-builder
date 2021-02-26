"""
Sensors
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect


class Sensors(BaseComponent):
    """
    Sensors
    """

    name = "Sensors"
    component_classification = Classification.CORE

    _modifications = [
        Modification.LIGHTWEIGHT,
        Modification.LONG_RANGE_SCANNER,
        Modification.WIDE_ANGLE_SCANNER,
    ]

    _default_modification = Modification.LONG_RANGE_SCANNER
