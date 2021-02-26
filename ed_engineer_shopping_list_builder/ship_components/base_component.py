"""
A base ship component
"""
from typing import List, Optional, Dict

from ed_engineer_shopping_list_builder import inputs
from ed_engineer_shopping_list_builder.classification import Classification
from ed_engineer_shopping_list_builder.effect import ExperimentalEffect
from ed_engineer_shopping_list_builder.modification import Modification


class BaseComponent:
    """
    A base ship component
    """

    # A list of possible modifications and effects
    _modifications = []  # type: List[Modification]
    _effects = []  # type: List[ExperimentalEffect]

    # Defaults, if a modification or effect is left empty
    _default_modification = None  # type: Optional[Modification]
    _default_max_grade = 5
    _default_effect = None  # type: Optional[ExperimentalEffect]

    name = ""
    # What kind of thing is this
    component_classification = None  # type: Classification
    # Can there only be one of this kind of component
    is_singleton = False

    def __init__(self):
        self.selected_modification = ""
        self.max_modification_grade = 0
        self.selected_effect = ""
        self.configure()

    def configure(self):
        """
        Configure this model with a modification and/or effect
        """
        if self._modifications:
            self._select_modification()
        if self._effects:
            self._select_effect()

    @property
    def modifications(self) -> List[str]:
        """
        Modifications which can apply to this component
        """
        return self._modifications

    @property
    def effects(self) -> List[str]:
        """
        Effects which can apply to this component
        """
        return self._effects

    def _select_modification(self):
        """
        .
        """
        self.selected_modification = inputs.make_choice(
            "modification", [None] + self._modifications, self._default_modification
        )

        if self.selected_modification:
            self.max_modification_grade = inputs.get_grade(self.max_modification_grade)

    def _select_effect(self):
        """
        .
        """
        self.selected_effect = inputs.make_choice(
            "effect", [None] + self._effects, self._default_effect
        )

    def to_shopping_list(self, cmdr_name: str, grade_counts: Dict[int, int]) -> str:
        """
        Formats this component into a shopping list entry
        """
        base = f"{cmdr_name}:G{{grade}} [{self.name}] {{modification}}"
        shopping_list = ""
        if self.selected_modification:
            for i in range(1, self.max_modification_grade + 1):
                for j in range(grade_counts[i]):
                    shopping_list += (
                        '"'
                        + base.format(grade=i, modification=self.selected_modification)
                        + '"'
                    ) + (
                        ","
                        if i != self.max_modification_grade or j < grade_counts[i] - 1
                        else ""
                    )

        if self.selected_effect:
            shopping_list += (
                ("," if self.selected_modification else "")
                + '"'
                + base.format(grade="", modification=self.selected_effect)
                + '"'
            )

        return shopping_list

    def __str__(self):
        """
        String representation of this component
        """
        return (
            f"{self.name}"
            + (" | " if self.selected_modification or self.selected_effect else "")
            + (
                f"G{self.max_modification_grade} {self.selected_modification}"
                if self.selected_modification
                else ""
            )
            + (" " if self.selected_modification and self.selected_effect else "")
            + (f"[{self.selected_effect}]" if self.selected_effect else "")
        )
