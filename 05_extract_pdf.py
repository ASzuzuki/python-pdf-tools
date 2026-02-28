from pypdf import PdfReader

input_path = input("テキストを抽出するPDFのパスを入力してください: ")
start_page = int(input("最初のページを入力してください: "))
end_page = int(input("最後のページを入力してください: "))

def extract_text(input_path, start_page, end_page, output_path):
    reader = PdfReader(input_path)
    texts = [page.extract_text() for page in reader.pages[start_page - 1: end_page]]
    text = "".join(texts)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

text_file = extract_text(input_path, start_page, end_page, "extract.txt")