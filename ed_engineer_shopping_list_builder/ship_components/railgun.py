"""
Rail Gun
"""
from ed_engineer_shopping_list_builder.ship_components.base_component import (
    BaseComponent,
)
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect


class RailGun(BaseComponent):
    """
    Rail Gun
    """

    component_classification = Classification.HARDPOINT
    name = "Rail Gun"

    _modifications = [
        Modification.HIGH_CAPACITY_MAGAZINE,
        Modification.LIGHTWEIGHT_MOUNT,
        Modification.LONG_RANGE_WEAPON,
        Modification.SHORT_RANGE_BLASTER,
        Modification.STURDY_MOUNT,
    ]
    _effects = [
        ExperimentalEffect.DOUBLE_BRACED,
        ExperimentalEffect.FEEDBACK_CASCADE,
        ExperimentalEffect.FLOW_CONTROL,
        ExperimentalEffect.MULTI_SERVOS,
        ExperimentalEffect.OVERSIZED,
        ExperimentalEffect.PLASMA_SLUG,
        ExperimentalEffect.STRIPPED_DOWN,
        ExperimentalEffect.SUPER_PENETRATOR,
    ]

    _default_modification = Modification.LONG_RANGE_WEAPON
    _default_effect = ExperimentalEffect.SUPER_PENETRATOR
