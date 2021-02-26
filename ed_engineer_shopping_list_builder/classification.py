"""
Component classification
"""
from ed_engineer_shopping_list_builder.printable_enum import PrintableEnum


# pylint: disable=too-few-public-methods
class Classification(PrintableEnum):
    """
    Ship component classifications
    """

    CORE = "Core"
    HARDPOINT = "Hardpoint"
    OPTIONAL_INTERNAL = "Optional internal"
    UTILITY = "Utility"
