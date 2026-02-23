from pypdf import PdfReader

file_path = input("パスを入力してください: ")

def show_pdf_info(file_path):
    reader = PdfReader(file_path)
    title = reader.metadata.title
    print(f"タイトル: {title}")
    creator = reader.metadata.creator    
    print(f"作成者: {creator}")
    page = len(reader.pages)
    print(f"ページ数: {page}")
    creation_date = reader.metadata.creation_date
    print(f"作成日: {creation_date}")

show_pdf_info(file_path)
