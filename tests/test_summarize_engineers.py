"""
Tests the summary of engineers
"""

from ed_engineer_shopping_list_builder import inputs, utils, summarize_engineers
from ed_engineer_shopping_list_builder.engineers import (
    LizRyder,
    LeiCheung,
    BillTurner,
    SeleneJean,
    JuriIshmaak,
)
from ed_engineer_shopping_list_builder.ship_components import (
    Armour,
    DetailedSurfaceScanner,
    FrameShiftWakeScanner,
    HullReinforcementPackage,
    KillWarrantScanner,
    ManifestScanner,
    MineLauncher,
    MissileRack,
    Sensors,
    TorpedoPylon,
)


def test_get_available_engineers(monkeypatch):
    """
    .
    """
    monkeypatch.setattr(
        inputs,
        "make_choices",
        lambda *args, **kwargs: ["Bill Turner", "Liz Ryder", "Lei Cheung"],
    )
    assert summarize_engineers.get_available_engineers() == [
        BillTurner,
        LizRyder,
        LeiCheung,
    ], "Expected engineers returned"


def test_simplify_components():
    """
    .
    """
    assert summarize_engineers.simplify_engineer_components(
        [SeleneJean, JuriIshmaak, LizRyder]
    ) == {
        Armour: SeleneJean,
        DetailedSurfaceScanner: JuriIshmaak,
        FrameShiftWakeScanner: JuriIshmaak,
        HullReinforcementPackage: SeleneJean,
        KillWarrantScanner: JuriIshmaak,
        ManifestScanner: JuriIshmaak,
        MineLauncher: JuriIshmaak,
        MissileRack: LizRyder,
        Sensors: JuriIshmaak,
        TorpedoPylon: LizRyder,
    }, "Correct modifications returned"


def test_print_summary(monkeypatch, capsys):
    """
    .
    """
    # pylint: disable=unused-argument
    monkeypatch.setattr(
        utils, "organize_components_by_classification", lambda components: []
    )
    monkeypatch.setattr(
        utils,
        "get_component_summary_by_classification",
        lambda components, func: "a description",
    )

    summarize_engineers.print_component_summary({})
    printed = capsys.readouterr()
    assert printed.out == "a description", "Ship summary returned"


def test_summarize_engineers(monkeypatch):
    """
    .
    """

    # pylint: disable=unused-argument
    @utils.counter_wrapper
    def get_available(*args, **kwargs):
        """
        .
        """

    @utils.counter_wrapper
    def simplify(*args, **kwargs):
        """
        .
        """

    @utils.counter_wrapper
    def print_summary(*args, **kwargs):
        """
        .
        """

    monkeypatch.setattr(summarize_engineers, "get_available_engineers", get_available)
    monkeypatch.setattr(summarize_engineers, "simplify_engineer_components", simplify)
    monkeypatch.setattr(summarize_engineers, "print_component_summary", print_summary)

    summarize_engineers.summarize_engineers()
    assert get_available.counter == 1, "Available engineers returned"
    assert simplify.counter == 1, "Simplified components"
    assert print_summary.counter == 1, "Printed summary"
