"""
break, continue and pass
"""


def break_demo():

    for number in range(10):

        if number == 5:
            break

        print(number)


def continue_demo():

    for number in range(10):

        if number % 2 == 0:
            continue

        print(number)


def pass_demo():

    for _ in range(3):
        pass

    print("Loop finished")


def demo():

    break_demo()

    continue_demo()

    pass_demo()