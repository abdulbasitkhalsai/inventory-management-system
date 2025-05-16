import json
import os
from models.base_product import Product
from models.electronics import Electronics
from models.grocery import Grocery
from models.clothing import Clothing
from core.exceptions import (
    ProductExistsError,
    ProductNotFoundError,
    OutOfStockError
)

class Inventory:
    def __init__(self, json_file="data/inventory.json"):
        self._products = {}
        self.json_file = json_file
        self._load()

    def add_product(self, product: Product):
        if product.product_id in self._products:
            raise ProductExistsError("Product with this ID already exists.")
        self._products[product.product_id] = product
        self._save()

    def remove_product(self, product_id):
        if product_id not in self._products:
            raise ProductNotFoundError("Product not found.")
        del self._products[product_id]
        self._save()

    def search_by_name(self, name):
        return [p for p in self._products.values() if name.lower() in p.name.lower()]

    def search_by_type(self, product_type):
        return [p for p in self._products.values() if product_type.lower() in type(p).__name__.lower()]

    def list_all_products(self):
        return list(self._products.values())

    def sell_product(self, product_id, quantity):
        product = self._get_product(product_id)
        if product.quantity_in_stock < quantity:
            raise OutOfStockError("Not enough stock to sell.")
        product.sell(quantity)
        self._save()

    def restock_product(self, product_id, quantity):
        product = self._get_product(product_id)
        product.restock(quantity)
        self._save()

    def total_inventory_value(self):
        return sum(p.get_total_value() for p in self._products.values())

    def remove_expired_products(self):
        to_remove = [pid for pid, p in self._products.items()
                     if isinstance(p, Grocery) and p.is_expired()]
        for pid in to_remove:
            del self._products[pid]
        self._save()

    def _get_product(self, product_id):
        if product_id not in self._products:
            raise ProductNotFoundError("Product not found.")
        return self._products[product_id]

    def get_all_products(self):
        return self._products

    def _save(self):
        with open(self.json_file, 'w') as f:
            json.dump(
                [p.to_dict() for p in self._products.values()],
                f,
                indent=4
            )
    def _load(self):
        if not os.path.exists(self.json_file):
            return
        with open(self.json_file, 'r') as f:
            try:
                products_data = json.load(f)
                for data in products_data:
                    product_type = data.get("type")
                    if product_type == "Electronics":
                        product = Electronics.from_dict(data)
                    elif product_type == "Grocery":
                        product = Grocery.from_dict(data)
                    elif product_type == "Clothing":
                        product = Clothing.from_dict(data)
                    else:
                        continue
                    self._products[product.product_id] = product

                # 👇 Update ID counter here
                from models.base_product import Product
                Product.update_id_counter(self._products.values())

            except json.JSONDecodeError:
                pass
