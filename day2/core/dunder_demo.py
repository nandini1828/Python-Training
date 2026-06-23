class DunderDemo:

    @staticmethod
    def equality_demo():
        return (15).__eq__(15)

    @staticmethod
    def addition_demo():
        return "Hello".__add__(" World")

    @staticmethod
    def contains_demo():
        return "Python".__contains__("Py")

    @staticmethod
    def absolute_demo():
        return (-42).__abs__()