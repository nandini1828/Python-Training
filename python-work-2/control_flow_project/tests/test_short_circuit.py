from control_flow.short_circuit import (
    and_short_circuit,
    or_short_circuit,
)


def test_and_short_circuit():
    assert and_short_circuit() is False


def test_or_short_circuit():
    assert or_short_circuit() is True