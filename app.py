import streamlit as st
import pandas as pd

st.title("Расчёт падения напряжения")

# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)
df = load_data(st.secrets["public_gsheets_url"])

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

# Display a static table
st.table(df)
