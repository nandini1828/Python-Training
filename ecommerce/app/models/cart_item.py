from app.models.product import Product


class CartItem:

    def __init__(self, product: Product, quantity: int = 1):
        self.product = product
        self.quantity = quantity

    def get_total(self):
        return self.product.price * self.quantity

    def increase_quantity(self):
        self.quantity += 1

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"