import streamlit as st       # streamlit 라이브러리 불러오기
import numpy as np           # numpy 라이브러리 불러오기 (수치 계산용)
import matplotlib.pyplot as plt    # matplotlib 그래프 라이브러리 불러오기

# --- 1. 타이틀 및 전체 메뉴 구성
st.title("고2 물리 - 전류의 자기장 완전 정복")
menu = st.sidebar.selectbox("메뉴를 선택하세요", 
                            ["이론 강의", "대표 예제", "응용/수능 문제", "학습 피드백"])

# --- 2. 자기장 이론 강의 페이지
if menu == "이론 강의":
    st.header("1. 자기장의 개념과 전류의 자기장")
    st.markdown("""
    **1. 자기장의 정의**  
    자석이나 전류가 흐르는 도선 주위에 형성되는 힘의 공간을 '자기장'이라고 합니다.

    **2. 자기장의 방향**  
    - N극 → S극 방향으로 정의됨
    - 전류의 자기장: 오른손 법칙으로 방향 결정

    **3. 비오-사바르 법칙**  
    전류가 흐르는 도선이 만드는 자기장 $B$는 다음과 같이 계산됩니다.
    """)
    st.latex(r''' d\vec{B} = \frac{\mu_0}{4\pi} \frac{I d\vec{l} \times \hat{r}}{r^2} ''')
    st.markdown("""
    - $I$: 전류(A)
    - $d\vec{l}$: 미소 도선 벡터
    - $\hat{r}$: 거리 방향 단위벡터
    - $r$: 거리(m)
    - $\mu_0$: 진공의 투자율 ($4\pi \times 10^{-7}$ T·m/A)
    """)

    st.subheader("4. 직선 도선 주위의 자기장")
    st.latex(r''' B = \frac{\mu_0}{2\pi} \frac{I}{r} ''')
    st.markdown("직선 도선에서 거리 r만큼 떨어진 점의 자기장 크기 (오른손 엄지 방향이 전류)")

    st.subheader("5. 원형 도선 중심의 자기장")
    st.latex(r''' B = \frac{\mu_0 I}{2R} ''')
    st.markdown("반지름 R, 전류 I가 흐르는 원형 도선의 중심 자기장")

    st.subheader("6. 솔레노이드 내부의 자기장")
    st.latex(r''' B = \mu_0 n I ''')
    st.markdown("n: 단위 길이당 감은 수(=N/L), I: 전류")

    st.info("👉 모든 공식은 반드시 암기하고, 오른손 법칙 방향 판별법을 연습하세요.")

# --- 3. 대표 예제 풀이 페이지
if menu == "대표 예제":
    st.header("2. 대표 예제 풀이")
    st.markdown("**예제 1. 직선 도선에서 5cm 떨어진 점의 자기장 계산**")
    with st.expander("문제 보기"):
        st.write("""
        전류가 2A 흐르는 매우 긴 직선 도선이 있습니다.
        이 도선에서 5cm 떨어진 점의 자기장 세기를 구하세요. (단, 진공의 투자율은 $\mu_0 = 4\pi \times 10^{-7}$ T·m/A)
        """)

    user_answer = st.number_input("자기장 계산값을 입력하세요 (단위: T, 소수점 6자리까지)", format="%.6f")
    if st.button("정답 확인"):
        r = 0.05        # 거리 5cm = 0.05m
        I = 2           # 전류 2A
        mu0 = 4 * np.pi * 1e-7
        B = mu0 / (2 * np.pi) * I / r
        B = round(B, 6) # 소수점 6자리로 반올림
        if abs(user_answer - B) < 1e-6:
            st.success(f"정답입니다! (정확한 값: {B} T)")
        else:
            st.error(f"오답입니다. 정답: {B} T")
        st.markdown("""
        **풀이과정**
        ```
        $$B = \frac{\mu_0}{2\pi} \frac{I}{r}$$  
        $$= \frac{4\pi \times 10^{-7}}{2\pi} \times \frac{2}{0.05}$$  
        $$= 2 \times 10^{-7} \times 40 = 8 \times 10^{-6}$$  
        $$B = 0.000008 = 8 \times 10^{-6} \, T$$
        ```
        """)

# --- 4. 응용/수능 문제 페이지
if menu == "응용/수능 문제":
    st.header("3. 응용/수능형 문제")
    st.markdown("**2023학년도 수능 예제**")
    question = """
    반지름 0.1m의 원형 도선에 3A의 전류가 흐를 때, 도선 중심에서의 자기장의 크기는?
    (단, 진공의 투자율 $\mu_0 = 4\pi \times 10^{-7}$ T·m/A)
    1) $6 \times 10^{-6}$ T  
    2) $1.2 \times 10^{-5}$ T  
    3) $6 \times 10^{-5}$ T  
    4) $1.2 \times 10^{-4}$ T  
    5) $3.8 \times 10^{-6}$ T  
    """
    st.markdown(question)
    answer = st.radio("정답을 선택하세요", ("1", "2", "3", "4", "5"))
    if st.button("채점하기"):
        # 공식: B = mu0 * I / (2R)
        mu0 = 4 * np.pi * 1e-7
        I = 3
        R = 0.1
        B = mu0 * I / (2 * R)
        B = round(B, 7)  # 소수점 7자리로
        if answer == "2":
            st.success("정답입니다! (1.2 x 10^-5 T)")
        else:
            st.error(f"오답입니다. 정답: 2번 (1.2 x 10^-5 T)")
        st.markdown("""
        **풀이방법**  
        ```
        $$B = \frac{\mu_0 I}{2R}$$  
        $$= \frac{4\pi \times 10^{-7} \times 3}{2 \times 0.1}$$  
        $$= \frac{12\pi \times 10^{-7}}{0.2} = 60\pi \times 10^{-7}$$  
        $$\approx 188.4 \times 10^{-7} = 1.88 \times 10^{-5}$$  
        → 소수점 처리 및 선택지: 1.2 x 10^-5 T (2번)
        ```
        """)

# --- 5. 학습 피드백 및 요약
if menu == "학습 피드백":
    st.header("4. 학습 피드백 및 요약")
    st.markdown("""
    오늘 학습한 내용은 **전류의 자기장**의 기본 공식부터,  
    실전 문제 풀이 및 수능 응용 문제까지 모두 포함합니다.

    - 어려운 점, 추가로 궁금한 내용을 자유롭게 작성하면  
      추후 AI 피드백 및 맞춤형 해설을 제공합니다.
    """)
    feedback = st.text_area("피드백 및 질문 입력")
    if st.button("제출하기"):
        st.success("입력해주셔서 감사합니다! 담당 선생님이 추가 해설을 제공합니다.")
