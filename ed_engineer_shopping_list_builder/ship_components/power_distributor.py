"""
Power Distributor
"""
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect
from ed_engineer_shopping_list_builder.ship_components.shielded_component import (
    BaseComponent,
)


class PowerDistributor(BaseComponent):
    """
    Power Distributor
    """

    name = "Power Distributor"
    component_classification = Classification.CORE

    _modifications = [
        Modification.CHARGE_ENHANCED,
        Modification.ENGINE_FOCUSED,
        Modification.HIGH_CHARGE_CAPACITY,
        Modification.SHIELDED,
        Modification.SYSTEM_FOCUSED,
        Modification.WEAPON_FOCUSED,
    ]

    _effects = [
        ExperimentalEffect.CLUSTER_CAPACITOR,
        ExperimentalEffect.DOUBLE_BRACED,
        ExperimentalEffect.FLOW_CONTROL,
        ExperimentalEffect.STRIPPED_DOWN,
        ExperimentalEffect.SUPER_CONDUITS,
    ]

    _default_modification = Modification.CHARGE_ENHANCED
    _default_effect = ExperimentalEffect.SUPER_CONDUITS
