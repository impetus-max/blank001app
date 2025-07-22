import streamlit as st

# 1. 앱 메타 정보 설정 (페이지 타이틀 등)
st.set_page_config(
    page_title="스트림릿 기본 앱 데모",
    layout="centered",      # wide, centered 선택 가능
    initial_sidebar_state="auto"
)

# 2. 앱 타이틀과 설명
st.title("🎈 스트림릿 기본 앱 예제")
st.header("여기는 Streamlit 앱의 기본 뼈대입니다!")
st.markdown("""
**Streamlit**은 Python만으로 대화형 웹앱을 아주 쉽게 만들 수 있는 오픈소스 프레임워크입니다.

주요 기능(위젯, 입력, 레이아웃, 상태관리 등)을 간단히 아래에 데모합니다.
""")

# 3. 사이드바 예시
st.sidebar.title("사이드바")
name = st.sidebar.text_input("이름을 입력하세요", "홍길동")
age = st.sidebar.slider("나이", 10, 80, 20)

# 4. 입력 위젯 예시
st.subheader("기본 입력 위젯들")
col1, col2 = st.columns(2)

with col1:
    hobby = st.selectbox("취미를 골라주세요", ["독서", "운동", "게임", "음악감상"])
    agree = st.checkbox("동의합니다")
with col2:
    rating = st.radio("만족도(5점 척도)", [1,2,3,4,5])
    memo = st.text_area("하고 싶은 말을 적어주세요")

# 5. 버튼/액션
if st.button("입력값 요약 출력"):
    st.success(f"이름: {name}\n나이: {age}\n취미: {hobby}\n만족도: {rating}\n동의여부: {agree}\n메모: {memo}")

# 6. 파일 업로드/다운로드
st.subheader("파일 업로드 & 다운로드")
uploaded = st.file_uploader("파일을 선택하세요", type=["txt", "csv", "xlsx"])
if uploaded:
    st.write("업로드된 파일 이름:", uploaded.name)
    # 예시: 텍스트 파일 미리보기
    if uploaded.type == "text/plain":
        content = uploaded.read().decode("utf-8")
        st.text_area("파일 내용 미리보기", content, height=100)

st.download_button("샘플 텍스트 다운로드", data="안녕하세요!\n이 파일은 예시입니다.", file_name="sample.txt")

# 7. 데이터 프레임/그래프 표시
import pandas as pd
import numpy as np
st.subheader("데이터프레임 & 차트 예시")
df = pd.DataFrame({
    "수치A": np.random.randint(10, 50, 10),
    "수치B": np.random.rand(10)
})
st.dataframe(df)
st.line_chart(df)

# 8. 이미지, 코드, 경고, 주의 등
st.subheader("미디어 및 메시지 예시")
st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=150)
st.code("""
for i in range(3):
    print("Hello, Streamlit!")
""", language="python")
st.warning("이것은 경고 메시지입니다!")
st.info("이것은 정보 메시지입니다.")
st.error("이것은 에러 메시지입니다.")

# 9. 기타 상호작용/상태관리
st.subheader("상태관리 (Session State)")
if 'count' not in st.session_state:
    st.session_state.count = 0
if st.button("카운트 증가"):
    st.session_state.count += 1
st.write("카운트 값:", st.session_state.count)

st.markdown("---")
st.caption("이 예시는 Streamlit의 주요 기능을 한 번에 보여주기 위한 종합 코드입니다. 질문은 언제든 환영!")
