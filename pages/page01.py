import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import numpy as np

# 한글 폰트 경로 지정
font_path = "./fonts/NanumGothic-Regular.ttf"

fontprop = fm.FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지

st.title("한글 폰트 테스트 페이지")
st.write("이 페이지는 NanumGothic 폰트로 한글이 깨지지 않게 표시합니다.")

df = pd.DataFrame({
    "과목": ["수학", "영어", "과학", "국어"],
    "점수": [90, 80, 85, 95]
})

st.dataframe(df)

fig, ax = plt.subplots()
ax.bar(df["과목"], df["점수"])
ax.set_title("과목별 점수", fontproperties=fontprop)
ax.set_xlabel("과목", fontproperties=fontprop)
ax.set_ylabel("점수", fontproperties=fontprop)
for label in ax.get_xticklabels():
    label.set_fontproperties(fontprop)
for label in ax.get_yticklabels():
    label.set_fontproperties(fontprop)
st.pyplot(fig)

st.info("matplotlib 차트 내 한글이 정상적으로 보이면 폰트 적용이 성공한 것입니다.")
