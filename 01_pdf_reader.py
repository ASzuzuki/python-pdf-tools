from pypdf import PdfReader

reader = PdfReader("Reasoning Models Don't Always Say What They Think.pdf")

pages = len(reader.pages)

for i in range(pages):
    text = reader.pages[i].extract_text()
    print(text)