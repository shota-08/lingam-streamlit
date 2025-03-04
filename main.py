import streamlit as st
import pandas as pd

from process import make_lingam_plot

def init_page():
    st.set_page_config(
        page_title="LiNGAM"
    )
    st.title("LiNGAM")
    st.info("欠損がある行は削除されるので注意！")

def csv_uploader():
    encoding_options = ["cp932", "utf-8", "shift-jis"]
    selected_encoding = st.selectbox("エンコーディングを選択してください", encoding_options)
    uploaded_file = st.file_uploader(
        label = "因果プロット用ファイル（.csv）をドロップしてください",
        type = "csv",
        accept_multiple_files=False
    )
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file, encoding=selected_encoding)
            return df
        except Exception as e:
            st.error(f"ファイルアップロードエラー: {e}")

def main():
    init_page()
    df = csv_uploader()
    if df is not None and not df.empty:
        column = st.selectbox("目的変数を選択してください", df.columns)
        if st.button("可視化"):
            try:
                make_lingam_plot(df, column)
                image_path = "./output/output.png"
                st.image(image_path)

                with open(image_path, "rb") as file:
                    st.download_button(
                        label="ダウンロード",
                        data=file,
                        file_name="output.png",
                        mime="image/png",
                    )
            except Exception as e:
                st.error(f"error: {e}")

if __name__ == "__main__":
    main()