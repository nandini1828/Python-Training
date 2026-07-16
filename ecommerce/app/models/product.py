class Product:

    def __init__(self, product_id, name, price, stock, category, description=None):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
        self.description = description

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Product({self.product_id}, {self.name})"

    def __lt__(self, other):
        return self.price < other.price