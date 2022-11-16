import requests
import streamlit as st
import json
import pandas as pd
import os
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

input = st.text_area("Enter paragraph")
if input != "" and input is not None:
    response = openai.Completion.create(
  model="text-davinci-002",
  prompt="A table with definition and keywords:\n\n" + input + "\n\n| keyword | definition",
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)["choices"][0]["text"]
    st.header("Copy and paste this into quizlet to import this study deck...")
    st.write(response)

with st.expander("Help/How To"):
    st.subheader("1) Enter text from a textbook or article into the text field above")
    st.subheader("2) Go to quizlet and click on create study set")
    st.subheader("3) Click on + import from word, excel, google docs, etc")
    st.subheader("4) Follow the setup in the image below...")
    st.image("./assets/QuizletDemo.png")