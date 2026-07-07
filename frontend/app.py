import streamlit as st

st.set_page_config(
    page_title="OmniMind AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= CSS ====================

st.markdown("""
<style>

html, body, [class*="css"]{
    background:#0f172a;
    color:white;
    font-family:Segoe UI;
}

/* Sidebar */

section[data-testid="stSidebar"]{
    background:#111827;
    border-right:1px solid #334155;
}

/* Cards */

.card{
    background:rgba(255,255,255,0.05);
    backdrop-filter:blur(18px);
    border:1px solid rgba(255,255,255,.12);
    border-radius:20px;
    padding:22px;
    transition:.3s;
}

.card:hover{
    transform:translateY(-6px);
    border:1px solid #60a5fa;
    box-shadow:0 0 30px rgba(96,165,250,.35);
}

/* Title */

.title{
    font-size:48px;
    font-weight:700;
}

.subtitle{
    color:#94a3b8;
    font-size:18px;
}

/* Buttons */

.stButton>button{

    width:100%;
    height:60px;

    border-radius:15px;

    background:#2563eb;

    color:white;

    border:none;

    font-size:18px;

}

.stButton>button:hover{

    background:#1d4ed8;

}

</style>
""",unsafe_allow_html=True)

# ================= Sidebar ====================

with st.sidebar:

    st.title("🧠 OmniMind AI")

    st.markdown("---")

    st.button("💬 Chat")

    st.button("📄 Documents")

    st.button("💻 Coding")

    st.button("📊 Analytics")

    st.button("🧠 Research")

    st.button("🗄 SQL")

    st.button("⚙ Settings")

# ================= Header ====================

st.markdown(
"""
<div class="title">

🧠 OmniMind AI

</div>

<div class="subtitle">

Enterprise Multi-Agent AI Platform

</div>

""",
unsafe_allow_html=True
)

st.write("")

# ================= Status ====================

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.markdown("""
<div class="card">

<h2>🟢 AI</h2>

Qwen Local

</div>
""",unsafe_allow_html=True)

with c2:

    st.markdown("""
<div class="card">

<h2>📄 Documents</h2>

0 Uploaded

</div>
""",unsafe_allow_html=True)

with c3:

    st.markdown("""
<div class="card">

<h2>🤖 Agents</h2>

6 Available

</div>
""",unsafe_allow_html=True)

with c4:

    st.markdown("""
<div class="card">

<h2>⚡ Backend</h2>

Running

</div>
""",unsafe_allow_html=True)

st.write("")

# ================= Chat ====================

st.markdown("## 💬 AI Workspace")

st.chat_message("assistant").write(
    "👋 Welcome to OmniMind AI.\n\nHow can I help you today?"
)

st.chat_input("Ask anything...")