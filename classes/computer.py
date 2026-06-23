class CPU:
    """Represents CPU configuration details."""

    def __init__(self, cores):
        """Initialize a CPU with the given number of cores."""
        self.cores = cores


class Computer:
    """Represents a computer composed of a brand and a CPU object."""

    def __init__(self, brand, cpu):
        """Initialize a Computer with a brand name and CPU instance."""
        self.brand = brand
        self.cpu = cpu
