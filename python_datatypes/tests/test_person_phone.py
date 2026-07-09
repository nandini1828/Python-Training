from python_datatypes.person_phone import Person


def test_add_and_get_phones():
    p = Person("Alice")
    p.add_phone("12345")
    p.add_phone("98765", type="home")
    phones = p.get_phones()
    assert len(phones) == 2
    assert phones[0].number == "12345"
    assert phones[1].type == "home"


def test_remove_phone():
    p = Person("Bob")
    p.add_phone("555")
    assert p.remove_phone("555") is True
    assert p.get_phones() == []


def test_find_phones_starting_with():
    p = Person("Carol")
    p.add_phone("123")
    p.add_phone("124")
    p.add_phone("999")
    found = p.find_phones_starting_with("12")
    assert len(found) == 2
    assert all(ph.number.startswith("12") for ph in found)
