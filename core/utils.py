import json
from models.electronics import Electronics
from models.grocery import Grocery
from models.clothing import Clothing
from models.base_product import Product

def load_from_file(inventory, filename="inventory.json"):
    try:
        with open(filename, "r") as f:
            products_dict = json.load(f)

        for product_id, product_data in products_dict.items():
            # Dynamically select the correct class based on the product data
            if product_data["type"] == "Electronics":
                product = Electronics.from_dict(product_data)
            elif product_data["type"] == "Grocery":
                product = Grocery.from_dict(product_data)
            elif product_data["type"] == "Clothing":
                product = Clothing.from_dict(product_data)
            else:
                # Default to Product or handle error
                product = Product.from_dict(product_data)

            inventory.add_product(product)

        print(f"Inventory loaded from {filename}")
    except Exception as e:
        print(f"Error loading inventory: {e}")

def save_to_file(inventory, filename="inventory.json"):
    try:
        # Get all products from the inventory
        products = inventory.get_all_products()
        # Serialize products to a dictionary
        products_dict = {pid: product.to_dict() for pid, product in products.items()}
        
        with open(filename, "w") as f:
            json.dump(products_dict, f, indent=4)
        print(f"Inventory saved to {filename}")
    except Exception as e:
        print(f"Error saving inventory: {e}")