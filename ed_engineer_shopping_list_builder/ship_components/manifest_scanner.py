"""
Manifest Scanner
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect


class ManifestScanner(BaseComponent):
    """
    Manifest Scanner
    """

    name = "Manifest Scanner"
    component_classification = Classification.UTILITY
    is_singleton = True

    _modifications = [
        Modification.FAST_SCANNER,
        Modification.LIGHTWEIGHT,
        Modification.LONG_RANGE_SCANNER,
        Modification.REINFORCED,
        Modification.SHIELDED,
        Modification.WIDE_ANGLE_SCANNER,
    ]

    _default_modification = Modification.FAST_SCANNER
