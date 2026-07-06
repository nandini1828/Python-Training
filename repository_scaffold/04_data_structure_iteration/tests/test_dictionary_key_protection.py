from dictionary_key_protection.utils import (
    clear_dictionary,
    filter_by_key,
    get_value_safe,
    key_exists,
    merge_with_override,
    remove_key_safely,
    set_default_value,
    update_dictionary,
)


def test_dictionary_protection_helpers():
    data = {'city': 'Pune'}
    assert get_value_safe(data, 'city') == 'Pune'
    assert get_value_safe(data, 'state', 'India') == 'India'
    assert set_default_value(data, 'country', 'India')['country'] == 'India'
    assert update_dictionary(data, {'city': 'Mumbai'})['city'] == 'Mumbai'
    assert merge_with_override(data, {'city': 'Mumbai'})['city'] == 'Mumbai'
    assert remove_key_safely(data, 'city') == {}
    assert key_exists(data, 'city') is True
    assert filter_by_key(data, ['city']) == {'city': 'Pune'}
    assert clear_dictionary(data) == {}
