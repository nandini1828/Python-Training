from collections import Counter
from collections import defaultdict
from collections import deque


recent_products = deque(maxlen=5)


def category_count(products):

    categories = []

    for product in products:
        categories.append(product.category)

    return Counter(categories)


def group_by_category(products):

    grouped = defaultdict(list)

    for product in products:

        grouped[
            product.category
        ].append(product)

    return grouped


def add_recent_product(product):

    recent_products.append(product)


def get_recent_products():

    return list(recent_products)