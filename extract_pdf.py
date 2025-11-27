
import sys
try:
    from pypdf import PdfReader
except ImportError:
    print("No PDF library found")
    sys.exit(1)

try:
    reader = PdfReader("/Users/adityasinha/Downloads/TARMS-main/UCS503_Project_File(SE).pdf")
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    print(text)
except Exception as e:
    print(f"Error reading PDF: {e}")
