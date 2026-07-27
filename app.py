import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

st.set_page_config(page_title="ChatGPT App", page_icon="🤖")

if "client" not in st.session_state:
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    st.session_state.client = OpenAI(api_key=api_key) if api_key else None

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Let's start chatting! 👇"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        if st.session_state.client is None:
            assistant_response = "Please add your OpenAI API key to the .env file."
            st.markdown(assistant_response)
        else:
            try:
                response = st.session_state.client.chat.completions.create(
                    model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                    temperature=0.7,
                )
                assistant_response = response.choices[0].message.content.strip()
                st.markdown(assistant_response)
            except Exception as exc:
                assistant_response = f"Sorry, I couldn't get a response: {exc}"
                st.markdown(assistant_response)

    st.session_state.messages.append({"role": "assistant", "content": assistant_response})
