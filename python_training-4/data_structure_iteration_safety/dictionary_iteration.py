def display_inventory(inventory):

    print("\nDictionary Keys")

    for key in inventory.keys():

        print(key)

    print("\nDictionary Values")

    for value in inventory.values():

        print(value)

    print("\nDictionary Items")

    for key,value in inventory.items():

        print(key,value)