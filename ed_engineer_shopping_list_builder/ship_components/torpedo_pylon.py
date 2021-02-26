"""
Torpedo Pylon
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect


class TorpedoPylon(BaseComponent):
    """
    Torpedo Pylon
    """

    component_classification = Classification.HARDPOINT
    name = "Torpedo Pylon"

    _modifications = [
        Modification.LIGHTWEIGHT_MOUNT,
        Modification.STURDY_MOUNT,
    ]

    _effects = [
        ExperimentalEffect.MASS_LOCK_MUNITION,
        ExperimentalEffect.PENETRATOR_PAYLOAD,
        ExperimentalEffect.REVERBERATING_CASCADE,
        ExperimentalEffect.FLOW_CONTROL,
        ExperimentalEffect.OVERSIZED,
        ExperimentalEffect.STRIPPED_DOWN,
        ExperimentalEffect.DOUBLE_BRACED,
    ]

    _default_effect = ExperimentalEffect.PENETRATOR_MUNITIONS
