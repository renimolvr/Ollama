import pandas as pd
import ollama

def detect_fraud_in_csv(csv_file):
    """
    Reads a CSV file and uses Ollama to detect possible fraud patterns.

    Args:
        csv_file (str): Path to the CSV file.

    Returns:
        str: AI-generated fraud analysis.
    """
    try:
        df = pd.read_csv(csv_file)  # Load CSV file
        
        # Convert the data into a structured text format for Ollama
        data_text = df.head(10).to_string()  # Analyze only first 10 rows for efficiency
        
        # Create a fraud detection prompt for Ollama
        prompt = f"""
        You are a financial fraud detection expert. Analyze the following financial data and detect possible fraud patterns:
        
        {data_text}
        
        Look for:
        - Unusual input tax credit claims
        - Mismatched sales vs. tax paid
        - Duplicate transactions
        - Suspicious refunds
        - High-risk patterns

        Provide a summary of potential fraud cases.
        """
        
        # Use Ollama to analyze the data
        response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": prompt}])
        
        return response['message']['content']
    
    except Exception as e:
        return f"Error reading CSV file: {str(e)}"

# Example Usage
csv_file_path = "fraud_detection.csv"  # Replace with your CSV file
fraud_report = detect_fraud_in_csv(csv_file_path)
print("\n🚨 Fraud Detection Report 🚨\n")
print(fraud_report)

