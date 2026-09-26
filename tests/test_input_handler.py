from calculators.input_handler import get_value_with_unit


def test_value_with_unit_space(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "20 mA")

    value, unit = get_value_with_unit("Enter value: ")

    assert value == 20
    assert unit == "mA"


def test_value_with_unit_no_space(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "4.7k")

    value, unit = get_value_with_unit("Enter value: ")

    assert value == 4.7
    assert unit == "k"


def test_value_with_unit_decimal(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "230 V")

    value, unit = get_value_with_unit("Enter value: ")

    assert value == 230
    assert unit == "V"