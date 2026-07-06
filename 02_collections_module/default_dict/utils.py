from collections import defaultdict


def group_students(data):
    """
    Group students by department.
    """

    students = defaultdict(list)

    for name, dept in data:
        students[dept].append(name)

    return students