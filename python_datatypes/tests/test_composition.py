from composition.composition_example import Computer


def test_computer_boot():
    c = Computer()
    # boot prints but we assert components exist
    assert hasattr(c, "processor") and hasattr(c, "memory") and hasattr(c, "storage")
