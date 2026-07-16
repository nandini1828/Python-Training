from dataclasses import dataclass


@dataclass
class SalesReport:

    total_orders: int

    total_products: int

    total_customers: int

    total_sales: float