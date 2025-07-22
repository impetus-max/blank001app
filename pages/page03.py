import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 영어로만 그래프가 나오도록 폰트 설정은 생략 (축/라벨만 영어)
plt.rcParams['axes.unicode_minus'] = False

st.set_page_config(page_title="전류의 자기장 시각화", layout="wide")

st.title("⚡ 전류의 자기장 시각화 ⚡")
st.markdown("""
- **직선 전류**: y축을 따라 흐르는 전류 주위에 동심원 자기장이 비오-사바르 법칙에 의해 생성됩니다.  
- **원형 루프 전류**: 루프 중심축 방향에 강한 자기장이 형성됩니다.  
- 화살표는 자기장의 방향과 크기를 나타냅니다.
""")

# 사이드바 한글 UI
experiment_type = st.sidebar.selectbox(
    "실험 유형",
    options=["직선 전류", "원형 루프 전류"]
)
current = st.sidebar.slider("전류 세기 (A)", min_value=0.1, max_value=5.0, value=2.0, step=0.1)
field_scale = st.sidebar.slider("자기장 강도 배율", min_value=50, max_value=1000, value=300, step=50)
density = st.sidebar.slider("벡터 밀도", min_value=10, max_value=30, value=20, step=1)

# 격자 생성
X = np.linspace(-5, 5, density)
Y = np.linspace(-4, 4, density)
X, Y = np.meshgrid(X, Y)

def calculate_straight_current_field(I, x, y, field_scale):
    """
    Magnetic field by straight current (Biot–Savart law)
    """
    mu0 = 4 * np.pi * 1e-7
    r = np.abs(x) + 0.01  # Prevent division by zero
    B_magnitude = mu0 * I / (2 * np.pi * r)
    B_magnitude_scaled = B_magnitude * field_scale
    Bx = np.zeros_like(x)
    By = np.sign(-x) * np.abs(B_magnitude_scaled)
    return Bx, By

def calculate_loop_current_field(I, x, y, field_scale):
    """
    Magnetic field (approximate) by a circular current loop
    """
    mu0 = 4 * np.pi * 1e-7
    R = 3.0
    r = np.sqrt(x**2 + y**2) + 0.01
    theta = np.arctan2(y, x)

    near_loop = np.abs(r - R) < 0.5
    B_magnitude = np.zeros_like(x)
    B_magnitude[near_loop] = mu0 * I * R**2 / (2 * (R**2 + (r[near_loop] - R)**2)**1.5)
    B_magnitude_scaled = B_magnitude * field_scale * 1e6

    Bx = -np.sin(theta) * B_magnitude_scaled
    By = np.cos(theta) * B_magnitude_scaled

    inside_loop = r < R
    return Bx, By, inside_loop

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_aspect('equal')
ax.set_xlim(-5, 5)
ax.set_ylim(-4, 4)

# 그래프 제목/라벨/범례만 영어
ax.set_title(f"Magnetic Field Vectors of {'Straight Current' if experiment_type=='직선 전류' else 'Circular Loop Current'} (Current: {current:.1f} A)")
ax.set_facecolor("#f8f9fa")
ax.grid(True, alpha=0.3)

if experiment_type == "직선 전류":
    Bx, By = calculate_straight_current_field(current, X, Y, field_scale)
    ax.quiver(X, Y, Bx, By, color='blue', pivot='middle', scale=500, width=0.006)
    ax.plot([0, 0], [-4, 4], 'r-', linewidth=3, label="Current (y-axis)")
elif experiment_type == "원형 루프 전류":
    Bx, By, inside = calculate_loop_current_field(current, X, Y, field_scale)
    ax.quiver(X, Y, Bx, By, color='blue', pivot='middle', scale=500, width=0.006)
    circle = plt.Circle((0, 0), 3, color='red', fill=False, linewidth=3, label="Current Loop")
    ax.add_patch(circle)
    ax.scatter(X[inside], Y[inside], color='cyan', alpha=0.3, s=50, label="Strong B field inside loop")

ax.legend(loc='upper right')
ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")

st.pyplot(fig)
