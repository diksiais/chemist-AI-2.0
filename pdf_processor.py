# pdf_processor.py
import PyPDF2
import io
import streamlit as st

def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from an uploaded PDF file.
    Args:
        uploaded_file: A file-like object from st.file_uploader.
    Returns:
        A string containing all extracted text from the PDF, or an error message.
    """
    try:
        # PyPDF2 needs a byte stream, so we use BytesIO
        pdf_file = io.BytesIO(uploaded_file.getvalue())
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        st.error(f"Error extracting text from PDF '{uploaded_file.name}': {e}")
        return f"Error extracting text from PDF: {e}"

def get_combined_uploaded_text():
    """
    Combines text from all uploaded papers stored in session state.
    Returns:
        A single string containing all extracted text, or an empty string if none.
    """
    combined_text = ""
    if st.session_state.uploaded_papers_data:
        for paper_info in st.session_state.uploaded_papers_data:
            combined_text += f"\n--- Start of Document: {paper_info['name']} ---\n"
            combined_text += paper_info['extracted_text']
            combined_text += f"\n--- End of Document: {paper_info['name']} ---\n"
    return combined_text

