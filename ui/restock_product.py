import streamlit as st

def render():
    st.header("🔄 Restock Product")
    inventory = st.session_state.inventory

    products = inventory.list_all_products()
    product_map = {f"{p.product_id} - {p.name}": p.product_id for p in products}

    if not product_map:
        st.warning("No products available.")
        return

    selected = st.selectbox("Select Product", list(product_map.keys()))
    quantity = st.number_input("Quantity to Add", min_value=1)

    if st.button("Restock"):
        try:
            inventory.restock_product(product_map[selected], quantity)
            st.success(f"{quantity} Pc(s) of {selected} restocked successfully!")
        except Exception as e:
            st.error(f"Error: {e}")
