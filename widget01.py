import streamlit as st
import pandas as pd
from datetime import datetime

data = {
    '例1' : [1,2,3,4],
    '例2' : [20,33,33,21]
}

#タイトル表示
st.title('タイトル表示します')

#ヘッダー表示
st.header('これはヘッダーです')

#サブヘッダーを表示
st.subheader('これはサブヘッダーです')

#テキストを表示
st.text('これはテキストです')

#マークダウン形式
st.markdown('### これは小見出しです これはマークダウン形式です')

#キャプション表示（薄い色）
st.caption('キャプション表示です')

#コードをわかりやすく表示
st.code('コードを表示できます print(test)') 

#数式をおしゃれに表示
st.latex('LATEX形式の数式を表示します x=y^3')

#自動でフォーマットを検知し、表示してくれる
st.write('テキスト、データフレーム、マークダウンなどを自動フォーマットで表示 ')

#データフレーム表示
st.dataframe(data)

#表を表示
st.table(data)

#ボタン表示
st.button('ボタンを表示します')

#ダウンロードボタン表示
st.download_button(
    label="Download Text File",
    data="test",
    file_name="test.txt",
    mime="text/plain"
)
#チェックボックス
st.checkbox('チェックボックス')

# ラジオボタンの選択肢
option = st.radio(
    "選択してください:",
    ("オプション 1", "オプション 2", "オプション 3")
)
st.write(f"選択されたオプション: {option}")

# セレクトボックスの選択肢
option1 = st.selectbox(
    '選択してください:',
    ['選択肢 1', '選択肢 2', '選択肢 3']
)
st.write(f"選択されたオプション: {option1}")

# マルチセレクトの選択肢
options = st.multiselect(
    '選択してください:',
    ['アイテム 1', 'アイテム 2', 'アイテム 3', 'アイテム 4']
)
st.write(f"選択されたアイテム: {options}")

# スライダーを表示
value = st.slider(
    "スライダーを動かして値を選択してください:",
    min_value=0,
    max_value=100,
    value=50
)
st.write(f"選択された値: {value}")

# スライダーの選択肢を指定
values = st.select_slider(
    '選択してください:',
    options=['低', '中', '高'],
    value='中'
)
st.write(f"選択された値: {values}")

# テキスト入力を表示
text = st.text_input("テキストを入力してください:")
st.write(f"入力されたテキスト: {text}")

# 数値入力を表示
number = st.number_input(
    "数値を入力してください:",
    min_value=0,
    max_value=100,
    value=10,
    step=1
)
st.write(f"入力された数値: {number}")

# テキストエリアを表示
text_area = st.text_area("テキストエリアに入力してください:")
st.write(f"入力されたテキスト: {text_area}")

# 日付入力を表示
date = st.date_input(
    "日付を選択してください:",
    value=datetime.today()
)
st.write(f"選択された日付: {date}")