"""
==================================================
Module: Composition Example
Topic: Composition
Author: Nandini

Description:
Demonstrates composition where a Car
contains an Engine.
==================================================
"""


class Engine:
    """
    Engine class.
    """

    def start(self):
        """
        Start the engine.
        """
        print("Engine Started")


class Car:
    """
    Car class using composition.
    """

    def __init__(self):
        self.engine = Engine()

    def drive(self):
        """
        Drive the car.
        """
        self.engine.start()
        print("Car is Moving")