# class_objects.py

def run():
    title = "Class Objects"
    description = "Shows Python class definitions, attributes, methods, class methods, and inheritance."

    class Student:
        def __init__(self, name, age, grade):
            self.name = name
            self.age = age
            self.grade = grade

        def introduce(self):
            return f"Hi, I'm {self.name}, {self.age} years old"

        def pass_exam(self):
            self.grade = "A"
            return f"{self.name} passed the exam!"

    class Car:
        total_cars = 0

        def __init__(self, brand, model, year):
            self.brand = brand
            self.model = model
            self.year = year
            self.speed = 0
            Car.total_cars += 1

        def accelerate(self, increase):
            self.speed += increase
            return f"{self.brand} {self.model} speed: {self.speed} km/h"

        def brake(self):
            self.speed = max(0, self.speed - 10)
            return f"{self.brand} {self.model} stopped"

        @classmethod
        def total_cars_created(cls):
            return f"Total cars created: {cls.total_cars}"

        @staticmethod
        def is_vintage(year):
            return year < 2000

    class Animal:
        def __init__(self, name):
            self.name = name

        def speak(self):
            return f"{self.name} makes a sound"

    class Dog(Animal):
        def speak(self):
            return f"{self.name} barks: Woof Woof!"

        def fetch(self):
            return f"{self.name} fetches the ball"

    class Cat(Animal):
        def speak(self):
            return f"{self.name} meows: Meow!"

    student1 = Student("Alice", 20, "B")
    student2 = Student("Bob", 19, "C")
    car1 = Car("Toyota", "Camry", 2020)
    car2 = Car("Honda", "Civic", 1995)
    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    details = [
        "### Student class",
        student1.introduce(),
        student2.pass_exam(),
        "",
        "### Car class",
        car1.accelerate(50),
        car1.brake(),
        Car.total_cars_created(),
        f"Car.is_vintage(1995) = {Car.is_vintage(1995)}",
        f"Car.is_vintage(2020) = {Car.is_vintage(2020)}",
        "",
        "### Inheritance examples",
        dog.speak(),
        dog.fetch(),
        cat.speak(),
        f"isinstance(dog, Animal) = {isinstance(dog, Animal)}",
    ]

    return {
        "title": title,
        "description": description,
        "details": "\n".join(details),
    }


if __name__ == "__main__":
    result = run()
    print(result["title"])
    print(result["description"])
    print(result["details"])
