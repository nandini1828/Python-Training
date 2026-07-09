"""
Shows how yield pauses and resumes execution.
"""


class GeneratorDemo:

    @staticmethod
    def counter():

        x = 1

        print("Before First Yield")

        yield x

        x += 1

        print("Before Second Yield")

        yield x

        x += 1

        print("Before Third Yield")

        yield x

    @staticmethod
    def demonstrate():

        generator = GeneratorDemo.counter()

        print(next(generator))

        print()

        print(next(generator))

        print()

        print(next(generator)) 


if __name__ == "__main__":
    GeneratorDemo.demonstrate()