import streamlit as st
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain_ollama.llms import OllamaLLM
import os

st.title("Chat-BOT")

ollama_list_output = os.popen('ollama list').read()

model_names = []
for line in ollama_list_output.split('\n'):
    if line: 
        parts = line.split()
        if len(parts) > 0 and ':' in parts[0]:
            model_names.append(parts[0])

st.sidebar.subheader('Model Zoo')
model_name = st.sidebar.selectbox('Select data', model_names)

model = OllamaLLM(model=model_name, num_ctx=1000, temperature=0.0, top_k=1, max_tokens=25)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Что у вас на уме?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    system_message = SystemMessage(
        content="Ты бот-помощник. Помогай!"
    )

    messages = [system_message]

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            messages.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            messages.append(AIMessage(content=msg["content"]))

    messages.append(HumanMessage(content=prompt))

    response = model.invoke(messages)

    with st.chat_message("assistant"):
        st.markdown(response)

    ы
