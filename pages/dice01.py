import streamlit as st
import random

st.set_page_config(page_title="주사위 게임", page_icon="🎲")

st.title("🎲 주사위 게임")
st.write("굴릴 주사위의 개수를 정하고, 버튼을 눌러 주사위를 굴려보세요!")

# 주사위 숫자에 대응하는 이모티콘
dice_emojis = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

# 주사위 개수 선택 (사이드바)
num_dice = st.sidebar.slider("주사위 개수", min_value=1, max_value=10, value=2)

if st.button("주사위 굴리기 🎲"):
    dice_results = [random.randint(1, 6) for _ in range(num_dice)]
    emoji_str = " ".join([dice_emojis[result-1] for result in dice_results])
    st.markdown(
        f"<h1 style='font-size:70px; text-align:center;'>{emoji_str}</h1>", 
        unsafe_allow_html=True
    )
    st.info(f"결과: {' '.join(map(str, dice_results))} (총합: {sum(dice_results)})")
else:
    st.markdown(
        "<h1 style='font-size:70px; text-align:center;'>❓</h1>", 
        unsafe_allow_html=True
    )
