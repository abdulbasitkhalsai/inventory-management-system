from .base_product import Product

class Electronics(Product):
    def __init__(self, name, price, quantity_in_stock, brand, warranty_years, product_id = None):
        super().__init__(name, price, quantity_in_stock, product_id)
        self.brand = brand
        self.warranty_years = warranty_years

    def __str__(self):
        return f"[Electronics] {self._name} - Brand: {self.brand}, Warranty: {self.warranty_years} years, Stock: {self._quantity_in_stock}, Price: ${self._price}"

    def to_dict(self):
        return {
            "type": "Electronics",
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity_in_stock": self.quantity_in_stock,
            "brand": self.brand,
            "warranty_years": self.warranty_years
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            product_id=data["product_id"],
            name=data["name"],
            price=data["price"],
            quantity_in_stock=data["quantity_in_stock"],
            warranty_years=data["warranty_years"],
            brand=data["brand"]
        )
