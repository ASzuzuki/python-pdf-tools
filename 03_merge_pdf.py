from pypdf import PdfWriter, PdfReader

path1 = input("PDF1: パスを入力してください: ")
path2 = input("PDF2: パスを入力してください: ")

file_list = [path1, path2]  
    

def merge_pdfs(file_list, output_path):
    writer = PdfWriter()
    for path in file_list:
        reader = PdfReader(path)
        pages = len(reader.pages)
        for i in range(pages):
            merged_text = writer.add_page(reader.pages[i])
    with open(output_path, "wb") as f:
        writer.write(f)

merged_pdf = merge_pdfs(file_list, "merged.pdf")
