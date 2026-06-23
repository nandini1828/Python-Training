class Animal:

    def eat(self) -> None:
        print("Animal is eating")

class Dog(Animal):

    def __init__(
        self,
        name: str
    ) -> None:
        self.name = name

    def bark(self) -> None:
        print(f"{self.name} is barking")