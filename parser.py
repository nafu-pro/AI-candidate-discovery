import pdfplumber

def extract_text_from_pdf(uploaded_file):
    """
    Extract text from a PDF uploaded through Streamlit.
    """
    text = ""

    try:
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

    except Exception as e:
        return f"Error reading PDF: {e}"

    return text