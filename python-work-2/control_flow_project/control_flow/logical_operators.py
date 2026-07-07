"""
Logical operators demonstration.
"""

def is_eligible(age, citizen):

    return age >= 18 and citizen


def can_access(is_admin, has_permission):

    return is_admin or has_permission


def is_not_logged_in(logged_in):

    return not logged_in



def demo():

    age = 22
    citizen = True

    print(age >= 18 and citizen)

    print(age < 18 or citizen)

    print(not citizen)