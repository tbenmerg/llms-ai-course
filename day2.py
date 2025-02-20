import streamlit as st
from langchain.llms import openai
from langchain.llms import OpenAI


def set_up_app():
    st.title('my first gen AI app2222')

    st.markdown("""
    this is a sample markdown
    try it on your 'own'
    """)

    openai_api_key = st.sidebar.text_input("open AI key")
    name = st.text_input("enter some text", "enter here")
    option = st.radio("choose one option:", options = ["Option1", "Option2"], index=0)

    print(option)
    # The user should configure the temperature
    temperature = st.slider("Enter the temperature: ", 0.0, 2.0, 1.0, step=float(0.01))
    print(temperature)
    return temperature, openai_api_key

def gen_response(txt, temperature, openai_api_key):
    llm = OpenAI(temperature = temperature, openai_api_key=openai_api_key)
    st.info(llm(txt))



def set_form(temperature, openai_api_key):
    with st.form("sample app"):
        txt = st.text_area("enter text:", "what GPT stands for")
        subm = st.form_submit_button("submit")
        if subm:
            gen_response(txt, temperature=temperature, openai_api_key=openai_api_key)


def main():
    temperature, openai_api_key = set_up_app()
    set_form(temperature, openai_api_key)

main()
