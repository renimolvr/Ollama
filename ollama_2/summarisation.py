import streamlit as st
import ollama

def summarize_text(text):
    model = "llama3.2"  
    prompt = f"Summarize the following text:\n\n{text}"
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

def main():
    st.title("Text Summarization App")
    
    uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
    user_input = st.text_area("Or enter text manually")

    if uploaded_file is not None:
        text = uploaded_file.read().decode("utf-8")
    else:
        text = user_input.strip()

    if st.button("Summarize") and text:
        summary = summarize_text(text)
        st.subheader("Summary")
        st.write(summary)

        # Download button
        st.download_button(
            label="Download Summary",
            data=summary,
            file_name="summary.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()

