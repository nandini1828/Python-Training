import asyncio
from functools import reduce

from app.models.order import Order
from app.services.cart_service import CartService
from app.utils.exceptions import CartEmpty
from app.utils.exceptions import OrderNotFound
from app.utils.store import Store


class OrderService:

    @staticmethod
    async def place_order(customer_id):

        cart = CartService.get_cart(customer_id)

        if len(cart) == 0:
            raise CartEmpty("Cart is empty.")

        await asyncio.sleep(2)

        order = Order(
            Store.order_id,
            customer_id,
            cart.items.copy(),
            cart.get_total()
        )

        Store.orders[Store.order_id] = order

        Store.order_id += 1

        cart.clear()

        return order

    @staticmethod
    def get_all_orders():

        return list(Store.orders.values())

    @staticmethod
    def get_order(order_id):

        order = Store.orders.get(order_id)

        if order is None:
            raise OrderNotFound("Order not found.")

        return order

    @staticmethod
    def total_sales():

        return reduce(
            lambda total, order: total + order.total,
            Store.orders.values(),
            0
        )

    @staticmethod
    def order_summary():

        summary = []

        for index, order in enumerate(Store.orders.values(), start=1):

            summary.append(
                {
                    "S.No": index,
                    "Order ID": order.order_id,
                    "Total": order.total
                }
            )

        return summary

    @staticmethod
    def order_details():

        ids = Store.orders.keys()

        totals = [order.total for order in Store.orders.values()]

        return list(zip(ids, totals))

    @staticmethod
    def cancel_order(order_id):
        if order_id not in Store.orders:
            raise OrderNotFound("Order not found.")
        order = Store.orders[order_id]
        order.cancel_order()
        return order
