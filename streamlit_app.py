import streamlit as st
import pandas as pd
import numpy as np
import time

# 페이지 제목과 설명
st.title("Streamlit 요소 예시 페이지")
st.header("헤더 예시")
st.subheader("서브헤더 예시")
st.text("이것은 일반 텍스트입니다.")

# 마크다운 사용 예시
st.markdown("""
**마크다운**을 사용하면 *굵게*, _기울임_, [링크](https://streamlit.io) 등 다양한 서식을 적용할 수 있습니다.
- 리스트
- 여러 줄
""")

# 코드 블록 표시
st.code("print('Hello, Streamlit!')", language='python')

# 메시지 박스들
st.info("이것은 정보 메시지입니다.")
st.success("이것은 성공 메시지입니다!")
st.warning("이것은 경고 메시지입니다!")
st.error("이것은 에러 메시지입니다!")
try:
    st.exception(Exception("예외 메시지 예시"))
except Exception:
    pass

# 입력 위젯들
name = st.text_input("이름을 입력하세요")
bio = st.text_area("자기소개를 입력하세요")
age = st.number_input("나이를 입력하세요", min_value=0, max_value=120, value=25)
height = st.slider("키를 선택하세요(cm)", 100, 200, 170)
color = st.color_picker("좋아하는 색을 선택하세요")
agree = st.checkbox("동의합니다")
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
hobbies = st.multiselect("취미를 선택하세요", ["독서", "운동", "음악", "여행"])
date = st.date_input("날짜를 선택하세요")
time_value = st.time_input("시간을 선택하세요")
uploaded_file = st.file_uploader("파일을 업로드하세요")

if st.button("클릭하세요"):
    st.write("버튼이 클릭되었습니다!")

# 사이드바
st.sidebar.title("사이드바 제목")
sidebar_option = st.sidebar.selectbox("옵션을 선택하세요", ["옵션1", "옵션2", "옵션3"])

# 데이터 표시
df = pd.DataFrame({
    "A": np.random.randn(5),
    "B": np.random.rand(5)
})
st.write("데이터프레임 예시:")
st.dataframe(df)
st.table(df)

# 차트 그리기
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)


# 이미지
st.image("https://static.streamlit.io/examples/dog.jpg", caption="강아지 이미지", use_column_width=True)

# 오디오/비디오
# 안전하게 임의 오디오 파일 만들기 (wav 파일 형태)
import io

# 진행 바
progress = st.progress(0)
for i in range(1, 101):
    progress.progress(i)
    time.sleep(0.01)

# 스피너
with st.spinner("잠시만 기다려주세요..."):
    time.sleep(1)

# 캡션, 구분선, 빈 공간
st.caption("이것은 캡션입니다.")

# 구분선 (버전 호환 고려)
if hasattr(st, "divider"):
    st.divider()
else:
    st.markdown("---")

st.write("")

# Expander
with st.expander("더보기"):
    st.write("이 영역은 펼칠 수 있습니다.")

# 상태 메시지(토스트) - 버전 호환성 체크
if hasattr(st, "toast"):
    st.toast("상태 메시지(토스트)", icon="🎉")

# 끝!
