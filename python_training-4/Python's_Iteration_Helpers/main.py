from model import Student

from utils import print_title

from range_helper import generate_roll_numbers
from enumerate_helper import display_students
from zip_helper import compare_subject_marks, compare_extra_subject
from reversed_helper import display_reverse
from sorted_helper import sort_students
from any_all_helper import distinction, all_pass


def main():

    students = [

        Student("John", 95, 92),
        Student("Alice", 88, 91),
        Student("David", 78, 82),
        Student("Emma", 35, 40)

    ]

    print_title("Student Result Management System")

    generate_roll_numbers(len(students))

    display_students(students)

    compare_subject_marks(students)

    compare_extra_subject()

    display_reverse(students)

    sort_students(students)

    distinction(students)

    all_pass(students)


if __name__ == "__main__":
    main()