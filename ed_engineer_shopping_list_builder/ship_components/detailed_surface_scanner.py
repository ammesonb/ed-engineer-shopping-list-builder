"""
Detailed Surface Scanner
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification


class DetailedSurfaceScanner(BaseComponent):
    """
    Detailed Surface Scanner
    """

    name = "Surface Scanner"
    is_singleton = True
    component_classification = Classification.OPTIONAL_INTERNAL

    _modifications = [Modification.EXPANDED_PROBE_SCANNING_RADIUS]

    _default_modification = Modification.EXPANDED_PROBE_SCANNING_RADIUS
