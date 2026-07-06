def search_product(products, search_name):

    print("\nSearching Product")

    for product in products:

        if product.name == search_name:

            print(f"{search_name} Found")

            break

    else:

        print(f"{search_name} Not Found")


def complete_deliveries(total):

    print("\nCompleting Deliveries")

    count = 1

    while count <= total:

        print(f"Completed Delivery {count}")

        count += 1

    else:

        print("All Deliveries Completed Successfully")