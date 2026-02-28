from pypdf import PdfReader

file_path = input("ファイルのパスを入力してください")

reader = PdfReader(file_path)
pages = len(reader.pages)

for i, item in enumerate(reader.pages):
    text = item.extract_text()
    print(f"{i}: {text}")