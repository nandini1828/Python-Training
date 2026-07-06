def discounted_prices(books):

    print("\nDiscounted Prices")

    prices = (

        book.price * 0.90

        for book in books

    )

    for price in prices:

        print(price)