"""Composition example: Computer composed of Processor, Memory, Storage.

This module demonstrates composition relationships in an enterprise-like
structure: a `Computer` is composed of `Processor`, `Memory`, and
`Storage` components.
"""

from typing import Any, Optional
import logging

logger = logging.getLogger(__name__)


class Processor:
    """Lightweight CPU representation."""

    def __init__(self, cores: int = 4, frequency_ghz: float = 3.2) -> None:
        self.cores = cores
        self.frequency_ghz = frequency_ghz

    def start(self) -> str:
        """Start the processor and return status."""

        status = f"Processor started ({self.cores} cores @ {self.frequency_ghz}GHz)"
        logger.debug(status)
        return status


class Memory:
    """Simple memory component."""

    def __init__(self, size_gb: int = 16) -> None:
        self.size_gb = size_gb

    def allocate(self, mb: int) -> str:
        msg = f"Allocated {mb}MB on {self.size_gb}GB memory"
        logger.debug(msg)
        return msg


class Storage:
    """Storage component (HDD/SSD)."""

    def __init__(self, capacity_gb: int = 512, ssd: bool = True) -> None:
        self.capacity_gb = capacity_gb
        self.ssd = ssd

    def read(self, path: str) -> str:
        msg = f"Read from {path} on {'SSD' if self.ssd else 'HDD'}"
        logger.debug(msg)
        return msg


class Computer:
    """Computer composed from Processor, Memory and Storage components."""

    def __init__(self, processor: Optional[Processor] = None, memory: Optional[Memory] = None, storage: Optional[Storage] = None) -> None:
        self.processor = processor or Processor()
        self.memory = memory or Memory()
        self.storage = storage or Storage()

    def boot(self) -> None:
        """Boot sequence that demonstrates composition usage."""

        logger.info("Booting computer...")
        proc_msg = self.processor.start()
        mem_msg = self.memory.allocate(128)
        storage_msg = self.storage.read("/boot/kernel")

        print(proc_msg)
        print(mem_msg)
        print(storage_msg)
