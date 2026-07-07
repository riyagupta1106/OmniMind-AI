import streamlit as st
import requests
import time


st.set_page_config(
    page_title="OmniMind AI",
    page_icon="🧠",
    layout="wide"
)


# CSS
st.markdown(
"""
<style>

.stApp {
background: linear-gradient(135deg,#0f172a,#020617);
color:white;
}


.card{
padding:25px;
border-radius:20px;
background:rgba(255,255,255,0.08);
box-shadow:0 8px 32px rgba(0,0,0,0.3);
text-align:center;
}


h1{
text-align:center;
font-size:55px;
}

</style>

""",
unsafe_allow_html=True
)



st.title("🧠 OmniMind AI")
st.caption(
"Enterprise Multi-Agent AI Intelligence Platform"
)



menu = st.sidebar.radio(
"Navigation",
[
"🤖 AI Assistant",
"📄 Documents",
"📊 Dashboard",
"⚙️ System"
]
)


# CHAT

if menu=="🤖 AI Assistant":


    st.header("AI Assistant")


    if "messages" not in st.session_state:
        st.session_state.messages=[]



    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):
            st.write(msg["content"])



    user_input = st.chat_input(
        "Ask OmniMind..."
    )



    if user_input:


        st.chat_message("user").write(
            user_input
        )


        st.session_state.messages.append(
            {
            "role":"user",
            "content":user_input
            }
        )



        with st.spinner(
            "OmniMind is thinking..."
        ):

            res=requests.post(

            "http://127.0.0.1:8000/chat",

            json={
            "message":user_input
            }

            )


            answer=res.json()["assistant"]



        st.chat_message(
            "assistant"
        ).write(answer)


        st.session_state.messages.append(
            {
            "role":"assistant",
            "content":answer
            }
        )



elif menu=="📊 Dashboard":

    st.header(
    "Analytics Dashboard"
    )


    a,b,c=st.columns(3)


    with a:
        st.metric(
        "AI Engine",
        "ONLINE 🟢"
        )


    with b:
        st.metric(
        "Model",
        "qwen2.5:3b"
        )


    with c:
        st.metric(
        "Chats",
        len(st.session_state.get(
        "messages",[]
        ))
        )



elif menu=="⚙️ System":

    st.header(
    "System Health"
    )


    r=requests.get(
    "http://127.0.0.1:8000/health"
    )


    st.success(
    r.json()
    )


else:

    st.header("📄 Document Intelligence")

    st.write(
        "Upload documents and chat with your knowledge base"
    )


    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )


    if uploaded_file:


        with st.spinner("Processing document..."):


            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    "application/pdf"
                )
            }


            response = requests.post(
                "http://127.0.0.1:8000/rag/upload",
                files=files
            )


        if response.status_code == 200:

            st.success(
                "✅ Document processed successfully"
            )

        else:

            st.error(
                "Upload failed"
            )



    st.divider()


    question = st.text_input(
        "Ask your document"
    )


    if st.button("Ask PDF"):


        with st.spinner(
            "Searching document..."
        ):


            res=requests.post(

                "http://127.0.0.1:8000/rag/query",

                json={
                    "question":question
                }

            )


        st.write(
            res.json()["answer"]
        )