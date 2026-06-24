from __future__ import annotations

from dunder_methods.dunder_utils import DunderDemo


def test_dunder_demo_representation() -> None:
    demo = DunderDemo("Ada", 37)
    assert repr(demo) == "DunderDemo(name='Ada', age=37)"
    assert str(demo) == "Ada (37)"
    assert demo != DunderDemo("Grace", 37)
