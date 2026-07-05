from modules.loop_project.loops.loop_control import (
    calculate_running_total,
    collect_even_numbers,
    filter_active_customers,
    find_first_failed_transaction,
    first_high_value_sale,
    future_discount_feature,
    skip_negative_numbers,
)


def test_find_first_failed_transaction():
    transactions = [True, True, False, True]
    assert find_first_failed_transaction(transactions) == 2


def test_find_first_failed_transaction_all_success():
    transactions = [True, True, True]
    assert find_first_failed_transaction(transactions) is None


def test_filter_active_customers():
    customers = [
        {"name": "Alice", "active": True},
        {"name": "Bob", "active": False},
        {"name": "Charlie", "active": True},
    ]

    expected = [
        {"name": "Alice", "active": True},
        {"name": "Charlie", "active": True},
    ]

    assert filter_active_customers(customers) == expected


def test_collect_even_numbers():
    numbers = [1, 2, 3, 4, 5, 6]
    assert collect_even_numbers(numbers) == [2, 4, 6]


def test_collect_even_numbers_empty():
    assert collect_even_numbers([1, 3, 5]) == []


def test_skip_negative_numbers():
    numbers = [-10, 5, -3, 8, 12]
    assert skip_negative_numbers(numbers) == [5, 8, 12]


def test_skip_negative_numbers_all_negative():
    assert skip_negative_numbers([-1, -2, -3]) == []


def test_first_high_value_sale():
    sales = [100, 200, 600, 800]
    assert first_high_value_sale(sales, 500) == 600


def test_first_high_value_sale_not_found():
    sales = [100, 200, 300]
    assert first_high_value_sale(sales, 500) is None


def test_calculate_running_total():
    assert calculate_running_total([10, 20, 30]) == 60


def test_calculate_running_total_empty():
    assert calculate_running_total([]) == 0


def test_future_discount_feature():
    assert future_discount_feature() is None