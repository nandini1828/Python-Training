from python_datatypes.dunder_methods import ImmutableMatrix, NamingContext


def test_immutable_matrix_transpose() -> None:
    matrix = ImmutableMatrix(((1, 2), (3, 4)))
    assert matrix.transpose() == ImmutableMatrix(((1, 3), (2, 4)))


def test_naming_context_attribute_lookup() -> None:
    context = NamingContext({"project": "Python Datatypes"})
    assert context.project == "Python Datatypes"
    assert "project" in context
