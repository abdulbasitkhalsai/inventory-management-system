import streamlit as st
from models.base_product import Product
from models.electronics import Electronics
from models.grocery import Grocery
from models.clothing import Clothing
from core.exceptions import ProductExistsError
import datetime


def render():
    st.header("➕ Add New Product")

    next_id = f"PRD{Product._id_counter:05d}"

    # Show next Product ID (auto-generated, read-only)
    product_type = st.selectbox("Select Product Type", ["Electronics", "Grocery", "Clothing"])
    st.text_input("Product ID", value=next_id, disabled=True)

    name = st.text_input("Product Name")
    price = st.number_input("Price", min_value=0.0)
    quantity = st.number_input("Quantity in Stock", min_value=0)

    additional_fields = {}

    if product_type == "Electronics":
        additional_fields["brand"] = st.text_input("Brand")
        additional_fields["warranty_years"] = st.number_input("Warranty (Years)", min_value=0)
    elif product_type == "Grocery":
        additional_fields["expiry_date"] = st.date_input("Expiry Date", min_value=datetime.date.today())
    elif product_type == "Clothing":
        additional_fields["size"] = st.selectbox("Size", ["S", "M", "L", "XL"])
        additional_fields["material"] = st.text_input("Material")

    if st.button("Add Product"):
        try:
            if product_type == "Electronics":
                product = Electronics(name=name, price=price, quantity_in_stock=quantity, **additional_fields)
            elif product_type == "Grocery":
                product = Grocery(name=name, price=price, quantity_in_stock=quantity, **additional_fields)
            elif product_type == "Clothing":
                product = Clothing(name=name, price=price, quantity_in_stock=quantity, **additional_fields)

            st.session_state.inventory.add_product(product)
            # st.success(f"{product_type} added successfully with ID: {product.product_id}")
            st.success(f"{product.product_id} - {product.name} added in {product_type} category successfully!")
        except ProductExistsError as e:
            st.error(str(e))
        except Exception as e:
            st.error(f"Error: {e}")
