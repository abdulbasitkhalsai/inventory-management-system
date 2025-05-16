from .base_product import Product
from datetime import datetime

class Grocery(Product):
    def __init__(self, name, price, quantity_in_stock, expiry_date, product_id=None):
        super().__init__(name, price, quantity_in_stock, product_id)
        if isinstance(expiry_date, str):
            self.expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d").date()
        elif isinstance(expiry_date, datetime):
            self.expiry_date = expiry_date.date()
        else:
            self.expiry_date = expiry_date

    def is_expired(self):
        return datetime.now().date() > self.expiry_date

    def __str__(self):
        status = "Expired" if self.is_expired() else "Fresh"
        return f"[Grocery] {self._name} - Expiry: {self.expiry_date} ({status}), Stock: {self._quantity_in_stock}, Price: ${self._price}"

    def to_dict(self):
        return {
            "type": "Grocery",
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity_in_stock": self.quantity_in_stock,
            "expiry_date": self.expiry_date.strftime("%Y-%m-%d")
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            product_id=data["product_id"],
            name=data["name"],
            price=data["price"],
            quantity_in_stock=data["quantity_in_stock"],
            expiry_date=data["expiry_date"]
        )
