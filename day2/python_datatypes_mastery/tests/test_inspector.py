from inspectors import (
    get_methods,
    get_methods_and_docs
)


def test_get_methods():

    methods = get_methods(list)

    assert "append" in methods
    assert "clear" in methods


def test_get_methods_and_docs():

    docs = get_methods_and_docs(list)

    assert isinstance(docs, list)

    assert len(docs) > 0