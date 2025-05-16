import re
from abc import ABC, abstractmethod

class Product(ABC):
    _id_counter = 1  # Class-level counter shared across all products

    def __init__(self, name, price, quantity_in_stock, product_id=None):
        if product_id:
            self._product_id = product_id
        else:
            self._product_id = f"PRD{Product._id_counter:05d}"
            Product._id_counter += 1  # Increment only for auto-generated IDs

        self._name = name
        self._price = price
        self._quantity_in_stock = quantity_in_stock

    def restock(self, amount):
        self._quantity_in_stock += amount

    def sell(self, quantity):
        if quantity > self._quantity_in_stock:
            raise ValueError("Not enough stock.")
        self._quantity_in_stock -= quantity

    def get_total_value(self):
        return self._price * self._quantity_in_stock

    @abstractmethod
    def __str__(self):
        pass

    # Read-only property
    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def quantity_in_stock(self):
        return self._quantity_in_stock

    @classmethod
    def from_dict(cls, data):
        return cls(
            product_id=data.get("product_id"),  # Keep ID if loading from saved state
            name=data["name"],
            price=data["price"],
            quantity_in_stock=data["quantity_in_stock"]
        )
    @classmethod
    def update_id_counter(cls, existing_products):
        """
        Updates _id_counter to avoid ID duplication.
        Accepts a list of existing product dictionaries or instances.
        """
        max_id = 0
        pattern = re.compile(r"PRD(\d{5})")

        for product in existing_products:
            product_id = product.product_id if isinstance(product, Product) else product.get("product_id", "")
            match = pattern.match(str(product_id))
            if match:
                id_num = int(match.group(1))
                if id_num > max_id:
                    max_id = id_num

        cls._id_counter = max_id + 1