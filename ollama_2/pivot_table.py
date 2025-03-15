import streamlit as st
import pandas as pd
import ollama

# Function to generate a pivot table using Llama 3.2
def generate_pivot_table(df, index, columns, values, aggfunc):
    try:
        pivot_table = pd.pivot_table(df, index=index, columns=columns, values=values, aggfunc=aggfunc)
        return pivot_table
    except Exception as e:
        return str(e)

# Streamlit UI
st.title("Pivot Table Generator using Ollama Llama 3.2")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data Preview:")
    st.dataframe(df.head())
    
    # Select columns for pivot table
    index_col = st.multiselect("Select Index Column(s)", df.columns)
    columns_col = st.multiselect("Select Columns Column(s)", df.columns)
    values_col = st.multiselect("Select Values Column", df.columns)
    agg_func = st.selectbox("Select Aggregation Function", ["sum", "mean", "count", "max", "min"])
    
    if st.button("Generate Pivot Table"):
        if index_col and columns_col and values_col:
            pivot_result = generate_pivot_table(df, index_col, columns_col, values_col, agg_func)
            st.write("### Pivot Table Result:")
            st.dataframe(pivot_result)
        else:
            st.error("Please select at least one column for index, columns, and values.")

