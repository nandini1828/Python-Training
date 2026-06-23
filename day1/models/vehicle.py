from abc import ABC
from abc import abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self) -> None:
        pass


class Car(Vehicle):

    def start(self) -> None:
        print("Car Started")