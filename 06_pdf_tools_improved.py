# インポート
from pypdf import PdfWriter, PdfReader

# PDF読取

def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = [page.extract_text() for page in reader.pages]
    for i, t in enumerate(text):
        print(f"ページ: {i}, {t}")

# PDFメタデータ抽出

def show_pdf_info(file_path):
    reader = PdfReader(file_path)
    title = reader.metadata.title
    print(f"タイトル: {title or '（未設定）'}")
    creator = reader.metadata.creator    
    print(f"作成者: {creator or '（未設定）'}")
    page = len(reader.pages)
    print(f"ページ数: {page}")
    creation_date = reader.metadata.creation_date
    print(f"作成日: {creation_date or '（未設定）'}")

# PDF結合
    
def merge_pdfs(file_list, output_path):
    writer = PdfWriter()
    for path in file_list:
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)
    with open(output_path, "wb") as f:
        writer.write(f)

# PDF分割

def split_pdf(input_path, start_page, end_page, output_path):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    pages = len(reader.pages)
    for i in range(start_page - 1, end_page):
        writer.add_page(reader.pages[i])
    with open(output_path, "wb") as f:
        writer.write(f)

# PDFテキスト抽出

def extract_text(input_path, start_page, end_page, output_path):
    reader = PdfReader(input_path)
    text = ""
    for i in range(start_page - 1, end_page):
        text += reader.pages[i].extract_text()
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)