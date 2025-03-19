import streamlit as st
from chat import hybrid_chat

st.title("🔹 Hybrid CAG + RAG Chatbot")

mode = st.radio("Choose mode:", ["CAG (Instant)", "RAG (Live Search)", "Hybrid"])
query = st.text_input("Ask me anything:")

if st.button("Get Answer"):
    response = hybrid_chat(query, mode=mode.split(" ")[0])  # Get first word of mode
    st.write(response)
