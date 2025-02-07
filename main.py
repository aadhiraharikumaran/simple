import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os


load_dotenv()


GROQ_API_KEY = os.getenv('GROQ_API_KEY')


client = Groq(api_key=GROQ_API_KEY)
MODEL = 'llama3-70b-8192'

def get_groq_response(question):
    messages = [
        {
            "role": "system",
            "content": "You are an AI assistant that answers questions."
        },
        {
            "role": "user",
            "content": question,
        }
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_tokens=4096
    )

    return response.choices[0].message.content


st.title("Simple Search App")

query = st.text_input("Enter your query:")


if st.button("Search"):
    if query:
        response = get_groq_response(query)
        st.write("Response:", response)
    else:
        st.write("Please enter a query.")
