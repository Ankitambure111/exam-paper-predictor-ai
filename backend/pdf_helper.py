from pypdf import PdfReader

def get_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Let's test it! 
# (Put a sample pdf in your folder and change 'test.pdf' to its name)
# print(get_text_from_pdf("test.pdf"))