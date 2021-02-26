"""
A component which can only be shielded
True for many optional internal modules
"""
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)


class ShieldedComponent(BaseComponent):
    """
    A generic shielded component, used for most optional internal modules
    """

    _modifications = [Modification.SHIELDED]
    component_classification = Classification.OPTIONAL_INTERNAL

    _default_modification = Modification.SHIELDED
