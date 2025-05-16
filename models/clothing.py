from .base_product import Product

class Clothing(Product):
    def __init__(self, name, price, quantity_in_stock, size, material, product_id = None):
        super().__init__(name, price, quantity_in_stock, product_id)
        self.size = size
        self.material = material

    def __str__(self):
        return f"[Clothing] {self._name} - Size: {self.size}, Material: {self.material}, Stock: {self._quantity_in_stock}, Price: ${self._price}"

    def to_dict(self):
        return {
            "type": "Clothing",
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity_in_stock": self.quantity_in_stock,
            "size": self.size,
            "material": self.material
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            product_id=data["product_id"],
            name=data["name"],
            price=data["price"],
            quantity_in_stock=data["quantity_in_stock"],
            size=data["size"],
            material=data["material"]
        )
