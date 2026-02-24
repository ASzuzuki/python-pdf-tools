from pypdf import PdfReader

file_path = input("ファイルのパスを入力してください")

reader = PdfReader(file_path)
pages = len(reader.pages)

for i in range(pages):
    text = reader.pages[i].extract_text()
    print(text)