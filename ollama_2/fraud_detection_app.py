import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ollama
import io

def generate_fraud_report(df, prediction):
    """Generate a fraud detection report using Ollama's Llama 3.2 model."""
    prompt = f"""
    You are an AI assistant specializing in fraud detection. Analyze the following dataset and provide insights:
    
    {df.head(10).to_string()}
    
    Based on the dataset, here are the fraud predictions:
    {prediction.to_string()}
    
    Provide a summary of possible fraud patterns, trends, and any anomalies found.
    """
    response = ollama.chat(model='llama3.2', messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

def detect_fraud(df):
    """Simple fraud detection logic based on amount threshold (for demo purposes)."""
    df['Fraud_Prediction'] = df['Amount'].apply(lambda x: 'Fraud' if x > 5000 else 'Legit')
    return df

def main():
    st.title("Fraud Detection and Analysis using Ollama Llama 3.2")
    st.write("Upload a CSV file for fraud detection and analysis.")
    
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("### Uploaded Data:")
        st.dataframe(df.head())
        
        # Perform Fraud Detection
        df = detect_fraud(df)
        st.write("### Fraud Detection Results:")
        st.dataframe(df)
        
        # Advanced Visualization
        st.write("### Data Visualizations")
        
        fig, ax = plt.subplots()
        sns.histplot(df['Amount'], bins=10, kde=True, ax=ax)
        ax.set_title("Transaction Amount Distribution")
        st.pyplot(fig)
        
        fraud_counts = df['Fraud_Prediction'].value_counts()
        fig, ax = plt.subplots()
        sns.barplot(x=fraud_counts.index, y=fraud_counts.values, ax=ax)
        ax.set_title("Fraud vs Legit Transactions")
        st.pyplot(fig)
        
        # Generate Report
        st.write("### Fraud Analysis Report")
        report = generate_fraud_report(df, df[['Amount', 'Fraud_Prediction']])
        st.text_area("Generated Report:", report, height=300)
        
        # Download Report
        output = io.StringIO()
        output.write(report)
        st.download_button("Download Report", output.getvalue(), file_name="fraud_report.txt")

if __name__ == "__main__":
    main()

