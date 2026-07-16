from app.models.product import Product
from app.utils.store import Store
from app.utils.exceptions import ProductNotFound


class ProductService:

    @staticmethod
    def add_product(name, price, stock, category, description=None):

        product = Product(
            product_id=Store.product_id,
            name=name,
            price=price,
            stock=stock,
            category=category,
            description=description
        )

        Store.products[Store.product_id] = product
        Store.product_id += 1

        return product

    @staticmethod
    def get_all_products():
        return list(Store.products.values())

    @staticmethod
    def get_product(product_id):

        product = Store.products.get(product_id)

        if product is None:
            raise ProductNotFound("Product not found.")

        return product

    @staticmethod
    def update_product(product_id, **kwargs):

        product = ProductService.get_product(product_id)

        if "name" in kwargs:
            product.name = kwargs["name"]

        if "price" in kwargs:
            product.price = kwargs["price"]

        if "stock" in kwargs:
            product.stock = kwargs["stock"]

        if "category" in kwargs:
            product.category = kwargs["category"]

        if "description" in kwargs:
            product.description = kwargs["description"]

        return product

    @staticmethod
    def delete_product(product_id):

        if product_id not in Store.products:
            raise ProductNotFound("Product not found.")

        return Store.products.pop(product_id)

    @staticmethod
    def search_products(keyword):

        return list(
            filter(
                lambda product: keyword.lower() in product.name.lower(),
                Store.products.values()
            )
        )

    @staticmethod
    def get_products_by_category(category):

        return list(
            filter(
                lambda product: product.category.lower() == category.lower(),
                Store.products.values()
            )
        )

    @staticmethod
    def sort_products_by_price():

        return sorted(Store.products.values(), key=lambda p: p.price)