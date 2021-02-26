"""
Component classification
"""
from ed_engineer_shopping_list_builder.printable_enum import PrintableEnum


class Classification(PrintableEnum):
    CORE = "Core"
    HARDPOINT = "Hardpoint"
    OPTIONAL_INTERNAL = "Optional internal"
    UTILITY = "Utility"
