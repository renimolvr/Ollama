import streamlit as st
import pandas as pd
import ollama

def generate_report(df):
    # Convert DataFrame to a readable format
    data_summary = df.describe().to_string()
    
    # Define the prompt for Ollama
    prompt = f"""
    I have sales data in CSV format. Here is a summary of the numerical columns:

    {data_summary}

    Generate a structured documentation report that includes:
    1. **Introduction** - Overview of the sales data.
    2. **Key Insights** - Trends in sales and profits.
    3. **Performance Analysis** - Best and worst performing regions and products.
    4. **Recommendations** - Suggestions based on trends.
    5. **Conclusion** - Summary of findings.

    Format the response in **Markdown** with proper headings (`#`, `##`, `-` for lists).
    """
    
    # Send the prompt to Ollama's Llama 3.2
    response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": prompt}])
    
    # Extract the Markdown content
    markdown_report = response["message"]["content"]
    
    return markdown_report

# Streamlit App
st.title("Sales Data Report Generator")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Preview of Data:")
    st.dataframe(df.head())
    
    if st.button("Generate Report"):
        st.write("### Generating Report...")
        report = generate_report(df)
        
        # Display the report
        st.markdown(report)
        
        # Provide download option
        st.download_button("Download Report", report, "sales_report.md", "text/markdown")

