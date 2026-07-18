import streamlit as st
from chatbot import get_response

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="AI Customer Support Assistant",
    page_icon="🤖",
    layout="wide"
)

# ---------------- Sidebar ----------------
with st.sidebar:
    st.title("🤖 AI Support")

    st.markdown("### 📌 Sample Questions")
    st.markdown("""
- How long does shipping take?
- Can I track my order?
- What is your return policy?
- How long do refunds take?
- Track my order ORD1002
- What payment methods do you accept?
- Do your products come with a warranty?
    """)

    st.divider()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------- Main Page ----------------
st.title("🤖 AI Customer Support Assistant")
st.caption("Powered by LangChain + Gemini")

st.info(
    "Welcome! Ask questions about shipping, returns, refunds, payments, warranty, or track your order."
)

# ---------------- Chat History ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- Chat Input ----------------
user_question = st.chat_input("Ask your question...")

if user_question:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    with st.chat_message("user"):
        st.markdown(user_question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_response(user_question)

        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

# ---------------- Footer ----------------
st.divider()
st.caption("Built using Python • LangChain • Gemini • Streamlit")