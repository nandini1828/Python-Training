from app.models.cart_item import CartItem


class Cart:

    def __init__(self):
        self.items = []

    def add_item(self, product):

        for item in self.items:

            if item.product.product_id == product.product_id:
                item.increase_quantity()
                return

        self.items.append(CartItem(product))

    def remove_item(self, product_id):

        for item in self.items:

            if item.product.product_id == product_id:
                self.items.remove(item)
                return

    def clear(self):
        self.items.clear()

    def get_total(self):

        total = 0

        for item in self.items:
            total += item.get_total()

        return total

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, product):

        for item in self.items:

            if item.product == product:
                return True

        return False

    def __str__(self):
        return f"Cart({len(self.items)} items)"