import random
import streamlit as st
import pandas as pd

# ======================================
# ページ設定
# ======================================

st.set_page_config(
    page_title="UIデザインシミュレーター",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"  # ← 最初から開く
)



# ======================================
# セッションステート初期化
# ======================================

if "card_bg" not in st.session_state:
    st.session_state.card_bg = "#202020"

if "card_text" not in st.session_state:
    st.session_state.card_text = "#ffffff"

if "title_color" not in st.session_state:
    st.session_state.title_color = "#00d9ff"

if "button_color" not in st.session_state:
    st.session_state.button_color = "#D06767"

# ======================================
# サイドバー
# ======================================

st.sidebar.title("🎨 UIデザインエディター")

page_bg = st.sidebar.color_picker(
    "ページ背景色",
    "#A1C7CB"
)

sidebar_bg = st.sidebar.color_picker(
    "サイドバー背景色",
    "#545454"
)

main_text = st.sidebar.color_picker(
    "全体文字色",
    "#737373"
)

# title_color = st.sidebar.color_picker(
#     "タイトル色",
#     "#00d9ff"
# )

# card_bg = st.sidebar.color_picker(
#     "カード背景色",
#     "#202020"
# )

# card_text = st.sidebar.color_picker(
#     "カード文字色",
#     "#ffffff"
# )

# button_color = st.sidebar.color_picker(
#     "ボタン色",
#     "#ff4b4b"
# )


card_bg = st.sidebar.color_picker(
    "カード背景色",
    st.session_state.card_bg
)

card_text = st.sidebar.color_picker(
    "カード文字色",
    st.session_state.card_text
)

title_color = st.sidebar.color_picker(
    "タイトル色",
    st.session_state.title_color
)

button_color = st.sidebar.color_picker(
    "ボタン色",
    st.session_state.button_color
)

# 色をセッションへ保存
st.session_state.card_bg = card_bg
st.session_state.card_text = card_text
st.session_state.title_color = title_color
st.session_state.button_color = button_color




font_size = st.sidebar.slider(
    "文字サイズ",
    12,
    40,
    18
)

radius = st.sidebar.slider(
    "角丸",
    0,
    50,
    20
)

shadow = st.sidebar.slider(
    "影の強さ",
    0,
    60,
    20
)




# ======================================
# グラデーション設定
# ======================================

st.sidebar.markdown("---")
st.sidebar.subheader("🌈 グラデーション")

use_gradient = st.sidebar.checkbox(
    "グラデーションを使用"
)

gradient_color = st.sidebar.color_picker(
    "グラデーション2色目",
    "#4ecdc4"
)

# gradient_type = st.sidebar.selectbox(
#     "グラデーション種類",
#     [
#         "線形",
#         "円形"
#     ]
# )

gradient_type = st.sidebar.radio(
    "グラデーション種類",
    ["線形", "円形"]
)

gradient_angle = st.sidebar.slider(
    "角度",
    0,
    360,
    135
)

# ======================================
# 背景生成
# ======================================

if use_gradient:

    if gradient_type == "線形":

        page_background = (
            f"linear-gradient("
            f"{gradient_angle}deg,"
            f"{page_bg},"
            f"{gradient_color})"
        )

    else:

        page_background = (
            f"radial-gradient("
            f"circle,"
            f"{page_bg},"
            f"{gradient_color})"
        )

else:

    page_background = page_bg



# ======================================
# サイドバー文字色自動判定
# ======================================

def is_light_color(hex_color):
    hex_color = hex_color.lstrip("#")

    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    brightness = (r * 299 + g * 587 + b * 114) / 1000

    return brightness > 160

sidebar_text_color = (
    "black"
    if is_light_color(sidebar_bg)
    else "white"
)

select_bg_color = (
    "white"
    if is_light_color(sidebar_bg)
    else "#262730"
)


# ======================================
# Streamlit全体デザイン
# ======================================

st.markdown(
    f"""
<style>

/* ==========================
ページ全体
========================== */

html,
body,
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] > .main
{{
    background:{page_background} !important;
    color:{main_text} !important;
}}

/* ==========================
メインエリア
========================== */

section.main
{{
    background:transparent !important;
}}

/* ==========================
サイドバー
========================== */

[data-testid="stSidebar"]
{{
    background:{sidebar_bg} !important;
}}

/* サイドバー文字 */

[data-testid="stSidebar"] *
{{
    color:{sidebar_text_color} !important;
}}



/* SelectBox */

[data-testid="stSidebar"] .stSelectbox *
{{
    color:{sidebar_text_color} !important;
}}

/* ColorPicker */

[data-testid="stSidebar"] .stColorPicker *
{{
    color:{sidebar_text_color} !important;
}}

/* Slider */

[data-testid="stSidebar"] .stSlider *
{{
    color:{sidebar_text_color} !important;
}}


/* ==========================
タイトル
========================== */

h1,h2,h3,h4,h5,h6
{{
    color:{title_color} !important;
}}

/* ==========================
本文
========================== */

p,label,span
{{
    color:{main_text} !important;
}}

/* ==========================
ボタン
========================== */

.stButton > button
{{
    background:{button_color} !important;
    color:white !important;
    border:none !important;
    border-radius:{radius}px !important;
    transition:0.3s;
}}

.stButton > button:hover
{{
    transform:scale(1.05);
}}

/* ==========================
入力欄
========================== */

.stTextInput input
{{
    border-radius:{radius}px !important;
}}

.stTextArea textarea
{{
    border-radius:{radius}px !important;
}}

.stSelectbox div[data-baseweb="select"]
{{
    border-radius:{radius}px !important;
}}

/* ==========================
カードアニメーション
========================== */

.preview-card
{{
    transition:0.3s;
}}

.preview-card:hover
{{
    transform:translateY(-8px);
}}

</style>
""",
    unsafe_allow_html=True
)




st.markdown(f"""
<style>

[data-testid="stSidebar"] *
{{
    color:{sidebar_text_color} !important;
}}

[data-testid="stSidebar"] .stSelectbox *
{{
    color:{sidebar_text_color} !important;
}}

[data-testid="stSidebar"] .stColorPicker *
{{
    color:{sidebar_text_color} !important;
}}

[data-testid="stSidebar"] .stSlider *
{{
    color:{sidebar_text_color} !important;
}}
</style>
""", unsafe_allow_html=True)


# ======================================
# メインUI
# ======================================

st.title("🎨 UIデザインシミュレーター")

title = st.text_input(
    "サイトタイトル",
    "My Website"
)

desc = st.text_area(
    "説明文",
    "ここに説明を書きます"
)

button_text = st.text_input(
    "ボタン名",
    "クリック"
)

st.markdown("---")


if st.button("🎲 ランダム配色生成"):

    st.session_state.card_bg = (
        f"#{random.randint(0,0xFFFFFF):06x}"
    )

    st.session_state.card_text = (
        f"#{random.randint(0,0xFFFFFF):06x}"
    )

    st.session_state.title_color = (
        f"#{random.randint(0,0xFFFFFF):06x}"
    )

    st.session_state.button_color = (
        f"#{random.randint(0,0xFFFFFF):06x}"
    )

    st.rerun()


# ======================================
# プレビュー
# ======================================

st.subheader("🖥️ プレビュー")

st.markdown(
    f"""
<style>

.preview-card {{
    background:{card_bg};
    padding:40px;
    border-radius:{radius}px;
    box-shadow:0 0 {shadow}px rgba(0,0,0,0.4);
    text-align:center;
    transition:0.3s;
}}

.preview-card:hover {{
    transform:translateY(-8px);
}}

.preview-title {{
    color:{title_color} !important;
    font-size:48px;
    margin-bottom:20px;
}}

.preview-text {{
    color:{card_text} !important;
    font-size:{font_size}px;
    margin-bottom:30px;
}}

.preview-btn {{
    background:{button_color};
    color:white;
    border:none;
    padding:12px 24px;
    border-radius:{radius}px;
    cursor:pointer;
}}

</style>

<div class="preview-card">

<div class="preview-title">
{title}
</div>

<div class="preview-text">
{desc}
</div>

<button class="preview-btn">
{button_text}
</button>

</div>
""",
    unsafe_allow_html=True
)





# ======================================
# デザイン評価
# ======================================

st.subheader("📊 デザイン評価")

score = 0

if use_gradient:
    score += 2

if shadow > 20:
    score += 1

if radius > 20:
    score += 1

if font_size > 24:
    score += 1

if score >= 5:
    rank = "S"
elif score >= 3:
    rank = "A"
elif score >= 2:
    rank = "B"
else:
    rank = "C"

st.metric(
    "デザインランク",
    rank
)

if rank == "S":

    st.success("🔥 プロレベルのデザイン")

    st.markdown("""
    ## 👑 Sランク達成！
    完全にプロデザイナー級です
    """)

    for _ in range(3):
        st.balloons()

elif rank == "A":

    st.info("🎨 とても良いデザイン")

    st.markdown("""
    ## ✨ Aランク
    とても洗練されたUIです
    """)

    for _ in range(2):
        st.snow()

elif rank == "B":

    st.warning("👍 良い感じ")

    st.markdown("""
    ### 😊 Bランク
    まだ改善の余地があります
    """)

else:

    st.write("🌱 シンプルデザイン")

    st.markdown("""
    ### 🌱 Cランク
    まずは色や影を追加してみよう
    """)




# ======================================
# スコアグラフ
# ======================================

# st.subheader("📈 デザイン分析")

# score_data = {
#     "配色": 2 if use_gradient else 1,
#     "影": min(shadow / 20, 5),
#     "角丸": min(radius / 10, 5),
#     "文字": min(font_size / 8, 5)
# }

# st.bar_chart(score_data)
st.subheader("📈 デザイン分析")

graph_data = pd.DataFrame({
    "項目": [
        "配色",
        "影",
        "角丸",
        "文字"
    ],
    "スコア": [
        5 if use_gradient else 2,
        min(shadow // 10, 5),
        min(radius // 10, 5),
        min(font_size // 8, 5)
    ]
})

st.bar_chart(
    graph_data.set_index("項目")
)
average_score = round(
    graph_data["スコア"].mean(),
    1
)

st.metric(
    "平均デザインスコア",
    f"{average_score}/5"
)

# ======================================
# 現在の設定表示
# ======================================

st.markdown("---")

st.subheader("⚙️ 現在の設定")

st.json({
    "ページ背景": page_bg,
    "グラデーション": use_gradient,
    "グラデーション色": gradient_color,
    "グラデーション種類": gradient_type,
    "角度": gradient_angle,
    "サイドバー背景": sidebar_bg,
    "タイトル色": title_color,
    "カード背景": card_bg,
    "カード文字": card_text,
    "ボタン色": button_color,
    "文字サイズ": font_size,
    "角丸": radius,
    "影": shadow
})
