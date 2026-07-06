from dunder_methods.dunder_examples import BankAccount


def test_dunder_eq_add():
    a = BankAccount("A", 100)
    b = BankAccount("B", 200)
    c = a + b
    assert isinstance(c, BankAccount)
    assert c.balance == 300
    assert (a == b) is False
