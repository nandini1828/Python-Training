"""
Composition example
"""


class CPU:

    def __init__(self, cores):
        self.cores = cores


class Computer:

    def __init__(self, brand, cpu):
        self.brand = brand
        self.cpu = cpu