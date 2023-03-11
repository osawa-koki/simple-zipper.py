import os
import tempfile
import zipfile
import sys

# コマンドライン引数を取得する
args = sys.argv[1:]

# "-i"または"-input"の場合、入力ファイルパスを取得する
if "-i" in args or "--input" in args:
    index = args.index("-i") + 1 if "-i" in args else args.index("--input") + 1
    input_path = args[index]
else:
    input_path = None

# "-o"または"-output"の場合、出力ファイルパスを取得する
if "-o" in args or "--output" in args:
    index = args.index("-o") + 1 if "-o" in args else args.index("--output") + 1
    output_path = args[index]
else:
    output_path = None

# 入力ファイルパスが指定されていない場合、エラーを出力して終了する
if input_path is None:
    print("Input path is not specified.")
    sys.exit(1)

# 出力ファイルパスが指定されていない場合、エラーを出力して終了する
if output_path is None:
    print("Output path is not specified.")
    sys.exit(1)

# dataディレクトリにあるファイル一覧を取得
files = os.listdir(input_path)

data = []
# ファイル一覧をループ
for file in files:
    with open(os.path.join(input_path, file), 'rb') as f:
        # ファイルの内容を取得
        path = file
        content = f.read()
        data.append({
            'path': path,
            'content': content,
        })

zip_path = output_path
# 一時ディレクトリを作成する
with tempfile.TemporaryDirectory() as temp_dir:
    # 各ファイルを一時ディレクトリに書き込む
    for data_object in data:
        file_path = temp_dir + data_object["path"]
        with open(file_path, "wb") as f:
            f.write(data_object["content"])
    # 一時ディレクトリ内のファイルをZIPファイルに追加する
    with zipfile.ZipFile(zip_path, "w") as zip:
        for data_object in data:
            file_path = temp_dir + data_object["path"]
            zip.write(file_path, arcname=data_object["path"])
