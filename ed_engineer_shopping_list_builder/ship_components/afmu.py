"""
AFMU
"""
from ed_engineer_shopping_list_builder.modification import Modification
from ed_engineer_shopping_list_builder.ship_components.shielded_component import (
    ShieldedComponent,
)


class AFMU(ShieldedComponent):
    """
    Auto Field Maintenance Unit
    """

    _default_modification = Modification.SHIELDED

    name = "AFMU"
