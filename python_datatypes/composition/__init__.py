"""Composition module demonstrating object relationships and responsibility delegation."""

from .demo import run_composition_demo
from .composition_utils import Address, Customer, Order, OrderHistory

__all__ = ["run_composition_demo", "Address", "Customer", "Order", "OrderHistory"]
