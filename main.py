import os
import tempfile
import zipfile

# dataディレクトリにあるファイル一覧を取得
files = os.listdir('data')

data = []
# ファイル一覧をループ
for file in files:
    with open(f'./data/{file}', 'rb') as f:
        # ファイルの内容を取得
        path = file
        content = f.read()
        data.append({
            'path': path,
            'content': content,
        })

zip_path = "./archive.zip"
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
