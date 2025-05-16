import streamlit as st
import pandas as pd

def render():
    st.header("📋 View Inventory")
    inventory = st.session_state.inventory

    search = st.text_input("Search by Product Name")
    filter_type = st.selectbox("Filter by Type", ["All", "Electronics", "Grocery", "Clothing"])

    products = inventory.list_all_products()

    # Apply filters
    if search:
        products = [p for p in products if search.lower() in p.name.lower()]
    if filter_type != "All":
        products = [p for p in products if type(p).__name__ == filter_type]

    if products:
        # Convert product objects to dicts
        rows = []
        for p in products:
            base = {
                "ID": p.product_id,
                "Name": p.name,
                "Type": type(p).__name__,
                "Price": p.price,
                "Stock": p.quantity_in_stock
            }

            # Add specific fields per product type
            if hasattr(p, "brand"):
                base["Brand"] = p.brand
            if hasattr(p, "warranty_years"):
                base["Warranty (yrs)"] = p.warranty_years
            if hasattr(p, "expiry_date"):
                base["Expiry Date"] = p.expiry_date.strftime("%Y-%m-%d")
                base["Status"] = "Expired" if p.is_expired() else "Fresh"
            if hasattr(p, "size"):
                base["Size"] = p.size
            if hasattr(p, "material"):
                base["Material"] = p.material

            rows.append(base)

        df = pd.DataFrame(rows)
        st.dataframe(df)
    else:
        st.info("No products match the filter.")
