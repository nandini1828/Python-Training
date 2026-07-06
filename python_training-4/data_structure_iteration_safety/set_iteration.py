def display_categories(products):

    print("\nUnique Categories")

    categories = {

        product.category

        for product in products

    }

    for category in categories:

        print(category)

    print("\nFast Membership Test")

    print("Electronics" in categories)