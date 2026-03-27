import streamlit as st
import os
import shutil

from app.document_loader import ingest_file
from app.vector_store import VectorStore
from app.rag_engine import RAGEngine


# -------------------------
# Page config
# -------------------------
st.set_page_config(
    page_title="VH24-DocMind",
    layout="wide"
)


# -------------------------
# Custom styling (your theme)
# -------------------------
st.markdown("""
<style>

/* Base */
body {
    background-color: #ffffff;
    color: #111827;
    font-family: 'Segoe UI', sans-serif;
}

/* Title */
.title {
    font-size: 34px;
    font-weight: 800;
    background: linear-gradient(90deg, #ff7a00, #2563eb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Accent tags */
.badge {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    margin-right: 6px;
}

/* Colors */
.orange { background: #fff7ed; color: #ff7a00; }
.blue { background: #eff6ff; color: #2563eb; }
.green { background: #ecfdf5; color: #16a34a; }

/* Question box */
.question-box {
    background: #fff7ed;
    border-left: 5px solid #ff7a00;
    padding: 14px;
    border-radius: 10px;
    margin-top: 10px;
}

/* Answer box */
.answer-box {
    background: #eff6ff;
    border-left: 5px solid #2563eb;
    padding: 16px;
    border-radius: 10px;
    margin-top: 10px;
}

/* Footer */
.footer {
    text-align: center;
    padding: 20px;
    margin-top: 50px;
    border-top: 1px solid #e5e7eb;
    font-size: 14px;
    color: #6b7280;
}

.footer a {
    text-decoration: none;
    margin: 0 10px;
    color: #2563eb;
    font-weight: 500;
}

.footer a:hover {
    color: #ff7a00;
}

</style>
""", unsafe_allow_html=True)


# -------------------------
# Title
# -------------------------
st.markdown('<div class="title">VH24-DocMind</div>', unsafe_allow_html=True)

st.markdown("""
<span class="badge orange">Offline</span>
<span class="badge blue">Private</span>
<span class="badge green">No API</span>
""", unsafe_allow_html=True)

st.markdown("""
<p style="color:#6b7280;font-size:14px;">
Ask questions from your documents - powered by VH24 AI (Ollama + RAG)
</p>
""", unsafe_allow_html=True)

# -------------------------
# Init
# -------------------------
if "vs" not in st.session_state:
    st.session_state.vs = VectorStore()

if "rag" not in st.session_state:
    st.session_state.rag = RAGEngine()


# -------------------------
# Sidebar - Upload
# -------------------------
st.sidebar.header("Upload Documents")

uploaded_file = st.sidebar.file_uploader(
    "Upload PDF / TXT / MD",
    type=["pdf", "txt", "md"]
)

if uploaded_file:
    file_path = os.path.join("uploads", uploaded_file.name)

    os.makedirs("uploads", exist_ok=True)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.sidebar.success("File uploaded")

    # ingest
    chunks = ingest_file(file_path)
    st.session_state.vs.add_documents(chunks)

    st.sidebar.success("Indexed successfully")


# -------------------------
# Clear DB
# -------------------------
if st.sidebar.button("🗑 Clear Database"):
    if os.path.exists("db"):
        shutil.rmtree("db")
    st.session_state.vs = VectorStore()
    st.sidebar.success("Database cleared")


# -------------------------
# Main Input
# -------------------------
question = st.text_input("Ask something about your document:")

if question:
    st.markdown(
        f'<div class="question-box"><b>You:</b> {question}</div>',
        unsafe_allow_html=True
    )

    with st.spinner("VH24-DocMind Thinking..."):
        answer = st.session_state.rag.ask(question)

    st.markdown(
        f'<div class="answer-box"><b>Answer:</b><br>{answer}</div>',
        unsafe_allow_html=True
    )


st.markdown(
    """
<div class="footer">
© 2026 VH24-DocMind<br>
Built by Vinay Hulsurkar aka VH24<br>

<a href="https://github.com/KaizenVH24" target="_blank">GitHub</a> |
<a href="https://linkedin.com/in/vinayhulsurkar" target="_blank">LinkedIn</a> |
<a href="mailto:vinayhulsurkar@gmail.com">Email</a> |
<a href="https://vinayhulsurkar.netlify.app/" target="_blank">My Website</a>
</div>
""",
    unsafe_allow_html=True
)