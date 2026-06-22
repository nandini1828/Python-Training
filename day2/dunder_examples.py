# Dunder = __something__
# The main goal of dunder methods is to make code cleaner, more intuitive, and highly readable. 
# Also called:
#     Magic Methods
#     Special Methods

# 10 + 20 can also be written as 10.__add__(20)

# "Hello"+"World" = > "Hello".__add__("World")

# len("Python") => "Python".__len__()

# "Py" in "Python" => "Python".__contains__("Py")

# 15 == 15 => (15).__eq__(15)

def equality_demo():
    result = (15).__eq__(15)
    print("\nEquality Demo")
    print(result)

def addition_demo():
    result = "Hello".__add__(" World")
    print("\nAddition Demo")
    print(result)

def length_demo():
    result = "Python".__len__()
    print("\nLength Demo")
    print(result)

def contains_demo():
    result = "Python".__contains__("Py")
    print("\nContains Demo")
    print(result)

def absolute_demo():
    result = (-42).__abs__()
    print("\nAbsolute Demo")
    print(result)

if __name__ == "__main__":
    equality_demo()
    addition_demo()
    length_demo()
    contains_demo()
    absolute_demo()