from pypdf import PdfReader, PdfWriter

input_path = input("分割するPDFのパスを入力してください: ")
start_page = int(input("最初のページを入力してください: "))
end_page = int(input("最後のページを入力してください: "))


def split_pdf(input_path, start_page, end_page, output_path):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    pages = len(reader.pages)
    for i in range(start_page - 1, end_page):
        writer.add_page(reader.pages[i])
    with open(output_path, "wb") as f:
        writer.write(f)

split_pdf = split_pdf(input_path, start_page, end_page, "split.pdf")