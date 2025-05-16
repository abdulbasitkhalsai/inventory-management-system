import streamlit as st
from core.inventory import Inventory
from ui.sidebar import sidebar_menu
from ui import (
    add_product,
    view_inventory,
    sell_product,
    restock_product,
)
# Initialize session state
from models.base_product import Product 

if "inventory" not in st.session_state:
    st.session_state.inventory = Inventory()


    Product.update_id_counter(st.session_state.inventory.list_all_products())
# Sidebar Navigation
page = sidebar_menu()

st.title("📦 Inventory Management System")

# Page Routing
if page == "Add Product":
    add_product.render()
elif page == "Sell Product":
    sell_product.render()
elif page == "Restock Product":
    restock_product.render()
else:
    view_inventory.render()