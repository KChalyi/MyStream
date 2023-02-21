import streamlit as st
import pandas as pd

st.title("A Simple Streamlit Web App")
name=st.text_input("Enter your name",' ')
st.write(f"Hello {name}!")
x=st.slider("Select an integer x",0,10,1)
y=st.slider("Select an integer y",0,10,1)
df=pd.DataFrame({"x":[x],"y":[y],"x+y":[x+y]},index=["addition row"])
st.write(df)
#@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)
df2 = load_data(st.secrets["public_gsheets_url"])
col_names=["Col1","Col2"]
df2.columns=col_names
row_names=["R1","R2"]
df2.index=row_names
st.write(df2)

# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

# Display a static table
st.table(df2)
