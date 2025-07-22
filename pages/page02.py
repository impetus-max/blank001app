import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 깨짐 방지(윈도우/맥/리눅스/코랩 공통, 환경에 맞게 폰트명 수정)
plt.rcParams['font.family'] = 'Malgun Gothic'  # 윈도우: 'Malgun Gothic', 맥: 'AppleGothic', 리눅스/코랩: 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False     # 마이너스(-) 깨짐 방지

# 페이지 제목 및 설명 표시
st.title("📊 CSV 파일 데이터 시각화")
st.write("CSV 파일을 업로드하면, 컬럼을 선택해 다양한 그래프로 시각화할 수 있습니다.")

# 파일 업로드 위젯
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

# 파일이 업로드되었는지 확인
if uploaded_file is not None:
    # 업로드한 파일에서 데이터프레임 생성
    df = pd.read_csv(uploaded_file)
    st.success("✅ 데이터 업로드 완료!")

    # 데이터 미리보기(상위 5개 행)
    st.subheader("데이터 미리보기")
    st.dataframe(df.head())

    # 숫자형 컬럼만 추출 (시각화용)
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    all_columns = df.columns.tolist()

    # 컬럼이 2개 이상일 때만 시각화 진행
    if len(numeric_columns) >= 1:
        st.subheader("시각화 옵션 선택")

        # X, Y축 컬럼 선택
        x_col = st.selectbox("X축 컬럼", all_columns, index=0)
        y_col = st.selectbox("Y축 컬럼 (숫자형만)", numeric_columns, index=0)

        # 그래프 타입 선택
        chart_type = st.selectbox("그래프 유형", ["선 그래프", "막대 그래프", "산점도", "히스토그램"])

        # 색상 및 기타 옵션
        color = st.color_picker("그래프 색상", "#4F8BF9")
        show_grid = st.checkbox("격자선 표시", True)

        st.subheader("🖼️ 그래프 미리보기")
        fig, ax = plt.subplots(figsize=(7, 4))

        # 각 유형에 따라 다른 그래프 그리기
        if chart_type == "선 그래프":
            ax.plot(df[x_col], df[y_col], marker='o', color=color)
            ax.set_title(f"{x_col} vs {y_col} (Line Chart)")
        elif chart_type == "막대 그래프":
            ax.bar(df[x_col], df[y_col], color=color)
            ax.set_title(f"{x_col}별 {y_col} (Bar Chart)")
        elif chart_type == "산점도":
            ax.scatter(df[x_col], df[y_col], color=color)
            ax.set_title(f"{x_col} vs {y_col} (Scatter Plot)")
        elif chart_type == "히스토그램":
            ax.hist(df[y_col], bins=8, color=color, edgecolor='black')
            ax.set_xlabel(y_col)
            ax.set_title(f"{y_col} 분포 (Histogram)")

        # 축 라벨, 격자 등 공통 스타일
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        if show_grid:
            ax.grid(True, linestyle='--', alpha=0.5)

        # Streamlit에 그래프 출력
        st.pyplot(fig)
    else:
        st.warning("⚠️ 숫자형 데이터가 한 개 이상 있어야 시각화가 가능합니다.")
else:
    st.info("CSV 파일을 업로드하면 데이터 미리보기 및 시각화 기능이 활성화됩니다.")

# 상세 설명
with st.expander("💡 사용법 안내"):
    st.markdown("""
    1. **CSV 파일을 업로드**하세요.
    2. **컬럼을 선택**해서 다양한 그래프를 시각화할 수 있습니다.
    3. **색상/옵션**을 바꿔가며 원하는 결과를 얻을 수 있습니다.
    4. 업로드한 데이터가 많을 때는 미리보기 표에서 상위 5개 행만 보입니다.
    """)

# --- END ---
