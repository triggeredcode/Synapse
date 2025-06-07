# views/style_view.py
import streamlit as st

def load_css():
    """Injects custom CSS to style the app."""
    css = """
    <style>
      
        /* --- Styles for Containers and Layout --- */
        .st-expander, div[data-testid="stVerticalBlock"] > [data-testid="stVerticalBlockBorderWrapper"] {
            border: 1px solid #262730 !important;
            border-radius: 10px !important;
            padding: 1rem;
        }

        h1, h2, h3 {
            padding-bottom: 1rem;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)