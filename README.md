# python-pdf-tools

PDF操作をするためのCLIアプリケーション
読取、メタデータ表示、結合、分割、テキスト抽出が可能

## セットアップ
```bash
git clone https://github.com/ASzuzuki/python-pdf-tools.git
cd python-pdf-tools
python -m venv venv
source venv/Scripts/activate  # Windows
pip install -r requirements.txt
```

## 使い方
- python main.pyを実行
- メニューが表示されるので、実行したい番号を入力
- 指示に従い、パス名や保存ファイル名を指定する

## 機能
- 読取: PDFのテキストを読み取って表示する
- メタデータ表示: PDFのメタデータ（タイトル、作成者、ページ数、作成日）を表示する
- 結合: 二つのPDFを結合する（パスを指定）
- 分割: 一つのPDFを任意のページで分割する（最初と最後のページを指定）
- テキスト抽出: 一つのPDFから、任意のページのテキストを抽出する（最初と最後のページを指定）
- 「6: 終了」を選択すると終了する

## 備考
以下のファイルは練習用に作成したもので、各メニューの機能を個別に実行可能
- 01_pdf_reader.py
- 02_pdf_metadata_extractor.py
- 03_merge_odf.py
- 04_split_pdf.py
- 05_extract_pdf.py