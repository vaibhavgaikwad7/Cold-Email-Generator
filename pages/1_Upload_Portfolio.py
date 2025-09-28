import streamlit as st
import pandas as pd
from app.portfolio import Portfolio

st.title("📁 Upload Your Project Portfolio")

st.markdown("Upload a `.csv` file with the following columns: `title`, `description`, and `link`.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        if not {'title', 'description', 'link'}.issubset(df.columns):
            st.error("CSV must contain 'title', 'description', and 'link' columns.")
        else:
            st.success("✅ Portfolio uploaded successfully!")
            st.session_state['portfolio_df'] = df
    except Exception as e:
        st.error(f"❌ Failed to load CSV: {e}")
