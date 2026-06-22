# First we need to check the type of the variable
# We can use the type() function to check the type of a variable
# We can also use the id() function to check the unique identifier of a variable
# We can use the dir() function to check the attributes and methods of a variable

print(isinstance(10, int))  # True
print(isinstance(10.5, float))  # True
# It checks whether the first argument is of type second argument ot not. It returns True if the first argument is of type second argument, otherwise it returns False.

class Animal:
    pass
class Dog(Animal):
    pass
dog = Dog()
print(isinstance(dog, Animal))  # True


price = "99.99"
price = float(price)
print(price)
print(type(price))

# OUTPUT
# 99.99
# <class 'float'>

age = 21
age = str(age)
print(age)
print(type(age))

# OUTPUT:
# 21
# <class 'str'>


value = 10.75
value = int(value)
print(value)
print(type(value))

# OUTPUT:
# 10
# <class 'int'>

