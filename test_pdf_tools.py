import pytest
from pypdf import PdfWriter, PdfReader
from fpdf import FPDF
from pdf_tools import show_pdf_info, merge_pdfs, split_pdf, read_pdf, extract_text

def test_show_pdf_info(tmp_path, capsys):
    pdf_path = tmp_path / "test_pdf.pdf"
    writer = PdfWriter()                             # テスト用の空PDFを作成
    writer.add_blank_page(width=200, height=200)    
    with open(pdf_path, "wb", ) as f:
        writer.write(f)
    result = show_pdf_info(pdf_path)
    captured = capsys.readouterr()
    assert "ページ数: 1" in captured.out   

def test_merge_pdfs(tmp_path):
    file1_path = tmp_path / "test_pdf1.pdf"
    file2_path = tmp_path / "test_pdf2.pdf"
    file_list = [file1_path, file2_path]
    output_path = tmp_path / "test_pdf3.pdf"
    for path in file_list:
        writer = PdfWriter()
        writer.add_blank_page(width=200, height=200)    
        with open(path, "wb", ) as f:
            writer.write(f)
    result = merge_pdfs(file_list, output_path)
    reader = PdfReader(output_path)
    pages = len(reader.pages)
    assert output_path.exists() == True
    assert pages == 2

def test_split_pdf(tmp_path):
    file_path = tmp_path / "test_pdf.pdf"
    split_file_path = tmp_path / "split_pdf.pdf"
    writer = PdfWriter()
    writer.add_blank_page(width=200, height=200)    
    writer.add_blank_page(width=200, height=200)    
    with open(file_path, "wb", ) as f:
        writer.write(f)
    result = split_pdf(file_path, 1, 1, split_file_path)
    reader = PdfReader(split_file_path)
    pages = len(reader.pages)
    assert split_file_path.exists()
    assert pages == 1

# 異常系

def test_split_pdf_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_pdf("存在しない.pdf")

# 異常系

def test_show_pdf_info_file_not_found():
    with pytest.raises(FileNotFoundError):
        show_pdf_info("存在しない.pdf")

# 異常系

def test_merge_pdfs_file_not_found():
    with pytest.raises(FileNotFoundError):
        pdf_list = ["存在しない1.pdf", "存在しない2.pdf"]
        output_path = "sample.pdf"
        merge_pdfs(pdf_list, output_path)

# 異常系

def test_split_pdf_page_not_found(tmp_path):
    with pytest.raises(IndexError):
        file_path = tmp_path / "test_pdf.pdf"
        split_file_path = tmp_path / "split_pdf.pdf"
        writer = PdfWriter()
        writer.add_blank_page(width=200, height=200)    
        writer.add_blank_page(width=200, height=200)    
        with open(file_path, "wb", ) as f:
            writer.write(f)
        split_pdf(file_path, 5, 5, split_file_path)

# 正常系

def test_read_pdf(tmp_path, capsys):
    path = tmp_path / "test.pdf"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.cell(txt="Hello World", w=0)
    pdf.output(path)
    result = read_pdf(path)
    captured = capsys.readouterr()
    assert "Hello World" in captured.out

# 正常系

def test_extract_text(tmp_path):
    path1 = tmp_path / "test.pdf"
    path2 = tmp_path / "result"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.cell(txt="Hello World", w=0)
    pdf.output(path1)
    result = extract_text(path1, 1, 1, path2)
    with open(path2, "r", encoding="UTF-8") as f:
        content = f.read()
    assert "Hello World" in content 
    
 # 異常系
 
def test_extract_text_file_not_found(tmp_path):
     with pytest.raises(FileNotFoundError):
        file_path = tmp_path / "存在しない.pdf"
        text_path = tmp_path / "result" 
        extract_text(file_path, 1, 1, text_path) 