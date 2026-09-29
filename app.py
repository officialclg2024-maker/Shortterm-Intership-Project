
import streamlit as st
from src.assistant import answer_question

st.set_page_config(
    page_title="AI College Information Assistant",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI-Powered College Information Assistant")
st.caption("Google Cloud Generative AI • Gemini • College Knowledge Base")

st.info(
    "Ask about admissions, departments, courses, fees, facilities, "
    "hostel, transport, academic calendar, or contact information."
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask your college-related question...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Searching the college knowledge base..."):
            answer, sources = answer_question(question)
        st.markdown(answer)
        if sources:
            st.caption("Sources: " + ", ".join(sources))

    st.session_state.messages.append({"role": "assistant", "content": answer})
