"""
Composition example with CPU and Computer classes.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class CPU:
    """Simple CPU description used for composition."""

    cores: int
    frequency_ghz: float


class Computer:
    """
    Computer composed of a brand and a CPU object.

    Demonstrates nested objects and the `__dict__` contents.
    """

    def __init__(self, brand: str, cpu: CPU) -> None:
        self.brand = brand
        self.cpu = cpu

    def specs(self) -> Dict[str, Any]:
        """Return a simple specs dictionary extracted from nested objects."""
        return {"brand": self.brand, "cpu": {"cores": self.cpu.cores, "frequency_ghz": self.cpu.frequency_ghz}}
