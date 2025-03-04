# LiNGAM Streamlit App
## 🤔これは何？
- LiNGAM (Linear Non-Gaussian Acyclic Model) を用いた因果推論を Streamlit で可視化するアプリケーションです。
- アップロードしたCSVデータを基に、目的変数に影響を与える因果関係を可視化し、ダウンロードできるようにします。

https://github.com/user-attachments/assets/5175cb8e-faae-4ffb-a217-59a973cc2d3d

## 🔧環境構築方法
### 1. python 仮想環境の構築
python 3.9 必須（LiNGAM バージョン指定のため）
```
py -3.9 -m venv .venv
```

以下のコマンドを実行し、仮想環境を有効化してください
```
.\.venv\Scripts\activate
```

### 2. 必要なライブラリをインストール
```
pip install -r requirements.txt
```

### 3. アプリの起動
```
streamlit run main.py
```

## 📂 ファイル構成
```
.
├── main.py          # Streamlitアプリのメインスクリプト
├── process.py       # LiNGAMモデルの処理を行うスクリプト
├── requirements.txt # 必要なパッケージを記述したファイル
└── output/          # 出力画像を保存するディレクトリ
```

## 🚀 使い方
1. `streamlit run main.py` を実行し、Webブラウザでアプリを開く
2. CSVファイルをアップロード（数値データが含まれていることを確認）
3. 目的変数を選択し、「可視化」ボタンを押下
4. 因果関係を示すグラフが生成される
5. 必要に応じて画像をダウンロード可能

## ⚠️ 注意点
- CSVの欠損値がある行は自動的に削除されます
- カテゴリ変数は数値に変換されます（Ordinal Encodingを使用）
- 目的変数は 因果の終点 (sink variable) として扱われます
