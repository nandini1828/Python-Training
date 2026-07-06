class Student:

    def __init__(self, name, maths, science):

        self.name = name
        self.maths = maths
        self.science = science

    def average(self):

        return (self.maths + self.science) / 2