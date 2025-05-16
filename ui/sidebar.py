import streamlit as st

def sidebar_menu():
    st.sidebar.title("📊 Inventory Menu")
    return st.sidebar.radio("Go to", [
        "View Inventory",
        "Add Product",
        "Sell Product",
        "Restock Product",
    ])
