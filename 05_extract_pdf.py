from pypdf import PdfReader

input_path = input("テキストを抽出するPDFのパスを入力してください: ")
start_page = int(input("最初のページを入力してください: "))
end_page = int(input("最後のページを入力してください: "))

def extract_text(input_path, start_page, end_page, output_path):
    reader = PdfReader(input_path)
    text = ""
    for i in range(start_page - 1, end_page):
        text += reader.pages[i].extract_text()
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

text_file = extract_text(input_path, start_page, end_page, "extract.txt")