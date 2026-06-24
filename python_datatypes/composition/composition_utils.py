from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Address:
    street: str
    city: str
    postal_code: str
    country: str


@dataclass
class Order:
    order_id: str
    quantity: int
    price_per_unit: float

    def total(self) -> float:
        return self.quantity * self.price_per_unit


@dataclass
class OrderHistory:
    orders: List[Order] = field(default_factory=list)

    def add_order(self, order: Order) -> None:
        self.orders.append(order)

    def total_revenue(self) -> float:
        return sum(order.total() for order in self.orders)


@dataclass
class Customer:
    customer_id: str
    name: str
    address: Address
    order_history: OrderHistory = field(default_factory=OrderHistory)

    def place_order(self, order: Order) -> None:
        self.order_history.add_order(order)

    def billing_summary(self) -> str:
        revenue = self.order_history.total_revenue()
        return f"Customer {self.name} owes ${revenue:.2f}"
