import openai
import streamlit as st

from streamlit_chat import message 

openai.api_key = st.secrets["api_secret"]

def generate_respone(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": prompt},
    ])

    return response['choices'][0]['message']['content']


st.title("Vincent's Chatbot")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input = st.text_input("You: ", "How are you doing", key="input")
    return input

user_input = get_text()

if user_input:
    output = generate_respone(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')