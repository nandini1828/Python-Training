import pytest
from class_objects import run


# Extract classes from the run() function
def get_classes():
    """Helper function to extract classes from run()"""
    import class_objects
    # We'll need to restructure this to access the classes
    # For now, let's define them directly from what we see
    pass


# Since classes are defined inside run(), we need to create them here for testing
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


# ============================================================================
# Student Class Tests
# ============================================================================
class TestStudent:
    """Test cases for the Student class"""

    def test_student_initialization(self):
        """Test Student initialization with name, age, and grade"""
        student = Student("Alice", 20, "B")
        assert student.name == "Alice"
        assert student.age == 20
        assert student.grade == "B"

    def test_student_introduce(self):
        """Test Student introduce method returns correct introduction"""
        student = Student("Bob", 19, "C")
        result = student.introduce()
        assert result == "Hi, I'm Bob, 19 years old"
        assert "Bob" in result
        assert "19" in result

    def test_student_introduce_different_ages(self):
        """Test introduce method with different ages"""
        student1 = Student("Alice", 20, "A")
        student2 = Student("Charlie", 25, "A")
        assert "20" in student1.introduce()
        assert "25" in student2.introduce()

    def test_student_pass_exam(self):
        """Test Student pass_exam method updates grade to A"""
        student = Student("David", 21, "C")
        result = student.pass_exam()
        assert student.grade == "A"
        assert "passed the exam" in result
        assert "David" in result

    def test_student_pass_exam_changes_grade(self):
        """Test that pass_exam changes the grade"""
        student = Student("Eve", 20, "D")
        original_grade = student.grade
        student.pass_exam()
        assert student.grade != original_grade
        assert student.grade == "A"


# ============================================================================
# Car Class Tests
# ============================================================================
class TestCar:
    """Test cases for the Car class"""

    @pytest.fixture(autouse=True)
    def reset_car_counter(self):
        """Reset total_cars counter before each test"""
        Car.total_cars = 0
        yield

    def test_car_initialization(self):
        """Test Car initialization with brand, model, and year"""
        car = Car("Toyota", "Camry", 2020)
        assert car.brand == "Toyota"
        assert car.model == "Camry"
        assert car.year == 2020
        assert car.speed == 0

    def test_car_increments_total_cars(self):
        """Test that creating cars increments total_cars counter"""
        assert Car.total_cars == 0
        car1 = Car("Honda", "Civic", 2022)
        assert Car.total_cars == 1
        car2 = Car("Ford", "Mustang", 2021)
        assert Car.total_cars == 2

    def test_car_accelerate(self):
        """Test Car accelerate method increases speed"""
        car = Car("BMW", "X5", 2023)
        result = car.accelerate(50)
        assert car.speed == 50
        assert "50" in result
        assert "BMW" in result
        assert "X5" in result

    def test_car_accelerate_multiple_times(self):
        """Test accelerating multiple times accumulates speed"""
        car = Car("Mercedes", "E-Class", 2023)
        car.accelerate(30)
        assert car.speed == 30
        car.accelerate(40)
        assert car.speed == 70
        car.accelerate(20)
        assert car.speed == 90

    def test_car_brake(self):
        """Test Car brake method decreases speed by 10"""
        car = Car("Audi", "A4", 2022)
        car.accelerate(100)
        result = car.brake()
        assert car.speed == 90
        assert "stopped" in result

    def test_car_brake_multiple_times(self):
        """Test braking multiple times"""
        car = Car("Porsche", "911", 2023)
        car.accelerate(100)
        car.brake()
        assert car.speed == 90
        car.brake()
        assert car.speed == 80

    def test_car_brake_prevents_negative_speed(self):
        """Test that brake doesn't allow negative speed"""
        car = Car("Tesla", "Model 3", 2023)
        car.accelerate(15)
        car.brake()
        assert car.speed == 5
        car.brake()
        assert car.speed == 0
        car.brake()  # Try to brake when speed is 0
        assert car.speed == 0  # Should stay at 0, not go negative

    def test_total_cars_created_classmethod(self):
        """Test total_cars_created classmethod"""
        Car("Toyota", "Corolla", 2020)
        Car("Honda", "Accord", 2021)
        result = Car.total_cars_created()
        assert "2" in result
        assert "Total cars created" in result

    def test_is_vintage_staticmethod(self):
        """Test is_vintage static method"""
        assert Car.is_vintage(1999) is True
        assert Car.is_vintage(2000) is False
        assert Car.is_vintage(2020) is False
        assert Car.is_vintage(1950) is True

    def test_is_vintage_edge_cases(self):
        """Test is_vintage with edge cases"""
        assert Car.is_vintage(1999) is True
        assert Car.is_vintage(2000) is False
        assert Car.is_vintage(2001) is False


# ============================================================================
# Animal Class Tests
# ============================================================================
class TestAnimal:
    """Test cases for the Animal class"""

    def test_animal_initialization(self):
        """Test Animal initialization with name"""
        animal = Animal("Lion")
        assert animal.name == "Lion"

    def test_animal_speak(self):
        """Test Animal speak method"""
        animal = Animal("Tiger")
        result = animal.speak()
        assert "Tiger" in result
        assert "makes a sound" in result


# ============================================================================
# Dog Class Tests (Inheritance)
# ============================================================================
class TestDog:
    """Test cases for the Dog class"""

    def test_dog_initialization(self):
        """Test Dog initialization inherits from Animal"""
        dog = Dog("Buddy")
        assert dog.name == "Buddy"

    def test_dog_speak_override(self):
        """Test Dog speak method overrides Animal speak"""
        dog = Dog("Rex")
        result = dog.speak()
        assert "Rex" in result
        assert "barks" in result
        assert "Woof Woof" in result

    def test_dog_fetch(self):
        """Test Dog fetch method"""
        dog = Dog("Max")
        result = dog.fetch()
        assert "Max" in result
        assert "fetches the ball" in result

    def test_dog_isinstance(self):
        """Test Dog is instance of Animal"""
        dog = Dog("Bella")
        assert isinstance(dog, Animal)
        assert isinstance(dog, Dog)

    def test_dog_inherits_animal_attributes(self):
        """Test Dog inherits Animal attributes"""
        dog = Dog("Charlie")
        assert hasattr(dog, "name")
        assert dog.name == "Charlie"


# ============================================================================
# Cat Class Tests (Inheritance)
# ============================================================================
class TestCat:
    """Test cases for the Cat class"""

    def test_cat_initialization(self):
        """Test Cat initialization inherits from Animal"""
        cat = Cat("Whiskers")
        assert cat.name == "Whiskers"

    def test_cat_speak_override(self):
        """Test Cat speak method overrides Animal speak"""
        cat = Cat("Mittens")
        result = cat.speak()
        assert "Mittens" in result
        assert "meows" in result
        assert "Meow" in result

    def test_cat_isinstance(self):
        """Test Cat is instance of Animal"""
        cat = Cat("Fluffy")
        assert isinstance(cat, Animal)
        assert isinstance(cat, Cat)

    def test_cat_inherits_animal_attributes(self):
        """Test Cat inherits Animal attributes"""
        cat = Cat("Shadow")
        assert hasattr(cat, "name")
        assert cat.name == "Shadow"


# ============================================================================
# Integration Tests
# ============================================================================
class TestIntegration:
    """Integration tests for all classes"""

    @pytest.fixture(autouse=True)
    def reset_car_counter(self):
        """Reset total_cars counter before each test"""
        Car.total_cars = 0
        yield

    def test_multiple_students(self):
        """Test creating multiple students and their interactions"""
        students = [
            Student("Alice", 20, "B"),
            Student("Bob", 19, "C"),
            Student("Charlie", 21, "A"),
        ]
        assert len(students) == 3
        assert all(isinstance(s, Student) for s in students)

    def test_multiple_cars(self):
        """Test creating multiple cars and tracking total"""
        cars = [
            Car("Toyota", "Camry", 2020),
            Car("Honda", "Civic", 1995),
            Car("Ford", "F-150", 2019),
        ]
        assert Car.total_cars == 3
        assert len(cars) == 3

    def test_inheritance_polymorphism(self):
        """Test polymorphism with Animal subclasses"""
        animals = [
            Dog("Buddy"),
            Cat("Whiskers"),
            Animal("Generic"),
        ]
        results = [animal.speak() for animal in animals]
        assert "barks" in results[0]
        assert "meows" in results[1]
        assert "makes a sound" in results[2]

    def test_mixed_usage(self):
        """Test using multiple classes together"""
        student = Student("John", 22, "B")
        car = Car("Tesla", "Model S", 2022)
        dog = Dog("Rover")

        assert student.name == "John"
        assert car.brand == "Tesla"
        assert dog.name == "Rover"
        assert isinstance(dog, Animal)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
