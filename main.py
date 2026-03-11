import os   # 上書き防止用にosをインポート
from pypdf.errors import PdfStreamError    # エラーのインポート
from pdf_tools import read_pdf, show_pdf_info, merge_pdfs, split_pdf, extract_text  # 関数インポート

def file_name_check(save_file_name):
    if os.path.exists(save_file_name):
        user_confirmation = (input(f"すでに{save_file_name}は存在します\n上書きしますか？: y/n"))
        return user_confirmation
    else:
        return "y"
    
while True:
    print("以下のメニューから番号を選択してください")
    user_input = input(f"1: PDF読取\n 2: メタデータ表示\n 3: PDF結合\n 4: PDF分割\n 5: テキスト抽出\n 6: 終了")    # メニュー
    input_list = ["1", "2", "3", "4", "5", "6"]
    if user_input not in input_list:
        print("無効な入力です")
        continue
    if user_input == "1":
        file_path = input("PDFのファイルパスを入力してください: ")
        try:
            read_pdf(file_path)
        except FileNotFoundError:
            print("ファイルが見つかりません")
        except PdfStreamError:
            print("有効なPDFファイルを指定してください")
    elif user_input == "2":
        file_path = input("パスを入力してください: ")
        try:
            show_pdf_info(file_path)
        except FileNotFoundError:
            print("ファイルが見つかりません")
        except PdfStreamError:
            print("有効なPDFファイルを指定してください")
    elif user_input == "3":
        path1 = input("PDF1: パスを入力してください: ")
        path2 = input("PDF2: パスを入力してください: ")
        try:
            file_list = [path1, path2]
            save_file_name = input("保存するファイル名を入力してください: ") + ".pdf"
            result = file_name_check(save_file_name)
            if result == "y":
                merge_pdfs(file_list, save_file_name)
            elif result == "n":
                print("中止してメニューに戻ります")
                continue
            else:
                print("yかnを入力してください")
                continue
        except FileNotFoundError: 
            print("ファイルが見つかりません")
        except PdfStreamError:
            print("有効なPDFファイルを指定してください")
    elif user_input == "4":
        input_path = input("分割するPDFのパスを入力してください: ")
        try:
            start_page = int(input("最初のページを入力してください: "))
            end_page = int(input("最後のページを入力してください: "))
            save_file_name = input("保存するファイル名を入力してください: ") + ".pdf"
            result = file_name_check(save_file_name)
            if result == "y":
                split_pdf(input_path, start_page, end_page, save_file_name)            
            elif result == "n":    
                print("中止してメニューに戻ります")
                continue
            else:
                print("yかnを入力してください")
                continue
        except (FileNotFoundError, ValueError, PdfStreamError):
            print("入力が正しくありません")
    elif user_input == "5":
        input_path = input("テキストを抽出するPDFのパスを入力してください: ")
        try:
            start_page = int(input("最初のページを入力してください: "))
            end_page = int(input("最後のページを入力してください: "))
            save_file_name = input("保存するファイル名を入力してください: ") + ".txt"
            result = file_name_check(save_file_name)
            if result == "y":
                text_file = extract_text(input_path, start_page, end_page, save_file_name)
            elif result == "n":
                print("中止してメニューに戻ります")
                continue
            else:
                print("yかnを入力してください")
                continue
        except (FileNotFoundError, ValueError, PdfStreamError):
            print("入力が正しくありません")
    else:
        print("終了します")
        break 