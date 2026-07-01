from collections import namedtuple


Student = namedtuple(

    "Student",

    ["id","name","course"]

)


def create_student():

    return Student(

        101,

        "Sagar",

        "Python"

    )