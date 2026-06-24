from .dunder_utils import ImmutableMatrix, NamingContext


def run_dunder_demo() -> None:
    matrix = ImmutableMatrix(((1, 2), (3, 4)))
    transposed = matrix.transpose()
    context = NamingContext({"project": "Python Datatypes", "version": "1.0.0"})

    print("Original matrix:", matrix)
    print("Transposed matrix:", transposed)
    print("Matrix equal to itself:", matrix == ImmutableMatrix(((1, 2), (3, 4))))
    print("Has project attribute:", "project" in context)
    print("Project value:", context.project)
